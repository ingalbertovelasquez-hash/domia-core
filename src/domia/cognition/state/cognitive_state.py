from dataclasses import dataclass
from typing import Optional

from domia.cognition.contracts.context import Context
from domia.cognition.contracts.intent import Intent
from domia.cognition.contracts.objective import Objective
from domia.cognition.decision_engine.decision import Decision
from domia.cognition.planner.plan import Plan


@dataclass
class CognitiveState:
    """
    Estado cognitivo compartido durante la ejecución
    de un pipeline de DomIA.
    """

    objective: Objective

    intent: Optional[Intent] = None

    plan: Optional[Plan] = None

    decision: Optional[Decision] = None

    context: Optional[Context] = None

    status: str = "INITIALIZED"