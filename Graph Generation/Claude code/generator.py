"""
Diagram Generator Module
Generates SVG diagrams from paper context and spatial layout descriptions using Claude API.
"""

import json
import re
import logging
from pathlib import Path
from typing import Optional, Dict

from anthropic import Anthropic
from config import Config


class DiagramGenerator:
    """Generate program flowchart SVG diagrams based on paper context and spatial layout using Claude."""
    
    def __init__(self, api_key: Optional[str] = None, model_name: Optional[str] = None):
        """
        Initialize the diagram generator.
        
        Args:
            api_key: Anthropic API key (defaults to Config.ANTHROPIC_API_KEY)
            model_name: Model name to use (defaults to Config.ANTHROPIC_MODEL)
        """
        self.api_key = api_key or Config.ANTHROPIC_API_KEY
        self.model_name = model_name or Config.ANTHROPIC_MODEL
        self.logger = logging.getLogger('DiagramGenerator')
        
        # Initialize Anthropic client
        try:
            self.client = Anthropic(api_key=self.api_key)
            self.logger.info(f"Anthropic client initialized with model: {self.model_name}")
        except Exception as e:
            raise ConnectionError(f"Failed to initialize Anthropic client: {e}")
    
    def _sanitize_svg(self, svg_code: str) -> str:
        """
        Clean SVG code and fix XML special character issues.
        
        Args:
            svg_code: Raw SVG code
            
        Returns:
            Sanitized SVG code
        """
        # Use regex to find all text tags and their content
        def escape_text_content(match):
            tag_start = match.group(1)  # <text...>
            content = match.group(2)     # text content
            tag_end = match.group(3)     # </text>
            
            # Escape special characters in text content
            # Only escape & symbol if it's not already part of an entity reference
            content = re.sub(r'&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', content)
            
            return tag_start + content + tag_end
        
        # Process <text>...</text> tags
        svg_code = re.sub(
            r'(<text[^>]*>)(.*?)(</text>)',
            escape_text_content,
            svg_code,
            flags=re.DOTALL | re.IGNORECASE
        )
        
        # Process <tspan>...</tspan> tags
        svg_code = re.sub(
            r'(<tspan[^>]*>)(.*?)(</tspan>)',
            escape_text_content,
            svg_code,
            flags=re.DOTALL | re.IGNORECASE
        )
        
        self.logger.info("SVG sanitization completed")
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
        
        # If nothing found, return with warning
        self.logger.warning("No SVG code found in the response")
        return response_text
    
    def _call_claude_api(self, prompt: str) -> str:
        """
        Call Claude API.
        
        Args:
            prompt: Prompt text
            
        Returns:
            API response text
        """
        try:
            response = self.client.messages.create(
                model=self.model_name,
                max_tokens=Config.MAX_TOKENS,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            response_text = response.content[0].text
            
            if not response_text:
                raise ValueError(f"Response content is None. Model: {self.model_name}")
            
            return response_text
            
        except Exception as e:
            self.logger.error(f"Failed to call API: {e}")
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
        Generate initial SVG diagram.
        
        Args:
            paper_context: Academic paper context
            diagram_caption: Diagram caption/title
            spatial_layout: Spatial layout description
            
        Returns:
            Generated SVG code
        """
        prompt = f"""Generate an SVG diagram for a program flowchart/architecture diagram based on the following information.

**Important Rules:**
1. Create clean, well-structured SVG code with proper spacing
2. Ensure elements (shapes, text) do **not** overlap
3. Do **not** include any legends or legend boxes
4. Arrows must start and end precisely on the border of the elements they connect
5. Represent the core mechanisms described in the context in detail - avoid using a single large block for complex mechanisms that should be broken down into multiple components
6. Strictly adhere to the spatial layout described below
7. Use clear, readable fonts (font-size: 14-16px for main text, 12px for labels)
8. Use appropriate colors to distinguish different types of components (e.g., input/output, processing modules, data flow)
9. Add arrow markers properly for directional flow
10. This is a **program flowchart/architecture diagram**, so focus on showing:
    - Data/control flow between components
    - Processing stages and modules
    - Hierarchical relationships
    - Temporal sequences if applicable

**Paper Context:**
{paper_context}

**Diagram Caption/Focus:**
{diagram_caption}

**Spatial Layout Instructions:**
{spatial_layout}

**Output Requirements:**
- Output **only** the SVG code
- Start with `<svg` and end with `</svg>`
- Include complete SVG with all necessary definitions (markers for arrows, etc.)
- Ensure the SVG is self-contained and can be rendered directly in a browser
- Do NOT use special characters like & in text elements - use plain text only
"""
        
        self.logger.info("Generating initial diagram via API...")
        
        try:
            response_text = self._call_claude_api(prompt)
            svg_code = self._extract_svg(response_text)
            
            # Clean SVG code
            svg_code = self._sanitize_svg(svg_code)
            
            self.logger.info(f"Generated SVG length: {len(svg_code)} characters")
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
        prompt = f"""You are tasked with improving an SVG diagram based on specific feedback. Please carefully address all the points raised in the feedback while maintaining the overall structure and intent of the original diagram.

**Current SVG Code:**
```xml
{current_svg}
```

**Feedback for Improvement:**
{feedback}

**Original Context (for reference):**

Paper Context: {paper_context}

Diagram Caption/Focus: {diagram_caption}

Spatial Layout Instructions: {spatial_layout}

**Rules to Follow During Improvement:**
1. Address all points raised in the feedback
2. Maintain clean, well-structured SVG code
3. Ensure elements do not overlap
4. Do **not** include any legends
5. Arrows must start and end precisely on the border of the elements they connect
6. Represent the core mechanisms described in the context in detail
7. Adhere to the spatial layout described
8. Keep all improvements consistent with the original structure unless feedback specifically requests changes
9. Do NOT use special characters like & in text elements - use plain text only

Please output **only** the improved SVG code block, starting with `<svg` and ending with `</svg>`.
"""
        
        self.logger.info("Improving diagram via API...")
        
        try:
            response_text = self._call_claude_api(prompt)
            improved_svg = self._extract_svg(response_text)
            
            # Clean SVG code
            improved_svg = self._sanitize_svg(improved_svg)
            
            if not improved_svg.strip().lower().startswith('<svg'):
                self.logger.warning("Improved response might not be valid SVG. Returning original.")
                return current_svg
            
            self.logger.info(f"Successfully improved SVG diagram ({len(improved_svg)} chars)")
            return improved_svg
            
        except Exception as e:
            self.logger.error(f"Failed to improve diagram: {e}")
            # Return original SVG on failure
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
    logger.info("Starting Diagram Generation (Claude Sonnet 4.5)")
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