from math import sqrt

from domia.vectorstore.vector_document import VectorDocument


class VectorStore:
    """
    Vector Store en memoria.

    Implementación sencilla para pruebas
    y primeras búsquedas semánticas.
    """

    def __init__(self):

        self._documents: list[VectorDocument] = []

    def add(
        self,
        document: VectorDocument,
    ) -> None:

        self._documents.append(document)

    def count(self) -> int:

        return len(self._documents)

    def similarity_search(
        self,
        embedding: list[float],
        top_k: int = 5,
    ) -> list[VectorDocument]:

        scored: list[tuple[float, VectorDocument]] = []

        for document in self._documents:

            similarity = self._cosine_similarity(
                embedding,
                document.embedding,
            )

            scored.append(
                (
                    similarity,
                    document,
                )
            )

        scored.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        return [
            document
            for _, document in scored[:top_k]
        ]

    def _cosine_similarity(
        self,
        a: list[float],
        b: list[float],
    ) -> float:
        """
        Calcula la similitud coseno entre dos vectores.
        """

        if len(a) != len(b):
            raise ValueError(
                "Vectors must have the same dimension."
            )

        dot = sum(x * y for x, y in zip(a, b))

        norm_a = sqrt(sum(x * x for x in a))

        norm_b = sqrt(sum(y * y for y in b))

        if norm_a == 0 or norm_b == 0:
            return 0.0

        return dot / (norm_a * norm_b)