"""
Diagram Generator Module
Generates SVG diagrams from paper context and spatial layout descriptions using GPT API.
"""

import json
import re
import time
import logging
from pathlib import Path
from typing import Optional, Dict

from openai import OpenAI
from config import Config


class DiagramGenerator:
    """Generate program flowchart SVG diagrams based on paper context and spatial layout."""
    
    def __init__(self, api_key: Optional[str] = None, model_name: Optional[str] = None):
        """
        Initialize the diagram generator.
        
        Args:
            api_key: OpenAI API key (defaults to Config.OPENAI_API_KEY)
            model_name: Model name to use (defaults to Config.OPENAI_MODEL)
        """
        self.api_key = api_key or Config.OPENAI_API_KEY
        self.model_name = model_name or Config.OPENAI_MODEL
        self.logger = logging.getLogger('DiagramGenerator')
        
        # Initialize OpenAI client
        try:
            self.client = OpenAI(api_key=self.api_key)
            self.logger.info(f"OpenAI client initialized with model: {self.model_name}")
        except Exception as e:
            raise ConnectionError(f"Failed to initialize OpenAI client: {e}")
    
    def _sanitize_svg(self, svg_code: str) -> str:
        """
        Clean SVG code and fix XML special character issues (enhanced version).
        
        Args:
            svg_code: Raw SVG code
            
        Returns:
            Sanitized SVG code
        """
        # Remove BOM marker
        svg_code = svg_code.replace('\ufeff', '')
        
        # Handle special characters in attribute values (within quotes)
        def _escape_double_attr(m):
            value = m.group(1)
            value = (value.replace('&', '&amp;')
                         .replace('<', '&lt;')
                         .replace('>', '&gt;')
                         .replace('"', '&quot;'))
            return '="' + value + '"'
        svg_code = re.sub(r'="([^"]*)"', _escape_double_attr, svg_code)
        
        # Handle single quote attributes
        def _escape_single_attr(m):
            value = m.group(1)
            value = (value.replace('&', '&amp;')
                         .replace('<', '&lt;')
                         .replace('>', '&gt;')
                         .replace("'", '&apos;'))
            return "='" + value + "'"
        svg_code = re.sub(r"='([^']*)'", _escape_single_attr, svg_code)
        
        # Handle special characters in text content
        def escape_text_content(match):
            tag_start = match.group(1)
            content = match.group(2)
            tag_end = match.group(3)
            
            # Skip if already contains entity references
            if not re.search(r'&(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);', content):
                content = content.replace('&', '&amp;')
            content = content.replace('<', '&lt;').replace('>', '&gt;')
            
            return tag_start + content + tag_end
        
        # Process <text> tags
        svg_code = re.sub(
            r'(<text[^>]*>)(.*?)(</text>)',
            escape_text_content,
            svg_code,
            flags=re.DOTALL | re.IGNORECASE
        )
        
        # Process <tspan> tags
        svg_code = re.sub(
            r'(<tspan[^>]*>)(.*?)(</tspan>)',
            escape_text_content,
            svg_code,
            flags=re.DOTALL | re.IGNORECASE
        )
        
        # Remove control characters (except common whitespace)
        svg_code = re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F]', '', svg_code)
        
        # Fix tag name formatting
        svg_code = re.sub(r'<([a-zA-Z][a-zA-Z0-9:_-]*)\s+', r'<\1 ', svg_code)
        svg_code = re.sub(r'</([a-zA-Z][a-zA-Z0-9:_-]*)>', r'</\1>', svg_code)
        
        self.logger.info("Enhanced SVG sanitization completed")
        return svg_code
    
    def _extract_svg(self, response_text: str) -> str:
        """
        Extract SVG code from API response.
        
        Args:
            response_text: API response text
            
        Returns:
            Extracted SVG code
        """
        # Try to extract from code block first
        code_block_pattern = r'```(?:xml|svg)?\s*\n(.*?)\n```'
        code_match = re.search(code_block_pattern, response_text, re.DOTALL | re.IGNORECASE)
        
        if code_match:
            svg_content = code_match.group(1).strip()
            if svg_content.lower().startswith('<svg'):
                self.logger.info("Successfully extracted SVG from code block")
                return svg_content
        
        # Fallback: search for SVG tags directly
        svg_pattern = r'<svg.*?</svg>'
        svg_match = re.search(svg_pattern, response_text, re.DOTALL | re.IGNORECASE)
        
        if svg_match:
            self.logger.info("Successfully extracted SVG from raw text")
            return svg_match.group(0)
        
        self.logger.warning("No SVG code found in the response")
        return response_text
    
    def _call_api(self, prompt: str, max_retries: Optional[int] = None) -> str:
        """
        Call GPT API with retry logic.
        
        Args:
            prompt: Prompt text
            max_retries: Maximum retry attempts (defaults to Config.MAX_RETRIES)
            
        Returns:
            API response text
        """
        max_retries = max_retries or Config.MAX_RETRIES
        
        for attempt in range(max_retries):
            try:
                self.logger.info(f"Calling API (attempt {attempt + 1}/{max_retries})...")
                
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[{"role": "user", "content": prompt}],
                    max_completion_tokens=Config.MAX_COMPLETION_TOKENS,
                )
                
                response_text = response.choices[0].message.content
                
                if not response_text:
                    raise ValueError(f"Response content is None. Model: {self.model_name}")
                
                self.logger.info(f"Successfully got response: {len(response_text)} characters")
                return response_text
                
            except Exception as e:
                if attempt < max_retries - 1:
                    wait_time = (attempt + 1) * 2  # 2s, 4s, 6s
                    self.logger.warning(f"API call failed: {e}")
                    self.logger.info(f"Retrying in {wait_time}s... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(wait_time)
                else:
                    self.logger.error(f"Failed to call API after {max_retries} attempts: {e}")
                    raise
    
    def _load_json_file(self, json_path: str) -> Optional[Dict]:
        """
        Load JSON file containing diagram caption and context.
        
        Args:
            json_path: Path to JSON file
            
        Returns:
            JSON data dictionary, None if failed
        """
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.logger.info(f"Successfully loaded JSON: {json_path}")
            return data
        except Exception as e:
            self.logger.error(f"Failed to load JSON file {json_path}: {e}")
            return None
    
    def _load_txt_file(self, txt_path: str) -> Optional[str]:
        """
        Load TXT file containing spatial layout description.
        
        Args:
            txt_path: Path to TXT file
            
        Returns:
            TXT file content, None if failed
        """
        try:
            with open(txt_path, 'r', encoding='utf-8') as f:
                content = f.read()
            self.logger.info(f"Successfully loaded TXT: {txt_path}")
            return content
        except Exception as e:
            self.logger.error(f"Failed to load TXT file {txt_path}: {e}")
            return None
    
    def generate_initial_diagram(
        self,
        paper_context: str,
        diagram_caption: str,
        spatial_layout: str
    ) -> str:
        """
        Generate initial SVG diagram from paper context and spatial layout.
        
        Args:
            paper_context: Academic paper context
            diagram_caption: Diagram caption/title
            spatial_layout: Spatial layout description
            
        Returns:
            Generated SVG code
        """
        prompt = f"""You are an expert in creating technical diagrams for academic papers. Based on the provided paper context, diagram caption, and spatial layout instructions, generate a clear and professional SVG flowchart or block diagram.

**Paper Context:**
{paper_context}

**Diagram Caption:**
{diagram_caption}

**Spatial Layout Instructions:**
{spatial_layout}

**Requirements:**
1. Create a clean, well-structured SVG diagram
2. Ensure no overlapping elements
3. Do **not** include any legends in the diagram
4. Arrows must start and end precisely on the borders of connected elements
5. Represent core mechanisms from the paper context in detail
6. Follow the spatial layout instructions precisely
7. Use clear, readable fonts and appropriate colors
8. **CRITICAL**: Do NOT use special characters like &, <, >, or quotes in element names, IDs, or class names
9. **CRITICAL**: For text content, use only plain text without any special XML characters

Please output **only** the SVG code block, starting with `<svg` and ending with `</svg>`.
"""
        
        self.logger.info("Generating initial diagram via API...")
        
        try:
            response_text = self._call_api(prompt)
            svg_code = self._extract_svg(response_text)
            
            # Sanitize SVG code
            svg_code = self._sanitize_svg(svg_code)
            
            if not svg_code.strip().lower().startswith('<svg'):
                raise ValueError("Response does not contain valid SVG code")
            
            self.logger.info(f"Successfully generated initial SVG diagram ({len(svg_code)} chars)")
            return svg_code
            
        except Exception as e:
            self.logger.error(f"Failed to generate initial diagram: {e}")
            raise
    
    def improve_diagram(
        self,
        current_svg: str,
        feedback: str,
        paper_context: str,
        diagram_caption: str,
        spatial_layout: str
    ) -> str:
        """
        Improve existing SVG diagram based on feedback.
        
        Args:
            current_svg: Current SVG code
            feedback: Feedback for improvements
            paper_context: Academic paper context
            diagram_caption: Diagram caption/title
            spatial_layout: Spatial layout description
            
        Returns:
            Improved SVG code
        """
        prompt = f"""You are an expert in creating technical diagrams for academic papers. Please improve the provided SVG diagram based on the feedback below.

**Current SVG Code:**
```svg
{current_svg}
```

**Feedback for Improvement:**
{feedback}

**Paper Context:**
{paper_context}

**Diagram Caption:**
{diagram_caption}

**Spatial Layout Instructions:**
{spatial_layout}

**Requirements:**
1. Address all feedback points thoroughly
2. Maintain clean, well-structured SVG code
3. Ensure elements do not overlap
4. Do **not** include any legends
5. Arrows must start and end precisely on the border of the elements they connect
6. Represent the core mechanisms described in the context in detail
7. Adhere to the spatial layout described
8. Keep all improvements consistent with the original structure unless feedback specifically requests changes
9. **CRITICAL**: Do NOT use special characters like &, <, >, or quotes in element names, IDs, or class names
10. **CRITICAL**: For text content, use only plain text without any special XML characters

Please output **only** the improved SVG code block, starting with `<svg` and ending with `</svg>`.
"""
        
        self.logger.info("Improving diagram via API...")
        
        try:
            response_text = self._call_api(prompt)
            improved_svg = self._extract_svg(response_text)
            
            # Sanitize SVG code
            improved_svg = self._sanitize_svg(improved_svg)
            
            if not improved_svg.strip().lower().startswith('<svg'):
                self.logger.warning("Improved response might not be valid SVG. Returning original.")
                return current_svg
            
            self.logger.info(f"Successfully improved SVG diagram ({len(improved_svg)} chars)")
            return improved_svg
            
        except Exception as e:
            self.logger.error(f"Failed to improve diagram: {e}")
            return current_svg
    
    def generate_from_files(
        self,
        json_path: str,
        txt_path: str,
        output_path: Optional[str] = None
    ) -> Optional[str]:
        """
        Generate SVG diagram from JSON and TXT files.
        
        Args:
            json_path: Path to JSON file (contains caption and context)
            txt_path: Path to TXT file (contains spatial layout)
            output_path: Output SVG file path (optional)
            
        Returns:
            Generated SVG code, None if failed
        """
        self.logger.info(f"Generating diagram from: {json_path} and {txt_path}")
        
        # Load JSON file
        json_data = self._load_json_file(json_path)
        if not json_data:
            return None
        
        # Load TXT file
        spatial_layout = self._load_txt_file(txt_path)
        if not spatial_layout:
            return None
        
        # Extract required information
        caption = json_data.get('caption', '')
        context = json_data.get('extracted_context', '')
        
        if not caption or not context:
            self.logger.error("Missing caption or context in JSON file")
            return None
        
        # Generate SVG
        svg_code = self.generate_initial_diagram(
            paper_context=context,
            diagram_caption=caption,
            spatial_layout=spatial_layout
        )
        
        # Save SVG file (if output path specified)
        if output_path:
            try:
                output_path_obj = Path(output_path)
                output_path_obj.parent.mkdir(parents=True, exist_ok=True)
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(svg_code)
                
                self.logger.info(f"SVG saved to: {output_path}")
                
            except Exception as e:
                self.logger.error(f"Failed to save SVG to {output_path}: {e}")
        
        return svg_code
    
    def batch_generate_diagrams(
        self,
        json_directory: str,
        txt_directory: str,
        output_directory: str
    ) -> Dict[str, bool]:
        """
        Batch generate SVG diagrams.
        
        Args:
            json_directory: JSON file directory
            txt_directory: TXT file directory
            output_directory: Output SVG file directory
            
        Returns:
            Dictionary with filename as key and success status as value
        """
        self.logger.info("Starting batch diagram generation...")
        self.logger.info(f"JSON directory: {json_directory}")
        self.logger.info(f"TXT directory: {txt_directory}")
        self.logger.info(f"Output directory: {output_directory}")
        
        json_dir = Path(json_directory)
        txt_dir = Path(txt_directory)
        output_dir = Path(output_directory)
        
        if not json_dir.exists():
            self.logger.error(f"JSON directory does not exist: {json_directory}")
            return {}
        
        if not txt_dir.exists():
            self.logger.error(f"TXT directory does not exist: {txt_directory}")
            return {}
        
        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Find all JSON files
        json_files = list(json_dir.glob("*.json"))
        self.logger.info(f"Found {len(json_files)} JSON files")
        
        results = {}
        
        for idx, json_file in enumerate(json_files, 1):
            file_stem = json_file.stem
            self.logger.info(f"\nProcessing {idx}/{len(json_files)}: {json_file.name}")
            
            # Find matching TXT file
            txt_file = txt_dir / f"{file_stem}.txt"
            
            if not txt_file.exists():
                self.logger.warning(f"No matching TXT file found for {json_file.name}")
                self.logger.warning(f"Expected: {txt_file}")
                results[json_file.name] = False
                continue
            
            # Set output path
            output_svg_path = output_dir / f"{file_stem}.svg"
            
            # Generate SVG
            svg_code = self.generate_from_files(
                json_path=str(json_file),
                txt_path=str(txt_file),
                output_path=str(output_svg_path)
            )
            
            if svg_code:
                self.logger.info(f"✓ Successfully generated: {output_svg_path.name}")
                results[json_file.name] = True
            else:
                self.logger.warning(f"✗ Failed to generate: {json_file.name}")
                results[json_file.name] = False
            
            # Add delay to avoid rate limits
            self.logger.info("Waiting 1 second before next request...")
            time.sleep(1)
        
        # Print summary
        self.logger.info("\n" + "=" * 80)
        self.logger.info("BATCH GENERATION SUMMARY")
        self.logger.info("=" * 80)
        successful = sum(1 for v in results.values() if v)
        self.logger.info(f"Total files: {len(results)}")
        self.logger.info(f"Successful: {successful}")
        self.logger.info(f"Failed: {len(results) - successful}")
        self.logger.info(f"Output directory: {output_directory}")
        self.logger.info("=" * 80)
        
        return results


def setup_logging(log_level=logging.INFO):
    """Configure logging system."""
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('diagram_generation.log')
        ]
    )


def main():
    """Main function for testing."""
    setup_logging()
    logger = logging.getLogger('main')
    
    logger.info("=" * 80)
    logger.info("Starting Diagram Generation")
    logger.info("=" * 80)
    
    # Initialize generator
    generator = DiagramGenerator()
    
    # Batch generate SVG diagrams
    json_directory = Config.JSON_DIRECTORY or "/path/to/json/files"
    txt_directory = Config.TXT_DIRECTORY or "/path/to/txt/files"
    output_directory = Config.OUTPUT_DIRECTORY or "/path/to/output"
    
    results = generator.batch_generate_diagrams(
        json_directory=json_directory,
        txt_directory=txt_directory,
        output_directory=output_directory
    )
    
    # Print final summary
    print(f"\n{'=' * 80}")
    print("FINAL SUMMARY")
    print(f"{'=' * 80}")
    print(f"Total processed: {len(results)}")
    successful = sum(1 for v in results.values() if v)
    print(f"Successful: {successful}")
    print(f"Failed: {len(results) - successful}")
    print(f"SVG files saved to: {output_directory}")
    print(f"{'=' * 80}\n")


if __name__ == "__main__":
    main()