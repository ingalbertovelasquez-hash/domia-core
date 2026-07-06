from enum import Enum


class RelationshipType(str, Enum):
    CONTAINS = "contains"
    USES = "uses"
    BELONGS_TO = "belongs_to"
    GENERATES = "generates"
    DEPENDS_ON = "depends_on"
    REFERENCES = "references"