from domia.cognition.decision_engine.decision import Decision
from domia.domain.services.knowledge_graph import KnowledgeGraph


class DecisionEngine:
    """
    Decision Engine v1.

    Selecciona conocimiento relevante utilizando
    una coincidencia simple de palabras clave.
    """

    def __init__(self, graph: KnowledgeGraph):
        self.graph = graph

    def decide(self, objective: str) -> Decision:

        objective_lower = objective.lower()

        recommended = []

        for node in self.graph.all_nodes():

            searchable = (
                f"{node.name} "
                f"{node.node_type} "
                f"{node.description}"
            ).lower()

            score = 0

            for word in objective_lower.split():

                if word in searchable:
                    score += 1

            if score > 0:
                recommended.append((score, node.name))

        recommended.sort(reverse=True)

        result = [
            node_name
            for _, node_name in recommended
        ]

        return Decision(
            objective=objective,
            recommended_nodes=result,
            reasoning="Knowledge ranked by keyword relevance.",
            recommended_engine="Pending",
        )