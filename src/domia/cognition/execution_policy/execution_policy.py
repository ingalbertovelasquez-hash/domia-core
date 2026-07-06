from domia.cognition.contracts.intent import Intent
from domia.cognition.execution_policy.policy import Policy


class ExecutionPolicy:
    """
    Motor de políticas de ejecución.

    Decide qué componentes del sistema
    deben participar según la intención.
    """

    def create(self, intent: Intent) -> Policy:

        capabilities = list(intent.required_capabilities)

        use_memory = True

        use_knowledge_graph = "knowledge_search" in capabilities

        build_context = "context_builder" in capabilities

        build_prompt = True

        execute_model = False

        return Policy(
            use_memory=use_memory,
            use_knowledge_graph=use_knowledge_graph,
            build_context=build_context,
            build_prompt=build_prompt,
            execute_model=execute_model,
            capabilities=capabilities,
        )