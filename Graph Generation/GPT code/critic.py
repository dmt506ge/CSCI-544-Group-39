"""
Critic Module
Evaluates generated SVG diagrams using GPT Vision API and provides feedback.
"""

import json
import re
import time
import base64
import io

import cairosvg
from PIL import Image, ImageDraw
from openai import OpenAI
from config import Config


class Critic:
    """Evaluates SVG diagrams using GPT Vision API and provides structured feedback."""
    
    def __init__(self, api_key=None, model_name=None):
        """
        Initialize the critic.
        
        Args:
            api_key: OpenAI API key (defaults to Config.OPENAI_API_KEY)
            model_name: Model name to use (defaults to Config.OPENAI_MODEL)
        """
        self.api_key = api_key or Config.OPENAI_API_KEY
        self.model_name = model_name or Config.OPENAI_MODEL

        # Initialize OpenAI client
        try:
            self.client = OpenAI(api_key=self.api_key)
            print(f"OpenAI client initialized with model: {self.model_name}")
        except Exception as e:
            raise ConnectionError(f"Failed to initialize OpenAI client: {e}")

    def _render_svg(self, svg_code):
        """
        Render SVG to PNG image using CairoSVG.
        
        Args:
            svg_code: SVG code string
            
        Returns:
            PIL Image object
        """
        print("Rendering SVG to PNG...")
        try:
            png_bytes = cairosvg.svg2png(bytestring=svg_code.encode('utf-8'))
            img = Image.open(io.BytesIO(png_bytes))
            print(f"SVG rendered successfully to PNG ({img.width}x{img.height})")
            return img
        except Exception as e:
            print(f"Error rendering SVG: {e}")
            
            # Save problematic SVG code for debugging
            error_filename = f"error_render_{int(time.time())}.svg"
            try:
                with open(error_filename, "w", encoding="utf-8") as f:
                    f.write(svg_code)
                print(f"Problematic SVG code saved to {error_filename}")
            except Exception as write_e:
                print(f"Could not save problematic SVG: {write_e}")

            # Return a placeholder error image
            error_img = Image.new('RGB', (200, 50), color='red')
            d = ImageDraw.Draw(error_img)
            d.text((10, 10), "SVG Rendering Error", fill='white')
            return error_img

    def _parse_feedback(self, response_text):
        """
        Parse feedback from API response, attempt JSON parsing with fallback to text.
        
        Args:
            response_text: API response text
            
        Returns:
            Parsed feedback dictionary or raw text
        """
        try:
            # Look for JSON block in response
            json_match = re.search(r'```json\n(.*?)\n```', response_text, re.DOTALL)
            if json_match:
                feedback_json = json_match.group(1)
                return json.loads(feedback_json)
            else:
                # Try parsing the whole text
                return json.loads(response_text)
        except json.JSONDecodeError:
            print("Warning: Could not parse feedback as JSON. Returning raw text.")
            return {"raw_feedback": response_text}
        except Exception as e:
            print(f"Error parsing feedback: {e}. Returning raw text.")
            return {"raw_feedback": response_text}

    def evaluate_diagram(self, svg_code, paper_context, spatial_layout_prompt):
        """
        Evaluate diagram using GPT Vision API.
        
        Args:
            svg_code: SVG code to evaluate
            paper_context: Academic paper context
            spatial_layout_prompt: Spatial layout instructions
            
        Returns:
            Structured feedback dictionary
        """
        print("Evaluating diagram using GPT Vision...")
        rendered_image = self._render_svg(svg_code)
        if not rendered_image:
            return {"error": "Failed to render SVG for evaluation."}

        # Convert PIL Image to base64
        buffered = io.BytesIO()
        rendered_image.save(buffered, format="PNG")
        img_byte_arr = buffered.getvalue()
        img_base64 = base64.b64encode(img_byte_arr).decode('utf-8')

        prompt = f"""Please evaluate the provided diagram image based on the following criteria and context. Provide detailed feedback in JSON format within a ```json ... ``` block.

**Evaluation Criteria:**
1. **Overlapping Elements:** Are there any overlapping elements (shapes, text)?
2. **Legends:** Does the diagram incorrectly include legends? (Legends are forbidden).
3. **Arrow Placement:** Do arrows start and end accurately on the borders of the connected elements?
4. **Mechanism Detail:** Are the core mechanisms from the paper context represented with sufficient detail? Or are complex parts oversimplified?
5. **Topology Consistency:** Does the diagram's structure and flow accurately reflect the logic described in the paper context?
6. **Spatial Layout Adherence:** Does the spatial arrangement of elements follow the provided layout instructions?

**Paper Context:**
{paper_context}

**Spatial Layout Instructions:**
{spatial_layout_prompt}

**Output Format:**
Return a JSON object with keys corresponding to the criteria (e.g., "overlapping", "legends", "arrows", "mechanism_details", "topology_consistency", "spatial_layout"). For each key, provide a brief assessment string. Also include a "detailed_suggestions" key containing a list of specific, actionable suggestions for improvement.

Example JSON structure:
```json
{{
  "overlapping": "Assessment text...",
  "legends": "Assessment text...",
  "arrows": "Assessment text...",
  "mechanism_details": "Assessment text...",
  "topology_consistency": "Assessment text...",
  "spatial_layout": "Assessment text...",
  "detailed_suggestions": [
    "Suggestion 1...",
    "Suggestion 2..."
  ]
}}
```
"""

        max_retries = Config.MAX_RETRIES
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": prompt},
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/png;base64,{img_base64}"
                                    }
                                }
                            ]
                        }
                    ],
                    max_completion_tokens=10000,
                )

                # Extract feedback text
                if response.choices and len(response.choices) > 0:
                    feedback_text = response.choices[0].message.content
                else:
                    raise ValueError("Received empty response from API")

                parsed_feedback = self._parse_feedback(feedback_text)
                return parsed_feedback

            except Exception as e:
                print(f"Error during evaluation (Attempt {attempt + 1}/{max_retries}): {e}")
                if attempt == max_retries - 1:
                    return {
                        "error": "Failed to get feedback after multiple retries.",
                        "last_exception": str(e)
                    }
                time.sleep(2 ** attempt)  # Exponential backoff

        # Fallback error message
        return {"error": "Unknown error occurred during API call."}