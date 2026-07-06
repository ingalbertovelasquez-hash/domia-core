from domia.domain.entities.knowledge_node import KnowledgeNode


def test_create_knowledge_node():

    node = KnowledgeNode(
        name="Customer Acquisition",
        node_type="Process"
    )

    assert node.name == "Customer Acquisition"
    assert node.node_type == "Process"
    assert node.status == "active"
    assert node.description == ""