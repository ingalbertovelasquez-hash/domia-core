from domia.memory.working.working_memory import WorkingMemory


def test_working_memory():

    memory = WorkingMemory()

    assert memory.size() == 0

    memory.put("objective", "Create AI Course")

    assert memory.size() == 1

    assert memory.get("objective") == "Create AI Course"

    memory.remove("objective")

    assert memory.get("objective") is None

    assert memory.size() == 0


def test_clear_working_memory():

    memory = WorkingMemory()

    memory.put("a", 1)
    memory.put("b", 2)
    memory.put("c", 3)

    assert memory.size() == 3

    memory.clear()

    assert memory.size() == 0