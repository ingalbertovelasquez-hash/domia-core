from domia.cognition.contracts.objective import Objective

from domia.reasoning.reasoning_result import ReasoningResult


class ReasoningEngine:
    """
    Primer motor de razonamiento de DomIA.

    En esta versión únicamente decide la estrategia
    cognitiva adecuada para resolver un objetivo.
    """

    def analyze(self, objective: Objective) -> ReasoningResult:

        text = objective.text.lower()

        strategy = "DIRECT"

        confidence = 0.90

        requires_memory = True

        requires_knowledge = False

        requires_verification = False

        notes = []

        if any(
            keyword in text
            for keyword in [
                "create",
                "design",
                "build",
                "develop",
                "curso",
                "crear",
                "diseñar",
            ]
        ):
            strategy = "PLAN"

            requires_knowledge = True

            notes.append(
                "Planning strategy selected."
            )

        return ReasoningResult(
            strategy=strategy,
            confidence=confidence,
            requires_memory=requires_memory,
            requires_knowledge=requires_knowledge,
            requires_verification=requires_verification,
            notes=notes,
        )