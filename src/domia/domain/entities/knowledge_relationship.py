from dataclasses import dataclass, field
from uuid import UUID, uuid4

from domia.domain.enums.relationship_type import RelationshipType


@dataclass
class KnowledgeRelationship:
    source_id: UUID
    target_id: UUID
    relationship_type: RelationshipType

    id: UUID = field(default_factory=uuid4)