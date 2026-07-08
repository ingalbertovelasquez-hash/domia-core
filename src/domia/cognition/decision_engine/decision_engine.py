from domia.cognition.decision_engine.decision import Decision
from domia.domain.services.knowledge_graph import KnowledgeGraph
from domia.embeddings.embedding_engine import EmbeddingEngine
from domia.embeddings.mock_embedding_provider import (
    MockEmbeddingProvider,
)


class DecisionEngine:
    """
    Decision Engine v3.

    Selecciona conocimiento utilizando
    ranking por palabras clave y prepara
    la integración con búsqueda semántica.
    """

    DEFAULT_TOP_K = 5

    def __init__(self, graph: KnowledgeGraph):

        self.graph = graph

        self.embedding_engine = EmbeddingEngine(
            MockEmbeddingProvider()
        )

    def decide(
        self,
        objective: str,
        top_k: int | None = None,
    ) -> Decision:

        if top_k is None:
            top_k = self.DEFAULT_TOP_K

        # --------------------------------------------------
        # Generación del embedding de la consulta
        # (todavía no se utiliza para el ranking)
        # --------------------------------------------------

        query_embedding = self.embedding_engine.embed(
            objective
        )

        # Evita advertencias de variable no utilizada.
        _ = query_embedding

        objective_lower = objective.lower()

        ranking: list[tuple[int, str]] = []

        for node in self.graph.all_nodes():

            searchable = (
                f"{node.name} "
                f"{node.node_type} "
                f"{node.description}"
            ).lower()

            score = 0

            for word in objective_lower.split():

                token = word.strip(".,!?()[]{}:;")

                if len(token) < 2:
                    continue

                if token in searchable:
                    score += 1

            if score > 0:
                ranking.append(
                    (
                        score,
                        node.name,
                    )
                )

        ranking.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        recommended = [
            node
            for _, node in ranking[:top_k]
        ]

        return Decision(
            objective=objective,
            recommended_nodes=recommended,
            reasoning=(
                f"Top-{top_k} knowledge ranked by "
                "keyword relevance. "
                "Semantic embedding generated."
            ),
            recommended_engine="Decision Engine v3",
        )