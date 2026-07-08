from domia.embeddings.embedding_provider import EmbeddingProvider


class MockEmbeddingProvider(EmbeddingProvider):
    """
    Implementación simulada.

    Produce vectores determinísticos para pruebas.
    """

    VECTOR_SIZE = 8

    def embed(self, text: str) -> list[float]:

        vector = [0.0] * self.VECTOR_SIZE

        for i, character in enumerate(text.lower()):

            index = i % self.VECTOR_SIZE

            vector[index] += ord(character) / 1000

        return vector