import requests

from domia.inference.provider import Provider


class OllamaProvider(Provider):
    """
    Proveedor para modelos locales
    ejecutados mediante Ollama.
    """

    def __init__(
        self,
        model: str = "qwen2.5:7b",
        host: str = "http://localhost:11434",
    ) -> None:

        self.model = model
        self.host = host

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = requests.post(
            f"{self.host}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            },
            timeout=300,
        )

        response.raise_for_status()

        payload = response.json()

        return payload["response"]