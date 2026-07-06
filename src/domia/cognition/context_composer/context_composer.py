from domia.cognition.contracts.context import Context
from domia.cognition.contracts.intent import Intent
from domia.cognition.decision_engine.decision import Decision
from domia.cognition.planner.plan import Plan


class ContextComposer:
    """
    Construye un contexto cognitivo unificado a partir
    de los componentes generados por el Cognitive Core.
    """

    def compose(
        self,
        objective: str,
        intent: Intent,
        plan: Plan,
        decision: Decision,
    ) -> Context:

        notes = [
            f"Domain: {intent.domain}",
            f"Confidence: {intent.confidence:.2f}",
        ]

        return Context(
            objective=objective,
            intent=intent.action,
            plan=list(plan.steps),
            knowledge=list(decision.recommended_nodes),
            notes=notes,
        )