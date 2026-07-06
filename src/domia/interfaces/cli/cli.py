from __future__ import annotations

from domia.domain.services.knowledge_graph import KnowledgeGraph


class DomIACLI:
    """
    Command Line Interface de DomIA.

    Esta clase será el punto de entrada para interactuar con
    el Cognitive Operating System desde la terminal.
    """

    VERSION = "0.1.0"

    def __init__(self) -> None:
        self.graph = KnowledgeGraph()

    def status(self) -> None:
        """
        Muestra el estado actual del sistema.
        """
        print("=" * 40)
        print("DomIA Cognitive Operating System")
        print(f"Version   : {self.VERSION}")
        print(f"Nodes     : {self.graph.node_count()}")
        print(f"Relations : {self.graph.relationship_count()}")
        print("Status    : READY")
        print("=" * 40)