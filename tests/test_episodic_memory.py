from domia.memory.episodic.episodic_memory import EpisodicMemory


def test_episodic_memory():

    memory = EpisodicMemory()

    memory.remember("User created an AI course")

    assert memory.size() == 1

    episodes = memory.recall()

    assert episodes[0].description == "User created an AI course"