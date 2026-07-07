from domia.inference.provider import Provider
from domia.inference.provider_factory import ProviderFactory


class InferenceEngine:
    """
    Motor de inferencia.

    Delega la generación de respuestas
    al proveedor configurado.
    """

    def __init__(
        self,
        provider: Provider | None = None,
    ):

        self.provider = (
            provider
            if provider is not None
            else ProviderFactory.create()
        )

    def generate(self, prompt: str) -> str:

        return self.provider.generate(prompt)