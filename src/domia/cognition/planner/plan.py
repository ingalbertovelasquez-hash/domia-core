from dataclasses import dataclass, field


@dataclass(frozen=True)
class Plan:
    """
    Plan de ejecución generado por DomIA.
    """

    objective: str

    steps: list[str] = field(default_factory=list)

    estimated_engine: str = "pending"