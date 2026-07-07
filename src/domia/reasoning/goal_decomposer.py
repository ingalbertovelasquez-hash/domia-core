from domia.cognition.contracts.objective import Objective

from domia.reasoning.goal import Goal


class GoalDecomposer:
    """
    Divide un objetivo complejo en
    una lista de subobjetivos.
    """

    def decompose(self, objective: Objective) -> list[Goal]:

        text = objective.text.lower()

        goals: list[Goal] = []

        if any(
            keyword in text
            for keyword in [
                "crear",
                "create",
                "diseñar",
                "design",
                "curso",
                "academy",
                "academia",
            ]
        ):

            goals.extend(
                [
                    Goal(
                        description="Analyze requirements",
                        priority=1,
                    ),
                    Goal(
                        description="Design solution",
                        priority=2,
                    ),
                    Goal(
                        description="Create implementation plan",
                        priority=3,
                    ),
                ]
            )

        else:

            goals.append(
                Goal(
                    description="Solve objective",
                    priority=1,
                )
            )

        return goals