from uuid import UUID

from domia.domain.entities.knowledge_node import KnowledgeNode
from domia.domain.entities.knowledge_relationship import (
    KnowledgeRelationship,
)


class KnowledgeGraph:
    """
    Servicio de dominio que mantiene un grafo
    de conocimiento completamente en memoria.
    """

    def __init__(self):

        self._nodes: dict[UUID, KnowledgeNode] = {}

        self._relationships: list[KnowledgeRelationship] = []

    def add_node(self, node: KnowledgeNode):

        self._nodes[node.id] = node

    def get_node(self, node_id: UUID):

        return self._nodes.get(node_id)

    def add_relationship(
        self,
        relationship: KnowledgeRelationship,
    ):

        self._relationships.append(relationship)

    def get_neighbors(
        self,
        node_id: UUID,
    ):

        neighbors = []

        for relationship in self._relationships:

            if relationship.source_id == node_id:

                target = self.get_node(
                    relationship.target_id
                )

                if target:

                    neighbors.append(target)

        return neighbors