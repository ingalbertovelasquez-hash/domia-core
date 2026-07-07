from domia.cognition.contracts.objective import Objective

from domia.reasoning.goal_decomposer import GoalDecomposer


def test_goal_decomposer():

    decomposer = GoalDecomposer()

    objective = Objective(
        text="Crear un curso de IA"
    )

    goals = decomposer.decompose(objective)

    assert len(goals) == 3

    assert goals[0].priority == 1

    assert goals[0].description == "Analyze requirements"

    assert goals[-1].priority == 3