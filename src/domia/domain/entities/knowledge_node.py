from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class KnowledgeNode:
    """
    Nodo base del Knowledge Graph de DomIA.
    """

    name: str
    node_type: str

    id: UUID = field(default_factory=uuid4)
    description: str = ""
    status: str = "active"