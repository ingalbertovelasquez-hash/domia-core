from domia.cognition.contracts.context import Context


class PromptBuilder:
    """
    Construye el prompt final que será enviado
    al modelo de IA.
    """

    def build(self, context: Context) -> str:

        sections = [
            f"Objective: {context.objective}",
            f"Intent: {context.intent}",
        ]

        if context.plan:
            sections.append("\nExecution Plan:")
            sections.extend(f"- {step}" for step in context.plan)

        if context.knowledge:
            sections.append("\nKnowledge:")
            sections.extend(f"- {item}" for item in context.knowledge)

        if context.notes:
            sections.append("\nNotes:")
            sections.extend(f"- {note}" for note in context.notes)

        sections.append("\nGenerate the best possible response.")

        return "\n".join(sections)