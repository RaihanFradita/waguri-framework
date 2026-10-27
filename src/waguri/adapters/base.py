from typing import Protocol

class ModelAdapter(Protocol):

    def generate(self, prompt: str) -> str:
        """Generate a response from an AI model."""
        ...