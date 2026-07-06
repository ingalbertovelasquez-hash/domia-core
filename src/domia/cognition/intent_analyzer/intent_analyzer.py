from domia.cognition.contracts.intent import Intent
from domia.cognition.contracts.objective import Objective


class IntentAnalyzer:
    """
    Analizador de intención (v1).

    Primera implementación basada en reglas.
    Su interfaz permanecerá estable cuando
    evolucionemos hacia IA semántica.
    """

    ACTIONS = {
        "crear": "create",
        "crea": "create",
        "diseñar": "create",
        "disenar": "create",
        "generar": "create",
        "construir": "create",
        "analizar": "analyze",
        "buscar": "search",
        "comparar": "compare",
    }

    DOMAINS = {
        "curso": "education",
        "universidad": "education",
        "escuela": "education",
        "abogado": "legal",
        "abogados": "legal",
        "contrato": "legal",
        "empresa": "business",
        "ventas": "business",
        "finanzas": "finance",
        "ia": "artificial_intelligence",
    }

    def analyze(self, objective: Objective) -> Intent:

        text = objective.text.lower()

        action = "unknown"

        for keyword, value in self.ACTIONS.items():
            if keyword in text:
                action = value
                break

        # Dominio principal
        domain = "general"

        if "curso" in text:
            domain = "education"
        elif "abogado" in text or "abogados" in text:
            domain = "legal"
        elif "empresa" in text:
            domain = "business"

        subject = objective.text

        capabilities = [
            "knowledge_search",
            "context_builder",
            "decision_engine",
        ]

        return Intent(
            action=action,
            domain=domain,
            subject=subject,
            confidence=0.95,
            required_capabilities=capabilities,
        )