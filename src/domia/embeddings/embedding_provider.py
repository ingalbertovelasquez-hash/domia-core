from abc import ABC, abstractmethod


class EmbeddingProvider(ABC):
    """
    Contrato para todos los proveedores
    de embeddings.
    """

    @abstractmethod
    def embed(self, text: str) -> list[float]:
        """
        Genera un vector para un texto.
        """
        raise NotImplementedError