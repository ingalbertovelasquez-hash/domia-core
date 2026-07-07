from domia.bootstrap.ai_foundation import load_ai_foundation
from domia.domain.entities.knowledge_node import KnowledgeNode
from domia.domain.entities.knowledge_relationship import (
    KnowledgeRelationship,
)
from domia.domain.enums.relationship_type import RelationshipType
from domia.domain.services.knowledge_graph import KnowledgeGraph


def load_foundation_graph() -> KnowledgeGraph:
    """
    Carga el Knowledge Graph fundacional de DomIA.

    Este grafo está compuesto por:

    - Foundation (identidad de DomIA)
    - AI Foundation (conocimiento de IA)
    """

    graph = KnowledgeGraph()

    # =====================================================
    # DomIA Foundation
    # =====================================================

    founder = KnowledgeNode(
        name="Albert D. Velásquez",
        node_type="Person",
        description="Founder and Chief Visionary of DomIA.",
    )

    domia = KnowledgeNode(
        name="DomIA",
        node_type="Project",
        description="Universal Cognitive Operating System.",
    )

    kairos = KnowledgeNode(
        name="Kairos GPT",
        node_type="Agent",
        description="Chief AI Architect.",
    )

    pecra = KnowledgeNode(
        name="PECRA",
        node_type="Framework",
        description="Prompt Engineering Framework.",
    )

    cos = KnowledgeNode(
        name="Cognitive Operating System",
        node_type="Concept",
        description="Operating System for Intelligence.",
    )

    nodes = [
        founder,
        domia,
        kairos,
        pecra,
        cos,
    ]

    for node in nodes:
        graph.add_node(node)

    relationships = [

        KnowledgeRelationship(
            source_id=founder.id,
            target_id=domia.id,
            relationship_type=RelationshipType.CONTAINS,
        ),

        KnowledgeRelationship(
            source_id=domia.id,
            target_id=kairos.id,
            relationship_type=RelationshipType.CONTAINS,
        ),

        KnowledgeRelationship(
            source_id=domia.id,
            target_id=pecra.id,
            relationship_type=RelationshipType.CONTAINS,
        ),

        KnowledgeRelationship(
            source_id=domia.id,
            target_id=cos.id,
            relationship_type=RelationshipType.CONTAINS,
        ),
    ]

    for relationship in relationships:
        graph.add_relationship(relationship)

    # =====================================================
    # Artificial Intelligence Foundation
    # =====================================================

    load_ai_foundation(graph)

    return graph