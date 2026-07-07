from domia.cognition.contracts.intent import Intent
from domia.cognition.contracts.objective import Objective


class IntentAnalyzer:
    """
    Analizador de intención v2.

    Implementación basada en reglas,
    preparada para evolucionar hacia
    clasificación semántica.
    """

    ACTIONS = {
        # Creación
        "crear": "create",
        "crea": "create",
        "diseñar": "create",
        "disenar": "create",
        "generar": "create",
        "construir": "create",

        # Explicación
        "qué es": "explain",
        "que es": "explain",
        "explica": "explain",
        "explícame": "explain",
        "explicame": "explain",
        "define": "explain",

        # Análisis
        "analizar": "analyze",
        "buscar": "search",
        "comparar": "compare",

        # Resumen
        "resume": "summarize",
        "resumir": "summarize",
    }

    def analyze(self, objective: Objective) -> Intent:
        """
        Analiza el objetivo y determina:

        - acción
        - dominio
        - capacidades requeridas
        """

        text = objective.text.lower()

        # --------------------------------------------------
        # Acción
        # --------------------------------------------------

        action = "unknown"

        for keyword, value in self.ACTIONS.items():
            if keyword in text:
                action = value
                break

        # --------------------------------------------------
        # Dominio (con prioridad)
        # --------------------------------------------------

        domain = "general"

        # Educación tiene prioridad
        if (
            "curso" in text
            or "universidad" in text
            or "escuela" in text
        ):
            domain = "education"

        # Luego legal
        elif (
            "abogado" in text
            or "abogados" in text
            or "contrato" in text
        ):
            domain = "legal"

        # Luego negocios
        elif (
            "empresa" in text
            or "ventas" in text
        ):
            domain = "business"

        # Luego finanzas
        elif "finanzas" in text:
            domain = "finance"

        # Finalmente IA
        elif (
            "ia" in text
            or "inteligencia artificial" in text
            or "aprendizaje" in text
            or "machine learning" in text
        ):
            domain = "artificial_intelligence"

        # --------------------------------------------------
        # Capacidades requeridas
        # --------------------------------------------------

        capabilities = [
            "knowledge_search",
            "context_builder",
            "decision_engine",
        ]

        return Intent(
            action=action,
            domain=domain,
            subject=objective.text,
            confidence=0.95,
            required_capabilities=capabilities,
        )