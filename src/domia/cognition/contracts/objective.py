from dataclasses import dataclass


@dataclass(frozen=True)
class Objective:
    """
    Representa el objetivo que el usuario desea alcanzar.
    """

    text: str