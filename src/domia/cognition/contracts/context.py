from dataclasses import dataclass, field


@dataclass(frozen=True)
class Context:
    """
    Contexto estructurado que será enviado al Prompt Builder.
    """

    objective: str

    knowledge: list[str] = field(default_factory=list)

    metadata: dict = field(default_factory=dict)