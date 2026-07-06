from dataclasses import dataclass, field


@dataclass
class Decision:
    """
    Resultado producido por el Decision Engine.
    """

    objective: str

    recommended_nodes: list[str] = field(default_factory=list)

    reasoning: str = ""

    recommended_engine: str = "None"