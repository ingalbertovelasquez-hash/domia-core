from domia.domain.services.knowledge_graph import KnowledgeGraph


class DomIACLI:

    def __init__(self):
        self.graph = KnowledgeGraph()

    def status(self):

        print("=" * 40)
        print("DomIA Cognitive Operating System")
        print("Version : 0.1.0")
        print(f"Nodes   : {len(self.graph._nodes)}")
        print(f"Relations: {len(self.graph._relationships)}")
        print("Status  : READY")
        print("=" * 40)