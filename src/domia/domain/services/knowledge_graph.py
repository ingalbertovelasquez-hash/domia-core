from __future__ import annotations

from typing import Dict, List

from domia.domain.entities.knowledge_node import KnowledgeNode
from domia.domain.entities.knowledge_relationship import KnowledgeRelationship


class KnowledgeGraph:
    """
    Implementación en memoria del Knowledge Graph de DomIA.
    """

    def __init__(self) -> None:
        self._nodes: Dict[str, KnowledgeNode] = {}
        self._relationships: List[KnowledgeRelationship] = []

    # =====================================================
    # NODES
    # =====================================================

    def add_node(self, node: KnowledgeNode) -> None:
        self._nodes[node.id] = node

    def get_node(self, node_id: str) -> KnowledgeNode | None:
        return self._nodes.get(node_id)

    def all_nodes(self) -> List[KnowledgeNode]:
        return list(self._nodes.values())

    def node_count(self) -> int:
        return len(self._nodes)

    # =====================================================
    # RELATIONSHIPS
    # =====================================================

    def add_relationship(self, relationship: KnowledgeRelationship) -> None:
        self._relationships.append(relationship)

    def all_relationships(self) -> List[KnowledgeRelationship]:
        return list(self._relationships)

    def relationship_count(self) -> int:
        return len(self._relationships)

    # =====================================================
    # QUERIES
    # =====================================================

    def outgoing_relationships(
        self,
        node_id: str,
    ) -> List[KnowledgeRelationship]:
        return [
            rel
            for rel in self._relationships
            if rel.source_id == node_id
        ]

    def incoming_relationships(
        self,
        node_id: str,
    ) -> List[KnowledgeRelationship]:
        return [
            rel
            for rel in self._relationships
            if rel.target_id == node_id
        ]

    def get_neighbors(
        self,
        node_id: str,
    ) -> List[KnowledgeNode]:
        """
        Devuelve todos los nodos conectados mediante relaciones salientes.
        """

        neighbors: List[KnowledgeNode] = []

        for relationship in self.outgoing_relationships(node_id):
            node = self.get_node(relationship.target_id)
            if node is not None:
                neighbors.append(node)

        return neighbors