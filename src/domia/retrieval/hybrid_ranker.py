class HybridRanker:
    """
    Combina la puntuación obtenida mediante
    búsqueda por palabras clave y búsqueda
    semántica.

    Esta primera versión utiliza una suma
    ponderada simple.

    score =
        keyword_weight * keyword_score +
        semantic_weight * semantic_score
    """

    def __init__(
        self,
        keyword_weight: float = 0.5,
        semantic_weight: float = 0.5,
    ) -> None:

        self.keyword_weight = keyword_weight
        self.semantic_weight = semantic_weight

    def score(
        self,
        keyword_score: float,
        semantic_score: float,
    ) -> float:
        """
        Calcula la puntuación híbrida.
        """

        return (
            keyword_score * self.keyword_weight
            + semantic_score * self.semantic_weight
        )