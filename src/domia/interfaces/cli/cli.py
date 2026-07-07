from __future__ import annotations

import os

from domia.application.pipelines.ask_pipeline import AskPipeline
from domia.domain.services.knowledge_graph import KnowledgeGraph


class DomIACLI:
    """
    Command Line Interface de DomIA.

    Punto de entrada para interactuar con
    el Cognitive Operating System desde la terminal.
    """

    VERSION = "0.6.0"

    def __init__(self) -> None:

        self.graph = KnowledgeGraph()

        self.ask_pipeline = AskPipeline()

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

    def ask(self, text: str) -> None:
        """
        Ejecuta el ciclo cognitivo completo
        y presenta el resultado.
        """

        result = self.ask_pipeline.run(text)

        provider = os.getenv("DOMIA_PROVIDER", "mock")

        print("=" * 60)
        print("DomIA Cognitive Operating System")
        print("=" * 60)

        print("\nQuestion")
        print("-" * 60)
        print(result["objective"])

        print("\nIntent")
        print("-" * 60)
        print(result["intent"].action)

        print("\nExecution Plan")
        print("-" * 60)

        for step in result["plan"].steps:
            print(f" • {step}")

        print("\nKnowledge")
        print("-" * 60)

        for node in result["decision"].recommended_nodes:
            print(f" • {node}")

        print("\nResponse")
        print("-" * 60)
        print(result["response"])

        print("\nPrompt")
        print("-" * 60)
        print(result["prompt"])

        print("\nProvider")
        print("-" * 60)
        print(provider)

        print("\nStatus")
        print("-" * 60)
        print(result["status"])

        print("=" * 60)