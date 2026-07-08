from domia.embeddings.embedding_provider import (
    EmbeddingProvider,
)


class EmbeddingEngine:
    """
    Motor de embeddings.

    Delega la generación de vectores
    al proveedor configurado.
    """

    def __init__(
        self,
        provider: EmbeddingProvider,
    ):

        self.provider = provider

    def embed(
        self,
        text: str,
    ) -> list[float]:

        return self.provider.embed(text)