from dataclasses import dataclass, field

from domia.cognition.planner.plan import Plan
from domia.reasoning.goal import Goal
from domia.reasoning.strategy import Strategy


@dataclass(frozen=True)
class ReasoningResult:
    """
    Resultado producido por el Reasoning Engine.

    Describe cómo DomIA debe abordar un problema.
    """

    strategy: Strategy

    goals: list[Goal]

    plan: Plan

    confidence: float

    requires_memory: bool

    requires_knowledge: bool

    requires_verification: bool

    notes: list[str] = field(default_factory=list)