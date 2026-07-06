from domia.cognition.contracts.objective import Objective
from domia.cognition.state.cognitive_state import CognitiveState


def test_create_cognitive_state():

    objective = Objective(
        text="Crear un curso de IA"
    )

    state = CognitiveState(
        objective=objective
    )

    assert state.objective.text == "Crear un curso de IA"

    assert state.intent is None

    assert state.plan is None

    assert state.decision is None

    assert state.context is None

    assert state.status == "INITIALIZED"