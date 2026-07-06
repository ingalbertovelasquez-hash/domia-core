from domia.cognition.context_builder import ContextBuilder
from domia.domain.services.knowledge_graph import KnowledgeGraph


class CognitiveEngine:
    """
    Core reasoning engine of DomIA.
    """

    def __init__(self, graph: KnowledgeGraph):
        self.graph = graph
        self.context_builder = ContextBuilder(graph)

    def build_prompt(self, node_id) -> str:
        context = self.context_builder.build(node_id)

        lines = [
            "You are the DomIA Cognitive Operating System.",
            "",
            "Use ONLY the following knowledge:",
            "",
        ]

        for node in context:
            lines.append(f"- {node.name} ({node.node_type})")

            if getattr(node, "description", ""):
                lines.append(f"  {node.description}")

        lines.append("")
        lines.append("Answer using only the available knowledge.")

        return "\n".join(lines)