from domia.cognition.contracts.objective import Objective

from domia.reasoning.reasoning_engine import ReasoningEngine
from domia.reasoning.strategy import Strategy


def test_reasoning_engine():

    engine = ReasoningEngine()

    objective = Objective(
        text="Crear un curso de IA"
    )

    result = engine.analyze(objective)

    assert result.strategy is Strategy.PLAN

    assert len(result.goals) == 3

    assert len(result.plan.steps) == 6

    assert result.requires_memory is True

    assert result.requires_knowledge is True

    assert result.confidence > 0.8