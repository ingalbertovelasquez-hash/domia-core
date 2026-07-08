from domia.domain.services.knowledge_graph import KnowledgeGraph
from domia.retrieval.retrieval_result import RetrievalResult
from domia.vectorstore.vector_document import VectorDocument


class KeywordRetriever:
    """
    Recuperador basado en palabras clave.

    Busca coincidencias simples dentro del
    Knowledge Graph y devuelve resultados
    ordenados por puntuación.
    """

    def __init__(
        self,
        graph: KnowledgeGraph,
    ) -> None:

        self.graph = graph

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[RetrievalResult]:

        query_lower = query.lower()

        results: list[RetrievalResult] = []

        for node in self.graph.all_nodes():

            searchable = (
                f"{node.name} "
                f"{node.node_type} "
                f"{node.description}"
            ).lower()

            score = 0

            for token in query_lower.split():

                token = token.strip(".,!?()[]{}:;")

                if len(token) < 2:
                    continue

                if token in searchable:
                    score += 1

            if score == 0:
                continue

            document = VectorDocument(
                id=node.id,
                text=node.name,
                embedding=[],
            )

            results.append(
                RetrievalResult(
                    document=document,
                    score=float(score),
                )
            )

        results.sort(
            key=lambda result: result.score,
            reverse=True,
        )

        return results[:top_k]