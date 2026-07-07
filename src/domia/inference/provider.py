from abc import ABC, abstractmethod


class Provider(ABC):
    """
    Contrato para todos los proveedores de inferencia.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Genera una respuesta a partir de un prompt.
        """
        raise NotImplementedError