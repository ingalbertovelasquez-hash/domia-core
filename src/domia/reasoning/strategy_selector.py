from domia.cognition.contracts.objective import Objective

from domia.reasoning.strategy import Strategy


class StrategySelector:
    """
    Selecciona la estrategia cognitiva
    más adecuada para un objetivo.
    """

    def select(self, objective: Objective) -> Strategy:

        text = objective.text.lower()

        if any(
            keyword in text
            for keyword in [
                "crear",
                "create",
                "build",
                "design",
                "diseñar",
                "curso",
                "academy",
                "academia",
            ]
        ):
            return Strategy.PLAN

        if any(
            keyword in text
            for keyword in [
                "compare",
                "comparar",
                "difference",
                "vs",
            ]
        ):
            return Strategy.ANALYZE

        if any(
            keyword in text
            for keyword in [
                "architecture",
                "arquitectura",
                "system",
                "sistema",
            ]
        ):
            return Strategy.DESIGN

        if any(
            keyword in text
            for keyword in [
                "calculate",
                "resolver",
                "solve",
                "equation",
            ]
        ):
            return Strategy.DEDUCE

        return Strategy.DIRECT