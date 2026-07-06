from domia.memory.semantic.semantic_memory import SemanticMemory


def test_semantic_memory():

    memory = SemanticMemory()

    memory.store("framework", "PECRA")

    assert memory.contains("framework")

    assert memory.recall("framework") == "PECRA"

    assert memory.size() == 1


def test_clear_semantic_memory():

    memory = SemanticMemory()

    memory.store("a", 1)
    memory.store("b", 2)

    memory.clear()

    assert memory.size() == 0