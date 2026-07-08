from domia.config.settings import Settings
from domia.inference.mock_provider import MockProvider
from domia.inference.ollama_provider import OllamaProvider
from domia.inference.openai_provider import OpenAIProvider
from domia.inference.provider import Provider


class ProviderFactory:
    """
    Fábrica de proveedores de inferencia.

    Centraliza la creación de proveedores
    soportados por DomIA.
    """

    @staticmethod
    def create(
        name: str | None = None,
    ) -> Provider:

        settings = Settings.load()

        provider = (
            name or settings.provider
        ).lower()

        if provider == "mock":
            return MockProvider()

        if provider == "openai":
            return OpenAIProvider()

        if provider == "ollama":
            return OllamaProvider()

        raise ValueError(
            f"Unknown provider: {provider}"
        )