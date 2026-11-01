# Waguri Framework

**Local-First Multimodal AI Reliability & Response Validation Framework**

Waguri Framework is an experimental, modular Python framework designed to improve AI output reliability through evidence-based validation, response evaluation, and multimodal output checking.

It aims to provide a validation layer between AI models and applications, helping developers identify unsupported claims, evaluate generated responses, and assess AI-generated images.

Waguri follows a **local-first architecture**, prioritizing local model execution and privacy-conscious processing while maintaining extensibility for different model providers.

> Waguri does not guarantee hallucination-free AI outputs. It provides tools to evaluate, validate, and identify potential reliability issues in AI-generated content.

---

## Core Capabilities

### Text Reliability

Tools for evaluating and validating AI-generated text.

- Evidence-aware response validation.
- Claim extraction and checking.
- Unsupported claim identification.
- Uncertainty handling.
- Response quality evaluation.

### Image Reliability

Planned multimodal capabilities for evaluating AI-generated images.

- Image integrity and technical quality checks.
- Prompt-to-image compliance evaluation.
- Visual consistency assessment.
- Visual artifact screening.
- Image safety evaluation.

### Model Integration

A modular adapter architecture designed to support different AI model runtimes.

- Local model integration.
- Cloud model adapter extensibility.
- Ollama integration for local inference.
- Pluggable model interfaces.

### Optimization Utilities

Utilities designed to improve AI application efficiency.

- Context window fitting.
- Token estimation.
- Response caching.
- Configurable processing workflows.

---

## Architecture

Waguri is designed around independent validation components that can be integrated into different AI applications.

```text
AI Application
      |
      v
Waguri Framework
      |
      +----------------------+
      |                      |
      v                      v
Text Reliability      Image Reliability
      |                      |
      v                      v
Evidence Checking     Image Validation
Claim Validation      Visual Analysis
Response Evaluation   Prompt Compliance
      |                      |
      +----------+-----------+
                 |
                 v
       Reliability Evaluation
                 |
                 v
          Validation Result
```

The architecture separates model inference from validation logic, allowing developers to integrate different models without coupling their applications to a specific provider.

---

## Project Structure

```text
waguri-framework/
│
├── src/
│   └── waguri/
│       ├── adapters/
│       ├── validation/
│       ├── optimization/
│       ├── evaluation/
│       └── ...
│
├── tests/
├── examples/
├── README.md
├── LICENSE
└── pyproject.toml
```

The project structure may evolve as new validation modules and multimodal capabilities are introduced.

---

## Requirements

- Python 3.11 or newer.
- pip.
- Git.

Additional dependencies may be required depending on the selected model adapter and optional validation features.

---

## Installation

### Install from GitHub

Waguri can be installed directly from its public GitHub repository:

```bash
pip install git+https://github.com/RaihanFradita/waguri-framework.git
```

### Install for Local Development

Clone the repository:

```bash
git clone https://github.com/RaihanFradita/waguri-framework.git

cd waguri-framework
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install in editable mode:

```bash
pip install -e .
```

---

## Development

Install development dependencies:

```bash
pip install -e ".[dev]"
```

Run tests:

```bash
python -m pytest -v
```

---

## Development Roadmap

Waguri is under active development.

| Component | Status |
|---|---|
| Modular Python architecture | In development |
| Model adapter interfaces | In development |
| Evidence-aware validation | Experimental |
| Claim extraction and checking | Experimental |
| Context optimization | In development |
| Token estimation | In development |
| Response caching | In development |
| Text quality evaluation | Planned |
| Image quality validation | Planned |
| Prompt-to-image compliance | Planned |
| Visual consistency evaluation | Planned |
| Local vision model integration | Planned |
| Multimodal reliability scoring | Planned |

Features are subject to change as the framework evolves.

---

## Design Principles

Waguri is developed around the following principles:

- **Reliability First:** Prioritize validation and evaluation over blindly trusting model outputs.
- **Local-First:** Prefer local execution where practical.
- **Modular Architecture:** Keep validation, optimization, and model adapters independent.
- **Provider Independence:** Avoid unnecessary coupling to a single AI provider.
- **Transparency:** Make validation results, uncertainty, and limitations explicit.
- **Extensibility:** Allow developers to integrate Waguri into different AI applications.

---

## Intended Use Cases

Waguri is designed to serve as a reliability layer for:

- AI assistants and chatbots.
- Retrieval-Augmented Generation (RAG) applications.
- Local LLM applications.
- AI-powered business systems.
- AI image generation applications.
- Multimodal AI workflows.

---

## Limitations

Waguri is an experimental framework.

Its validation mechanisms have limitations and may produce false positives or false negatives. Evidence matching does not necessarily establish semantic correctness, and visual evaluation depends on the capabilities of the selected vision model.

Developers should independently evaluate results before using them in critical applications.

---

## License

This project is licensed under the **Apache License 2.0**.

See [LICENSE](LICENSE) for details.

---

## Contributing

Contributions, bug reports, and feature suggestions are welcome.

Please open an issue before submitting major architectural changes.

---

**Waguri Framework**  
*Building more reliable AI systems, one validation layer at a time.*

GitHub: https://github.com/RaihanFradita/waguri-framework
