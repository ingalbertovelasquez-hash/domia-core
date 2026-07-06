from dataclasses import dataclass, field


@dataclass(frozen=True)
class Intent:
    """
    Resultado del análisis de intención.
    """

    action: str

    domain: str

    subject: str

    confidence: float

    required_capabilities: list[str] = field(default_factory=list)