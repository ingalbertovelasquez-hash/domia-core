from domia.cognition.contracts.intent import Intent
from domia.cognition.planner.plan import Plan


class Planner:
    """
    Planner v1.

    Convierte una intención en un plan de ejecución.
    """

    def create_plan(self, intent: Intent) -> Plan:

        steps = [
            "Analyze Intent",
            "Search Knowledge",
            "Build Context",
            "Build Prompt",
            "Execute Model",
            "Validate Response",
        ]

        return Plan(
            objective=intent.subject,
            steps=steps,
            estimated_engine="pending",
        )