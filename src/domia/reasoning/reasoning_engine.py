from domia.cognition.contracts.objective import Objective
from domia.cognition.intent_analyzer.intent_analyzer import IntentAnalyzer
from domia.cognition.planner.planner import Planner

from domia.reasoning.goal_decomposer import GoalDecomposer
from domia.reasoning.reasoning_result import ReasoningResult
from domia.reasoning.strategy import Strategy
from domia.reasoning.strategy_selector import StrategySelector


class ReasoningEngine:
    """
    Orquestador del razonamiento de DomIA.
    """

    def __init__(self):

        self.strategy_selector = StrategySelector()

        self.goal_decomposer = GoalDecomposer()

        self.intent_analyzer = IntentAnalyzer()

        self.planner = Planner()

    def analyze(self, objective: Objective) -> ReasoningResult:

        strategy = self.strategy_selector.select(objective)

        goals = self.goal_decomposer.decompose(objective)

        intent = self.intent_analyzer.analyze(objective)

        plan = self.planner.create_plan(intent)

        confidence = 0.90

        requires_memory = True

        requires_knowledge = strategy is Strategy.PLAN

        requires_verification = False

        notes = [
            f"Strategy: {strategy.value}",
            f"Goals: {len(goals)}",
            f"Plan steps: {len(plan.steps)}",
        ]

        return ReasoningResult(
            strategy=strategy,
            goals=goals,
            plan=plan,
            confidence=confidence,
            requires_memory=requires_memory,
            requires_knowledge=requires_knowledge,
            requires_verification=requires_verification,
            notes=notes,
        )