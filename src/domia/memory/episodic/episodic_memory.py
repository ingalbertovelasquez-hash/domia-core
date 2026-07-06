from dataclasses import dataclass
from datetime import datetime


@dataclass
class Episode:
    timestamp: datetime
    description: str


class EpisodicMemory:
    """
    Memoria episódica.

    Almacena eventos ocurridos durante la vida del sistema.
    """

    def __init__(self):
        self._episodes: list[Episode] = []

    def remember(self, description: str) -> None:
        self._episodes.append(
            Episode(
                timestamp=datetime.now(),
                description=description,
            )
        )

    def recall(self) -> list[Episode]:
        return list(self._episodes)

    def clear(self) -> None:
        self._episodes.clear()

    def size(self) -> int:
        return len(self._episodes)