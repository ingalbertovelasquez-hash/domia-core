from uuid import uuid4

from domia.domain.entities.knowledge_relationship import KnowledgeRelationship
from domia.domain.enums.relationship_type import RelationshipType


def test_create_relationship():

    relationship = KnowledgeRelationship(
        source_id=uuid4(),
        target_id=uuid4(),
        relationship_type=RelationshipType.CONTAINS,
    )

    assert relationship.relationship_type == RelationshipType.CONTAINS