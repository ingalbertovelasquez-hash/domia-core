from dataclasses import dataclass, field


@dataclass
class Context:
    """
    Contexto cognitivo consolidado.

    Contiene toda la información necesaria para
    construir un prompt posteriormente.
    """

    objective: str

    intent: str

    plan: list[str] = field(default_factory=list)

    knowledge: list[str] = field(default_factory=list)

    notes: list[str] = field(default_factory=list)