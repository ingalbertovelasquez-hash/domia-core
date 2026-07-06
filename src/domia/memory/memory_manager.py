from domia.memory.episodic.episodic_memory import EpisodicMemory
from domia.memory.semantic.semantic_memory import SemanticMemory
from domia.memory.working.working_memory import WorkingMemory


class MemoryManager:
    """
    Orquesta las memorias de DomIA.
    """

    def __init__(self):
        self.working = WorkingMemory()
        self.semantic = SemanticMemory()
        self.episodic = EpisodicMemory()

    def clear_all(self) -> None:
        self.working.clear()
        self.semantic.clear()
        self.episodic.clear()