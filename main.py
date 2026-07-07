import sys

from domia.bootstrap.foundation import load_foundation_graph
from domia.cognition.decision_engine.decision_engine import DecisionEngine
from domia.interfaces.cli.cli import DomIACLI


def main():

    cli = DomIACLI()

    if len(sys.argv) == 1:
        print("Available commands:")
        print("  status")
        print("  demo")
        print("  decide")
        print("  ask")
        return

    command = sys.argv[1]

    if command == "status":

        cli.status()

    elif command == "demo":

        graph = load_foundation_graph()

        print("=" * 50)
        print("DomIA Foundation Knowledge Graph")
        print("=" * 50)

        for node in graph.all_nodes():
            print(f"✓ {node.name} ({node.node_type})")

        print()
        print(f"Nodes         : {graph.node_count()}")
        print(f"Relationships : {graph.relationship_count()}")
        print()
        print("Foundation Graph Loaded Successfully")

    elif command == "decide":

        graph = load_foundation_graph()

        engine = DecisionEngine(graph)

        decision = engine.decide(
            "Create an AI course"
        )

        print("=" * 50)
        print("DomIA Decision Engine")
        print("=" * 50)
        print(f"Objective : {decision.objective}")
        print()

        print("Recommended Knowledge:")
        for node in decision.recommended_nodes:
            print(f" • {node}")

        print()

        print(f"Reasoning : {decision.reasoning}")
        print(f"Engine    : {decision.recommended_engine}")

    elif command == "ask":

        if len(sys.argv) < 3:
            print(
                'Usage: python main.py ask "your question"'
            )
            return

        question = " ".join(sys.argv[2:])

        cli.ask(question)

    else:

        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()