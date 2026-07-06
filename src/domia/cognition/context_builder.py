from uuid import UUID

from domia.domain.services.knowledge_graph import KnowledgeGraph


class ContextBuilder:

    def __init__(self, graph: KnowledgeGraph):
        self.graph = graph

    def build(self, node_id: UUID):

        node = self.graph.get_node(node_id)

        if node is None:
            return []

        context = [node]

        context.extend(
            self.graph.get_neighbors(node_id)
        )

        return context