from dataclasses import dataclass, field


@dataclass(frozen=True)
class Policy:
    """
    Política de ejecución de DomIA.

    Define qué capacidades deben ejecutarse
    para resolver una intención.
    """

    use_memory: bool

    use_knowledge_graph: bool

    build_context: bool

    build_prompt: bool

    execute_model: bool

    capabilities: list[str] = field(default_factory=list)