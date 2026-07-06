from domia.bootstrap.foundation import load_foundation_graph
from domia.cognition.contracts.objective import Objective
from domia.cognition.intent_analyzer.intent_analyzer import IntentAnalyzer
from domia.cognition.planner.planner import Planner
from domia.cognition.decision_engine.decision_engine import DecisionEngine
from domia.memory.memory_manager import MemoryManager


class AskPipeline:
    """
    Primer pipeline cognitivo de DomIA.

    Orquesta los componentes principales del núcleo cognitivo.
    """

    def __init__(self):

        self.graph = load_foundation_graph()

        self.memory = MemoryManager()

        self.intent_analyzer = IntentAnalyzer()

        self.planner = Planner()

        self.decision_engine = DecisionEngine(self.graph)

    def run(self, text: str) -> dict:

        objective = Objective(text=text)

        intent = self.intent_analyzer.analyze(objective)

        plan = self.planner.create_plan(intent)

        decision = self.decision_engine.decide(intent.subject)

        self.memory.working.put("objective", objective.text)
        self.memory.working.put("intent", intent)
        self.memory.working.put("plan", plan)
        self.memory.working.put("decision", decision)

        return {
            "objective": objective.text,
            "intent": intent,
            "plan": plan,
            "decision": decision,
            "status": "READY",
        }