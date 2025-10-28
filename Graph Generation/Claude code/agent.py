"""
Agent Module
Orchestrates the diagram generation-evaluation-improvement loop using Claude API.
"""

import json
from pathlib import Path

from generator import DiagramGenerator
from critic import Critic
from config import Config


class Agent:
    """Orchestrates the iterative diagram generation and improvement process using Claude."""
    
    def __init__(self, anthropic_api_key=None, max_iterations=None):
        """
        Initialize the Agent.
        
        Args:
            anthropic_api_key: Anthropic API key (defaults to Config.ANTHROPIC_API_KEY)
            max_iterations: Maximum iteration count (defaults to Config.MAX_ITERATIONS)
        """
        api_key = anthropic_api_key or Config.ANTHROPIC_API_KEY
        self.max_iterations = max_iterations or Config.MAX_ITERATIONS
        
        self.generator = DiagramGenerator(api_key=api_key)
        self.critic = Critic(api_key=api_key)

    def run(self, paper_context, diagram_caption, spatial_layout_prompt):
        """
        Run the complete generation-evaluation-improvement loop.
        
        Args:
            paper_context: Academic paper context
            diagram_caption: Diagram caption/title
            spatial_layout_prompt: Spatial layout instructions
            
        Returns:
            Tuple of (final SVG code, final feedback)
        """
        print("Starting diagram generation process...")
        current_svg = None
        feedback = None

        for i in range(self.max_iterations):
            print(f"\n{'=' * 80}")
            print(f"--- Iteration {i + 1}/{self.max_iterations} ---")
            print(f"{'=' * 80}")

            if i == 0:
                # Initial generation
                print("Generating initial diagram...")
                current_svg = self.generator.generate_initial_diagram(
                    paper_context=paper_context,
                    diagram_caption=diagram_caption,
                    spatial_layout=spatial_layout_prompt
                )
            else:
                # Improvement step
                print("Improving diagram based on feedback...")
                current_svg = self.generator.improve_diagram(
                    current_svg=current_svg,
                    feedback=self._format_feedback_for_generator(feedback),
                    paper_context=paper_context,
                    diagram_caption=diagram_caption,
                    spatial_layout=spatial_layout_prompt
                )

            print(f"Generated SVG length: {len(current_svg)} characters")

            # Evaluation step
            print("\nEvaluating diagram...")
            feedback = self.critic.evaluate_diagram(
                svg_code=current_svg,
                paper_context=paper_context,
                spatial_layout_prompt=spatial_layout_prompt
            )

            print("\n--- Critic Feedback ---")
            print(json.dumps(feedback, indent=2, ensure_ascii=False))

            # Check if should stop early
            if isinstance(feedback, dict):
                if feedback.get("error"):
                    print("\n⚠️ Stopping due to critic error.")
                    break

                suggestions = feedback.get("detailed_suggestions", [])
                if not suggestions:
                    print("\n✓ No further suggestions from critic. Stopping iterations.")
                    break

                print(f"\n📋 Received {len(suggestions)} suggestions for improvement")
            elif i > 0:
                print("\n⚠️ Warning: Unexpected feedback format received. Stopping iterations.")
                break

        print("\n" + "=" * 80)
        print("Diagram generation process finished.")
        print("=" * 80)
        
        return current_svg, feedback

    def _format_feedback_for_generator(self, feedback):
        """
        Format critic feedback into text usable by the generator.
        
        Args:
            feedback: Feedback dictionary from critic
            
        Returns:
            Formatted feedback text
        """
        if not isinstance(feedback, dict):
            return str(feedback)

        formatted_lines = []

        # Add feedback from each evaluation dimension
        criteria = [
            ("overlapping", "Overlapping Elements"),
            ("legends", "Legends"),
            ("arrows", "Arrow Placement"),
            ("mechanism_details", "Mechanism Detail"),
            ("topology_consistency", "Topology Consistency"),
            ("spatial_layout", "Spatial Layout Adherence")
        ]

        for key, label in criteria:
            if key in feedback:
                formatted_lines.append(f"**{label}:** {feedback[key]}")

        # Add detailed suggestions
        if "detailed_suggestions" in feedback and feedback["detailed_suggestions"]:
            formatted_lines.append("\n**Detailed Suggestions for Improvement:**")
            for idx, suggestion in enumerate(feedback["detailed_suggestions"], 1):
                formatted_lines.append(f"{idx}. {suggestion}")

        return "\n".join(formatted_lines) if formatted_lines else "No specific feedback provided."

    def run_from_files(self, json_path, txt_path, output_path=None):
        """
        Run complete process from JSON and TXT files.
        
        Args:
            json_path: JSON file path (contains caption and context)
            txt_path: TXT file path (contains spatial layout)
            output_path: Output SVG file path (optional)
            
        Returns:
            Tuple of (final SVG code, final feedback)
        """
        print("Loading data from files...")
        print(f"JSON: {json_path}")
        print(f"TXT: {txt_path}")

        # Load JSON file
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
        except Exception as e:
            print(f"Failed to load JSON file: {e}")
            return None, {"error": f"Failed to load JSON: {e}"}

        # Load TXT file
        try:
            with open(txt_path, 'r', encoding='utf-8') as f:
                spatial_layout = f.read()
        except Exception as e:
            print(f"Failed to load TXT file: {e}")
            return None, {"error": f"Failed to load TXT: {e}"}

        # Extract required information
        caption = json_data.get('caption', '')
        context = json_data.get('extracted_context', '')

        if not caption or not context:
            print("Missing caption or context in JSON file")
            return None, {"error": "Missing caption or context"}

        # Run the process
        final_svg, final_feedback = self.run(
            paper_context=context,
            diagram_caption=caption,
            spatial_layout_prompt=spatial_layout
        )

        # Save final SVG
        if output_path and final_svg:
            try:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(final_svg)
                print(f"\n✓ Final SVG saved to: {output_path}")
            except Exception as e:
                print(f"\n⚠️ Failed to save SVG: {e}")

        return final_svg, final_feedback

    def batch_run(
        self,
        json_directory=None,
        txt_directory=None,
        output_directory=None
    ):
        """
        Batch process multiple diagrams.
        
        Args:
            json_directory: JSON file directory (defaults to Config.JSON_DIRECTORY)
            txt_directory: TXT file directory (defaults to Config.TXT_DIRECTORY)
            output_directory: Output SVG directory (defaults to Config.OUTPUT_DIRECTORY)
            
        Returns:
            Results dictionary {filename: success status}
        """
        json_directory = json_directory or Config.JSON_DIRECTORY
        txt_directory = txt_directory or Config.TXT_DIRECTORY
        output_directory = output_directory or Config.OUTPUT_DIRECTORY
        
        print("\n" + "=" * 80)
        print("STARTING BATCH PROCESSING WITH AGENT")
        print("=" * 80)
        print(f"JSON directory: {json_directory}")
        print(f"TXT directory: {txt_directory}")
        print(f"Output directory: {output_directory}")
        print(f"Max iterations per diagram: {self.max_iterations}")
        print("=" * 80 + "\n")
        
        json_dir = Path(json_directory)
        txt_dir = Path(txt_directory)
        output_dir = Path(output_directory)
        
        # Check if directories exist
        if not json_dir.exists():
            print(f"❌ JSON directory does not exist: {json_directory}")
            return {}
        
        if not txt_dir.exists():
            print(f"❌ TXT directory does not exist: {txt_directory}")
            return {}
        
        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Find all JSON files
        json_files = sorted(list(json_dir.glob("*.json")))
        print(f"Found {len(json_files)} JSON files\n")
        
        results = {}
        successful = 0
        failed = 0
        
        for idx, json_file in enumerate(json_files, 1):
            file_stem = json_file.stem.lower()  # Convert to lowercase for matching
            
            print("\n" + "=" * 80)
            print(f"PROCESSING {idx}/{len(json_files)}: {json_file.name}")
            print("=" * 80)
            
            # Find matching TXT file (case-insensitive)
            txt_file = None
            for txt_candidate in txt_dir.glob("*.txt"):
                if txt_candidate.stem.lower() == file_stem:
                    txt_file = txt_candidate
                    break
            
            if not txt_file or not txt_file.exists():
                print(f"⚠️  No matching TXT file found for {json_file.name}")
                print(f"   Expected: {file_stem}.txt (case-insensitive)")
                results[json_file.name] = False
                failed += 1
                continue
            
            # Set output path
            output_svg_path = output_dir / f"{file_stem}.svg"
            
            # Run Agent process
            try:
                final_svg, feedback = self.run_from_files(
                    json_path=str(json_file),
                    txt_path=str(txt_file),
                    output_path=str(output_svg_path)
                )
                
                if final_svg and not feedback.get("error"):
                    print(f"\n✅ Successfully generated: {output_svg_path.name}")
                    results[json_file.name] = True
                    successful += 1
                else:
                    print(f"\n❌ Failed to generate: {json_file.name}")
                    if feedback.get("error"):
                        print(f"   Error: {feedback['error']}")
                    results[json_file.name] = False
                    failed += 1
                    
            except Exception as e:
                print(f"\n❌ Exception during processing {json_file.name}: {e}")
                results[json_file.name] = False
                failed += 1
        
        # Print final summary
        print("\n" + "=" * 80)
        print("BATCH PROCESSING SUMMARY")
        print("=" * 80)
        print(f"Total files: {len(results)}")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")
        print(f"Output directory: {output_directory}")
        print("=" * 80)
        
        # Print detailed results
        print("\nDetailed Results:")
        for filename, success in sorted(results.items()):
            status = "✅" if success else "❌"
            print(f"{status} {filename}")
        
        return results


def main():
    """Example usage."""
    # Initialize Agent
    agent = Agent()

    # Option 1: Process single file
    # final_svg, feedback = agent.run_from_files(
    #     json_path="/path/to/file.json",
    #     txt_path="/path/to/file.txt",
    #     output_path="/path/to/output.svg"
    # )

    # Option 2: Batch process all files
    results = agent.batch_run()

    print("\n" + "=" * 80)
    print("FINAL RESULTS")
    print("=" * 80)
    print(f"Total processed: {len(results)}")
    successful = sum(1 for v in results.values() if v)
    print(f"Successful: {successful}")
    print(f"Failed: {len(results) - successful}")
    print("=" * 80)


if __name__ == "__main__":
    main()