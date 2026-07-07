from domia.bootstrap.ai_foundation import load_ai_foundation
from domia.domain.services.knowledge_graph import KnowledgeGraph


def test_load_ai_foundation():

    graph = KnowledgeGraph()

    load_ai_foundation(graph)

    assert graph.node_count() == 11

    assert graph.relationship_count() == 10