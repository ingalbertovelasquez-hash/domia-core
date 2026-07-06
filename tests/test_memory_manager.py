from domia.memory.memory_manager import MemoryManager


def test_memory_manager():

    manager = MemoryManager()

    manager.working.put("objective", "AI")

    manager.semantic.store("framework", "PECRA")

    manager.episodic.remember("Created objective")

    assert manager.working.size() == 1
    assert manager.semantic.size() == 1
    assert manager.episodic.size() == 1

    manager.clear_all()

    assert manager.working.size() == 0
    assert manager.semantic.size() == 0
    assert manager.episodic.size() == 0