from domia.cognition.contracts.objective import Objective

from domia.reasoning.strategy import Strategy
from domia.reasoning.strategy_selector import StrategySelector


def test_strategy_selector():

    selector = StrategySelector()

    objective = Objective(
        text="Crear un curso de IA"
    )

    strategy = selector.select(objective)

    assert strategy is Strategy.PLAN