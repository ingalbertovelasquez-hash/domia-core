from dataclasses import dataclass, field


@dataclass(frozen=True)
class Goal:
    """
    Representa un subobjetivo generado
    por el Goal Decomposer.
    """

    description: str

    priority: int

    dependencies: list[str] = field(default_factory=list)