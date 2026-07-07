from domia.application.pipelines.inference_pipeline import (
    InferencePipeline,
)
from domia.bootstrap.foundation import load_foundation_graph
from domia.cognition.context_composer.context_composer import (
    ContextComposer,
)
from domia.cognition.contracts.objective import Objective
from domia.cognition.decision_engine.decision_engine import (
    DecisionEngine,
)
from domia.cognition.intent_analyzer.intent_analyzer import (
    IntentAnalyzer,
)
from domia.cognition.planner.planner import Planner
from domia.memory.memory_manager import MemoryManager


class AskPipeline:
    """
    Pipeline cognitivo principal de DomIA.

    Ejecuta el ciclo cognitivo completo.
    """

    def __init__(self):

        self.graph = load_foundation_graph()

        self.memory = MemoryManager()

        self.intent_analyzer = IntentAnalyzer()

        self.planner = Planner()

        self.decision_engine = DecisionEngine(self.graph)

        self.context_composer = ContextComposer()

        self.inference_pipeline = InferencePipeline()

    def run(self, text: str) -> dict:

        objective = Objective(text=text)

        intent = self.intent_analyzer.analyze(objective)

        plan = self.planner.create_plan(intent)

        decision = self.decision_engine.decide(intent.subject)

        context = self.context_composer.compose(
            objective=objective.text,
            intent=intent,
            plan=plan,
            decision=decision,
        )

        inference = self.inference_pipeline.run(
            context
        )

        self.memory.working.put(
            "objective",
            objective.text,
        )

        self.memory.working.put(
            "intent",
            intent,
        )

        self.memory.working.put(
            "plan",
            plan,
        )

        self.memory.working.put(
            "decision",
            decision,
        )

        self.memory.working.put(
            "context",
            context,
        )

        self.memory.working.put(
            "response",
            inference["response"],
        )

        return {
            "objective": objective.text,
            "intent": intent,
            "plan": plan,
            "decision": decision,
            "context": context,
            "prompt": inference["prompt"],
            "response": inference["response"],
            "status": "COMPLETED",
        }