from dataclasses import dataclass


@dataclass
class VectorDocument:
    """
    Documento almacenado dentro
    del Vector Store.
    """

    id: str

    text: str

    embedding: list[float]