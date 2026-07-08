from dataclasses import dataclass

from domia.vectorstore.vector_document import VectorDocument


@dataclass(frozen=True)
class RetrievalResult:
    """
    Resultado de una recuperación de conocimiento.

    Representa un documento junto con su
    puntuación de relevancia.
    """

    document: VectorDocument

    score: float