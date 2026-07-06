from typing import Any


class SemanticMemory:
    """
    Memoria semántica de DomIA.

    Almacena conocimiento persistente
    mediante pares clave-valor.
    """

    def __init__(self):
        self._knowledge: dict[str, Any] = {}

    def store(self, key: str, value: Any) -> None:
        self._knowledge[key] = value

    def recall(self, key: str):
        return self._knowledge.get(key)

    def contains(self, key: str) -> bool:
        return key in self._knowledge

    def remove(self, key: str) -> None:
        self._knowledge.pop(key, None)

    def clear(self) -> None:
        self._knowledge.clear()

    def size(self) -> int:
        return len(self._knowledge)

    def all(self) -> dict[str, Any]:
        return dict(self._knowledge)