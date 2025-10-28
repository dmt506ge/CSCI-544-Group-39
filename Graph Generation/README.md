# SVG Diagram Generator

An intelligent system for generating academic diagram SVGs from paper context and spatial layout descriptions. This project provides **two implementations** using different AI providers:

1. **OpenAI Version** - Uses GPT-4/GPT-5 API
2. **Anthropic Version** - Uses Claude Sonnet 4.5/Opus 4 API

Both versions offer the same core functionality with provider-specific optimizations.

##  Features

-  **Automated Diagram Generation**: Generate SVG diagrams from academic paper context
-  **Iterative Refinement**: Agent-critic loop for continuous improvement
- **Vision-based Evaluation**: Uses AI Vision APIs to evaluate diagram quality
-  **Batch Processing**: Process multiple diagrams efficiently
- **Secure Configuration**: Environment-based API key management

##  Project Structure

```
.
├── GPT code/                    # OpenAI/GPT-based implementation
│   ├── agent.py
│   ├── generator.py
│   ├── critic.py
│   ├── config.py
│   ├── requirements.txt        # OpenAI dependencies (openai, python-dotenv, cairosvg, Pillow)
│   ├── .env.example            # OpenAI environment template
│   └── README.md
│
├── Claude code/                 # Anthropic/Claude-based implementation
│   ├── agent.py
│   ├── generator.py
│   ├── critic.py
│   ├── config.py
│   ├── requirements.txt        # Anthropic dependencies (anthropic, python-dotenv, cairosvg, Pillow)
│   ├── .env.example            # Anthropic environment template
│   └── README.md
│
└── README.md                    # This file
```

##  Architecture

Both implementations follow the same three-component architecture:

1. **Generator**: Creates and improves SVG diagrams using AI
2. **Critic**: Evaluates diagrams using Vision API and provides structured feedback
3. **Agent**: Orchestrates the generation-evaluation-improvement loop

### Evaluation Criteria

Both versions evaluate diagrams against:
-  Overlapping elements
-  Legend presence (forbidden)
-  Arrow placement accuracy
-  Mechanism detail completeness
-  Topology consistency
-  Spatial layout adherence

##  Quick Start

### Prerequisites

- Python 3.8+
- API key from either:
  - OpenAI (for GPT version)
  - Anthropic (for Claude version)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   ```

2. **Choose your version** and navigate to that folder:
   ```bash
   # For OpenAI version
   cd "GPT code"
   
   # OR for Anthropic version
   cd "Claude code"
   ```

3. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies** (each folder has its own requirements.txt):
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your API key:
   
   **For OpenAI version** (`GPT code/.env`):
   ```bash
   OPENAI_API_KEY=sk-your-actual-api-key-here
   OPENAI_MODEL=gpt-4
   MAX_ITERATIONS=3
   MAX_RETRIES=3
   MAX_COMPLETION_TOKENS=12000
   ```
   
   **For Anthropic version** (`Claude code/.env`):
   ```bash
   ANTHROPIC_API_KEY=sk-ant-api03-your-actual-api-key-here
   ANTHROPIC_MODEL=claude-sonnet-4-5
   MAX_ITERATIONS=3
   MAX_RETRIES=3
   MAX_TOKENS=8192
   ```

## Usage

### Choose Your Version

#### Option 1: OpenAI/GPT Version

```python
# Navigate to OpenAI version
cd "GPT code"

# Use the OpenAI implementation
from agent import Agent

agent = Agent()
svg_code, feedback = agent.run_from_files(
    json_path="path/to/diagram.json",
    txt_path="path/to/layout.txt",
    output_path="path/to/output.svg"
)
```

**Command line**:
```bash
cd "GPT code"
python agent.py
```

#### Option 2: Anthropic/Claude Version

```python
# Navigate to Anthropic version
cd "Claude code"

# Use the Claude implementation
from agent import Agent

agent = Agent()
svg_code, feedback = agent.run_from_files(
    json_path="path/to/diagram.json",
    txt_path="path/to/layout.txt",
    output_path="path/to/output.svg"
)
```

**Command line**:
```bash
cd "Claude code"
python agent.py
```

### Input Files Format

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

### Batch Processing

Both versions support batch processing:

```python
# Process all diagrams in directories
results = agent.batch_run(
    json_directory="path/to/json/files",
    txt_directory="path/to/txt/files",
    output_directory="path/to/output"
)
```

## ⚖️ Comparison: OpenAI vs Anthropic

| Feature | OpenAI Version | Anthropic Version |
|---------|----------------|-------------------|
| **Model** | GPT-4o, GPT-5 | Claude Sonnet 4.5, Opus 4 |
| **Default Model** | `gpt-4o` | `claude-sonnet-4-5` |
| **Max Tokens** | 12,000 | 8,192 |
| **Strengths** | Wide model selection | Strong reasoning, cost-effective |
| **Best For** | Established workflows | Latest AI capabilities |
| **API Docs** | [OpenAI Docs](https://platform.openai.com/docs) | [Anthropic Docs](https://docs.anthropic.com) |

### Which Version to Choose?

**Choose OpenAI Version if:**
- You already have OpenAI API access
- You need GPT-5 capabilities
- You prefer the OpenAI ecosystem

**Choose Anthropic Version if:**
- You want to use Claude's latest models
- You prefer Anthropic's API design
- You need Claude Sonnet 4.5's efficiency

**Both versions produce comparable quality diagrams!**

## Configuration

Key environment variables (applies to both versions):

| Variable | Description | Default |
|----------|-------------|---------|
| `MAX_ITERATIONS` | Max refinement iterations | `3` |
| `MAX_RETRIES` | Max retry attempts on failure | `3` |
| `JSON_DIRECTORY` | Input JSON files directory | `""` |
| `TXT_DIRECTORY` | Input TXT files directory | `""` |
| `OUTPUT_DIRECTORY` | Output SVG files directory | `""` |

**OpenAI-specific:**
- `OPENAI_API_KEY` (required)
- `OPENAI_MODEL` (default: `gpt-4`)
- `MAX_COMPLETION_TOKENS` (default: `12000`)

**Anthropic-specific:**
- `ANTHROPIC_API_KEY` (required)
- `ANTHROPIC_MODEL` (default: `claude-sonnet-4-5`)
- `MAX_TOKENS` (default: `8192`)

## Cost Considerations

### OpenAI Pricing
- Charges per token (input + output)
- GPT-4o: Higher cost, high quality
- GPT-5: Latest features, premium pricing

### Anthropic Pricing
- Charges per token (input + output)
- Vision API adds cost for image processing
- Claude Sonnet 4.5: Cost-effective, fast
- Claude Opus 4: Premium quality

**Typical cost per diagram**: $0.10 - $0.50 depending on complexity and iterations

Check current pricing:
- [OpenAI Pricing](https://openai.com/pricing)
- [Anthropic Pricing](https://www.anthropic.com/pricing)

## 🛠️ Troubleshooting

### API Key Errors
```
ValueError: [OPENAI/ANTHROPIC]_API_KEY not found
```
**Solution**: Check your `.env` file has the correct API key

### Rate Limiting
**Solution**: Add delays between requests or reduce batch size

### SVG Rendering Errors
**Solution**: Check generated SVG for XML issues. Error files are saved for debugging.

##  Dependencies

Each version has its own `requirements.txt` file:

### OpenAI Version (`GPT code/requirements.txt`):
```txt
openai>=1.0.0
python-dotenv>=1.0.0
cairosvg>=2.7.0
Pillow>=10.0.0
```

### Anthropic Version (`Claude code/requirements.txt`):
```txt
anthropic>=0.18.0
python-dotenv>=1.0.0
cairosvg>=2.7.0
Pillow>=10.0.0
```

### Common Dependencies (both versions):
- `python-dotenv`: Environment variable management
- `cairosvg`: SVG to PNG rendering
- `Pillow`: Image processing

### Version-Specific Dependencies:
- **OpenAI version**: `openai` - OpenAI API client
- **Anthropic version**: `anthropic` - Anthropic Claude API client

Install dependencies by navigating to your chosen folder and running:
```bash
cd "GPT code"  # or "Claude code"
pip install -r requirements.txt
```

## Security

- ✅ API keys in `.env` (gitignored)
- ✅ Never commit `.env` file
- ✅ Use `.env.example` as template
- ✅ Environment variables in production

## Acknowledgments

This project leverages:
- OpenAI's GPT models
- Anthropic's Claude AI models

Both implementations benefit from cutting-edge AI vision and generation capabilities.
