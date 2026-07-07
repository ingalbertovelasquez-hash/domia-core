from dataclasses import dataclass, field


@dataclass(frozen=True)
class ReasoningResult:
    """
    Resultado producido por el Reasoning Engine.

    Describe cómo DomIA debe abordar un problema,
    sin ejecutar todavía el razonamiento.
    """

    strategy: str

    confidence: float

    requires_memory: bool

    requires_knowledge: bool

    requires_verification: bool

    notes: list[str] = field(default_factory=list)