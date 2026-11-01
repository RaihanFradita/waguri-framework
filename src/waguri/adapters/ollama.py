from typing import Any


class OllamaAdapter:
    def __init__(
        self,
        model: str,
        base_url: str = "http://localhost:11434",
        timeout: float = 30.0,
    ) -> None:
        if not model.strip():
            raise ValueError("Model name must not be empty.")
        if timeout <= 0:
            raise ValueError("Timeout must be greater than zero.")

        self.model = model
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def check_connection(self) -> bool:
        try:
            import httpx
        except ImportError as error:
            raise RuntimeError(
                "Ollama support requires the optional 'httpx' dependency. "
                "Install it with: pip install waguri-framework[ollama]"
            ) from error

        try:
            response = httpx.get(
                f"{self.base_url}/api/tags",
                timeout=self.timeout,
            )
            response.raise_for_status()
            return True
        except httpx.HTTPError as error:
            raise RuntimeError(
                f"Unable to reach Ollama at '{self.base_url}'. "
                "Ensure the local Ollama server is running."
            ) from error

    def is_available(self) -> bool:
        try:
            self.check_connection()
            return True
        except RuntimeError:
            return False

    def generate(self, prompt: str) -> str:
        try:
            import httpx
        except ImportError as error:
            raise RuntimeError(
                "Ollama support requires the optional 'httpx' dependency. "
                "Install it with: pip install waguri-framework[ollama]"
            ) from error

        try:
            self.check_connection()
            response = httpx.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                },
                timeout=self.timeout,
            )
            response.raise_for_status()
        except httpx.HTTPError as error:
            raise RuntimeError(
                f"Model '{self.model}' is unavailable or Ollama is unreachable at '{self.base_url}'."
            ) from error

        payload: Any = response.json()
        generated = payload.get("response") if isinstance(payload, dict) else None
        if not isinstance(generated, str):
            raise TypeError("Ollama response must contain a string 'response' field.")
        return generated
