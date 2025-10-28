# SVG Diagram Generator

An intelligent system for generating academic diagram SVGs from paper context and spatial layout descriptions using GPT API with iterative refinement.

## Features

-  **Automated Diagram Generation**: Generate SVG diagrams from academic paper context
-  **Iterative Refinement**: Agent-critic loop for continuous improvement
-  **Vision-based Evaluation**: Uses GPT Vision API to evaluate diagram quality
-  **Batch Processing**: Process multiple diagrams efficiently
-  **Secure Configuration**: Environment-based API key management

## Architecture

The system consists of three main components:

1. **Generator** (`generator.py`): Creates and improves SVG diagrams using GPT API
2. **Critic** (`critic.py`): Evaluates diagrams using GPT Vision API and provides structured feedback
3. **Agent** (`agent.py`): Orchestrates the generation-evaluation-improvement loop

## Installation

### Prerequisites

- Python 3.8+
- OpenAI API key with access to GPT-4o or GPT-5

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
   
   Then edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

## Configuration

All configuration is managed through environment variables in the `.env` file:

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | *Required* |
| `OPENAI_MODEL` | Model to use | `gpt-4` |
| `MAX_ITERATIONS` | Max refinement iterations | `3` |
| `MAX_RETRIES` | Max retry attempts on failure | `3` |
| `MAX_COMPLETION_TOKENS` | Max tokens in response | `12000` |
| `JSON_DIRECTORY` | Input JSON files directory | `""` |
| `TXT_DIRECTORY` | Input TXT files directory | `""` |
| `OUTPUT_DIRECTORY` | Output SVG files directory | `""` |

## Usage

### Basic Usage

#### 1. Generate a Single Diagram

```python
from agent import Agent

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
from agent import Agent

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
python agent.py
```

Or use individual components:

```bash
# Generate diagrams only
python generator.py

# Evaluate existing SVG
python critic.py
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
├── agent.py              # Main orchestrator
├── generator.py          # SVG diagram generator
├── critic.py            # Diagram evaluator
├── config.py            # Configuration management
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment file
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## How It Works

1. **Initial Generation**: Generator creates an SVG diagram from paper context and layout instructions
2. **Evaluation**: Critic evaluates the diagram using GPT Vision API against multiple criteria:
   - Overlapping elements
   - Legend presence (forbidden)
   - Arrow placement accuracy
   - Mechanism detail completeness
   - Topology consistency
   - Spatial layout adherence
3. **Refinement**: Based on feedback, Generator improves the diagram
4. **Iteration**: Steps 2-3 repeat until max iterations reached or no more improvements needed

## Advanced Configuration

### Custom Model Selection

```python
from agent import Agent

agent = Agent(
    openai_api_key="your-key",
    max_iterations=5  # Custom iteration count
)
```

### Using Different Models

Edit your `.env` file:
```
OPENAI_MODEL=gpt-5
```

## Troubleshooting

### Common Issues

1. **API Key Error**
   ```
   ValueError: OPENAI_API_KEY not found in environment variables
   ```
   **Solution**: Ensure `.env` file exists with valid API key

2. **SVG Rendering Error**
   ```
   Error rendering SVG: ...
   ```
   **Solution**: Check SVG code for XML special characters; the system should auto-sanitize

3. **Rate Limiting**
   ```
   Failed to call API after 3 attempts: Rate limit exceeded
   ```
   **Solution**: Add delays between requests or reduce batch size

## Security Notes

-  API keys stored in `.env` (not tracked by git)
-  `.env.example` provided for reference
-  Never commit `.env` file
-  Use environment variables in production

## Dependencies

- `openai`: OpenAI API client
- `python-dotenv`: Environment variable management
- `cairosvg`: SVG to PNG rendering
- `Pillow`: Image processing

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

[Your License Here]

## Support

For issues and questions, please open an issue on GitHub.

---

**Note**: This tool requires an OpenAI API key and will incur API usage costs based on your usage.
