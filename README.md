# Waguri Framework
AI Reliability and Response Validation Framework.

Waguri Framework is an experimental Python framework designed to improve
AI response reliability through evidence validation, output checking,
and controlled response generation.

## Features

- Modular architecture
- Local and cloud model adapter support
- Evidence-aware response validation (in development)
- Response quality evaluation (planned)
- Context and token-budget optimization utilities

## Project structure

- `src/waguri/adapters/`: model adapter protocol and implementations
- `src/waguri/validation/`: claim splitting and evidence checks
- `src/waguri/optimization/`: context fitting, token estimation, and response cache
- `src/waguri/evaluation/`: benchmark result types and exact-match evaluation
- `tests/`: unit tests
- `examples/`: runnable usage examples

## Requirements

- Python 3.11 or newer

## Development Status

Waguri Framework is under active development. Its validation mechanisms
are experimental and do not guarantee hallucination-free responses.

## License

Apache-2.0