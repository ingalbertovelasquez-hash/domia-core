from domia.domain.entities.knowledge_node import KnowledgeNode
from domia.domain.entities.knowledge_relationship import (
    KnowledgeRelationship,
)
from domia.domain.enums.relationship_type import RelationshipType
from domia.domain.services.knowledge_graph import KnowledgeGraph


def test_add_node():

    graph = KnowledgeGraph()

    node = KnowledgeNode(
        name="DomIA",
        node_type="Project",
    )

    graph.add_node(node)

    assert graph.get_node(node.id) == node


def test_get_neighbors():

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

    neighbors = graph.get_neighbors(customer.id)

    assert len(neighbors) == 1

    assert neighbors[0].name == "DomIA"