from domia.inference.mock_provider import MockProvider
from domia.inference.openai_provider import OpenAIProvider
from domia.inference.provider import Provider


class ProviderFactory:
    """
    Fábrica de proveedores de inferencia.

    Centraliza la creación de proveedores
    soportados por DomIA.
    """

    @staticmethod
    def create(name: str = "mock") -> Provider:

        provider = name.lower()

        if provider == "mock":
            return MockProvider()

        if provider == "openai":
            return OpenAIProvider()

        raise ValueError(
            f"Unknown provider: {name}"
        )