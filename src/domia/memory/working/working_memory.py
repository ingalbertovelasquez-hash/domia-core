from typing import Any


class WorkingMemory:
    """
    Memoria de trabajo.

    Almacena información temporal durante la ejecución
    de una tarea cognitiva.
    """

    def __init__(self):
        self._memory: dict[str, Any] = {}

    def put(self, key: str, value: Any) -> None:
        self._memory[key] = value

    def get(self, key: str):
        return self._memory.get(key)

    def remove(self, key: str) -> None:
        self._memory.pop(key, None)

    def clear(self) -> None:
        self._memory.clear()

    def size(self) -> int:
        return len(self._memory)

    def all(self) -> dict[str, Any]:
        return dict(self._memory)