from domia.domain.entities.knowledge_node import KnowledgeNode
from domia.domain.entities.knowledge_relationship import KnowledgeRelationship
from domia.domain.enums.relationship_type import RelationshipType
from domia.domain.services.knowledge_graph import KnowledgeGraph


def load_ai_foundation(graph: KnowledgeGraph) -> None:
    """
    Carga el conocimiento fundacional de Inteligencia Artificial.
    """

    ai = KnowledgeNode(
        name="Artificial Intelligence",
        node_type="Concept",
        description="Science of building intelligent systems.",
    )

    ml = KnowledgeNode(
        name="Machine Learning",
        node_type="Concept",
        description="Algorithms that learn from data.",
    )

    dl = KnowledgeNode(
        name="Deep Learning",
        node_type="Concept",
        description="Neural-network based machine learning.",
    )

    rl = KnowledgeNode(
        name="Reinforcement Learning",
        node_type="Concept",
        description="Learning through rewards and penalties.",
    )

    supervised = KnowledgeNode(
        name="Supervised Learning",
        node_type="Concept",
        description="Learning using labeled data.",
    )

    unsupervised = KnowledgeNode(
        name="Unsupervised Learning",
        node_type="Concept",
        description="Learning without labeled data.",
    )

    nn = KnowledgeNode(
        name="Neural Networks",
        node_type="Concept",
        description="Computational models inspired by the brain.",
    )

    llm = KnowledgeNode(
        name="Large Language Models",
        node_type="Concept",
        description="Foundation models trained on massive text corpora.",
    )

    rag = KnowledgeNode(
        name="Retrieval-Augmented Generation",
        node_type="Concept",
        description="Combines retrieval with language models.",
    )

    nlp = KnowledgeNode(
        name="Natural Language Processing",
        node_type="Concept",
        description="AI field focused on language understanding.",
    )

    cv = KnowledgeNode(
        name="Computer Vision",
        node_type="Concept",
        description="AI field focused on image understanding.",
    )

    nodes = [
        ai,
        ml,
        dl,
        rl,
        supervised,
        unsupervised,
        nn,
        llm,
        rag,
        nlp,
        cv,
    ]

    for node in nodes:
        graph.add_node(node)

    relationships = [

        KnowledgeRelationship(
            source_id=ai.id,
            target_id=ml.id,
            relationship_type=RelationshipType.CONTAINS,
        ),

        KnowledgeRelationship(
            source_id=ml.id,
            target_id=supervised.id,
            relationship_type=RelationshipType.CONTAINS,
        ),

        KnowledgeRelationship(
            source_id=ml.id,
            target_id=unsupervised.id,
            relationship_type=RelationshipType.CONTAINS,
        ),

        KnowledgeRelationship(
            source_id=ml.id,
            target_id=rl.id,
            relationship_type=RelationshipType.CONTAINS,
        ),

        KnowledgeRelationship(
            source_id=ml.id,
            target_id=dl.id,
            relationship_type=RelationshipType.CONTAINS,
        ),

        KnowledgeRelationship(
            source_id=dl.id,
            target_id=nn.id,
            relationship_type=RelationshipType.CONTAINS,
        ),

        KnowledgeRelationship(
            source_id=ai.id,
            target_id=nlp.id,
            relationship_type=RelationshipType.CONTAINS,
        ),

        KnowledgeRelationship(
            source_id=ai.id,
            target_id=cv.id,
            relationship_type=RelationshipType.CONTAINS,
        ),

        KnowledgeRelationship(
            source_id=ai.id,
            target_id=llm.id,
            relationship_type=RelationshipType.CONTAINS,
        ),

        KnowledgeRelationship(
            source_id=llm.id,
            target_id=rag.id,
            relationship_type=RelationshipType.CONTAINS,
        ),
    ]

    for relationship in relationships:
        graph.add_relationship(relationship)