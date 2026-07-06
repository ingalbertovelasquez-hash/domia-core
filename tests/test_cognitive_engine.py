from domia.cognition.cognitive_engine import CognitiveEngine
from domia.domain.entities.knowledge_node import KnowledgeNode
from domia.domain.services.knowledge_graph import KnowledgeGraph


def test_build_prompt():

    graph = KnowledgeGraph()

    customer = KnowledgeNode(
        name="Albert D. Velásquez",
        node_type="Person",
        description="Founder of DomIA."
    )

    graph.add_node(customer)

    engine = CognitiveEngine(graph)

    prompt = engine.build_prompt(customer.id)

    assert "DomIA Cognitive Operating System" in prompt
    assert "Albert D. Velásquez" in prompt
    assert "Founder of DomIA." in prompt