from domia.cognition.context_builder import ContextBuilder
from domia.domain.entities.knowledge_node import KnowledgeNode
from domia.domain.entities.knowledge_relationship import (
    KnowledgeRelationship,
)
from domia.domain.enums.relationship_type import RelationshipType
from domia.domain.services.knowledge_graph import KnowledgeGraph


def test_build_context():

    graph = KnowledgeGraph()

    customer = KnowledgeNode(
        name="Customer",
        node_type="Person",
    )

    project = KnowledgeNode(
        name="DomIA",
        node_type="Project",
    )

    graph.add_node(customer)
    graph.add_node(project)

    graph.add_relationship(
        KnowledgeRelationship(
            source_id=customer.id,
            target_id=project.id,
            relationship_type=RelationshipType.CONTAINS,
        )
    )

    builder = ContextBuilder(graph)

    context = builder.build(customer.id)

    assert len(context) == 2