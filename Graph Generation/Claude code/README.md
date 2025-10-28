# SVG Diagram Generator (Claude Edition)

An intelligent system for generating academic diagram SVGs from paper context and spatial layout descriptions using Anthropic's Claude API with iterative refinement.

## Features

-  **Automated Diagram Generation**: Generate SVG diagrams from academic paper context using Claude
-  **Iterative Refinement**: Agent-critic loop for continuous improvement
-  **Vision-based Evaluation**: Uses Claude Vision API to evaluate diagram quality
-  **Batch Processing**: Process multiple diagrams efficiently
-  **Secure Configuration**: Environment-based API key management

## Architecture

The system consists of three main components:

1. **Generator** (`generator_anthropic.py`): Creates and improves SVG diagrams using Claude API
2. **Critic** (`critic_anthropic.py`): Evaluates diagrams using Claude Vision API and provides structured feedback
3. **Agent** (`agent_anthropic.py`): Orchestrates the generation-evaluation-improvement loop

## Installation

### Prerequisites

- Python 3.8+
- Anthropic API key with access to Claude Sonnet 4.5

### Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   ```

2. **Create and activate virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   ```bash
   cp .env.example .env
   ```
   
   Then edit `.env` and add your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=sk-ant-api03-your-actual-api-key-here
   ```

## Configuration

All configuration is managed through environment variables in the `.env` file:

| Variable | Description | Default |
|----------|-------------|---------|
| `ANTHROPIC_API_KEY` | Your Anthropic API key | *Required* |
| `ANTHROPIC_MODEL` | Model to use | `claude-sonnet-4-5` |
| `MAX_ITERATIONS` | Max refinement iterations | `3` |
| `MAX_RETRIES` | Max retry attempts on failure | `3` |
| `MAX_TOKENS` | Max tokens in response | `8192` |
| `JSON_DIRECTORY` | Input JSON files directory | `""` |
| `TXT_DIRECTORY` | Input TXT files directory | `""` |
| `OUTPUT_DIRECTORY` | Output SVG files directory | `""` |

## Usage

### Basic Usage

#### 1. Generate a Single Diagram

```python
from agent_anthropic import Agent

# Initialize agent
agent = Agent()

# Generate from files
svg_code, feedback = agent.run_from_files(
    json_path="path/to/diagram.json",
    txt_path="path/to/layout.txt",
    output_path="path/to/output.svg"
)
```

#### 2. Batch Process Multiple Diagrams

```python
from agent_anthropic import Agent

# Initialize agent
agent = Agent()

# Process all diagrams in directories
results = agent.batch_run(
    json_directory="path/to/json/files",
    txt_directory="path/to/txt/files",
    output_directory="path/to/output"
)
```

### Command Line Usage

Run the agent directly:

```bash
python agent_anthropic.py
```

Or use individual components:

```bash
# Generate diagrams only
python generator_anthropic.py

# Note: critic requires an existing SVG file
```

### Input File Format

#### JSON File (diagram context)
```json
{
  "caption": "System Architecture Diagram",
  "extracted_context": "The system consists of three main components..."
}
```

#### TXT File (spatial layout)
```
Arrange components in three layers:
- Top: Input processing modules
- Middle: Core processing engine
- Bottom: Output generation
```

## File Structure

```
.
├── agent_anthropic.py              # Main orchestrator
├── generator_anthropic.py          # SVG diagram generator
├── critic_anthropic.py            # Diagram evaluator
├── config_anthropic.py            # Configuration management
├── requirements.txt               # Python dependencies
├── .env.example                   # Example environment file
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

## How It Works

1. **Initial Generation**: Generator creates an SVG diagram from paper context and layout instructions using Claude
2. **Evaluation**: Critic evaluates the diagram using Claude Vision API against multiple criteria:
   - Overlapping elements
   - Legend presence (forbidden)
   - Arrow placement accuracy
   - Mechanism detail completeness
   - Topology consistency
   - Spatial layout adherence
3. **Refinement**: Based on feedback, Generator improves the diagram using Claude
4. **Iteration**: Steps 2-3 repeat until max iterations reached or no more improvements needed

## Advanced Configuration

### Custom Model Selection

```python
from agent_anthropic import Agent

agent = Agent(
    anthropic_api_key="your-key",
    max_iterations=5  # Custom iteration count
)
```

### Using Different Claude Models

Edit your `.env` file:
```
ANTHROPIC_MODEL=claude-opus-4
```

Available models:
- `claude-sonnet-4-5` (default, recommended for balance of speed and quality)
- `claude-opus-4` (highest quality, slower)
- Other Claude models as available

## Troubleshooting

### Common Issues

1. **API Key Error**
   ```
   ValueError: ANTHROPIC_API_KEY not found in environment variables
   ```
   **Solution**: Ensure `.env` file exists with valid API key

2. **SVG Rendering Error**
   ```
   Error rendering SVG: ...
   ```
   **Solution**: Check SVG code for XML special characters; the system should auto-sanitize. Error SVG files are saved for debugging.

3. **Rate Limiting**
   ```
   Failed to call API: Rate limit exceeded
   ```
   **Solution**: Anthropic has rate limits. Add delays between requests or reduce batch size. Consider upgrading your API tier.

## API Costs

This tool uses Anthropic's Claude API which charges based on:
- Input tokens (text sent to Claude)
- Output tokens (text received from Claude)

Typical costs per diagram:
- Initial generation: ~4,000-8,000 tokens
- Each iteration: ~6,000-10,000 tokens
- Vision evaluation: Additional cost for image processing

Check [Anthropic's pricing page](https://www.anthropic.com/pricing) for current rates.

## Security Notes

- ✅ API keys stored in `.env` (not tracked by git)
- ✅ `.env.example` provided for reference
- ✅ Never commit `.env` file
- ✅ Use environment variables in production

## Dependencies

- `anthropic`: Anthropic API client for Claude
- `python-dotenv`: Environment variable management
- `cairosvg`: SVG to PNG rendering
- `Pillow`: Image processing

## Performance Tips

1. **Batch Processing**: Process multiple diagrams in sequence rather than parallel to respect rate limits
2. **Model Selection**: Use `claude-sonnet-4-5` for faster, cost-effective results
3. **Iteration Limit**: Set appropriate MAX_ITERATIONS (3-5 typically sufficient)
4. **Error Handling**: Failed generations save error files for debugging

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

[Your License Here]

## Support

For issues and questions:
- GitHub Issues: [your-repo-issues]
- Anthropic Documentation: https://docs.anthropic.com
- API Status: https://status.anthropic.com

---

**Note**: This tool requires an Anthropic API key and will incur API usage costs. Always monitor your usage through the [Anthropic Console](https://console.anthropic.com/).

## Acknowledgments

Built with Anthropic's Claude AI family of models.
