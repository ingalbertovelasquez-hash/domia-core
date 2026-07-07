from enum import Enum


class Strategy(Enum):
    """
    Estrategias cognitivas disponibles
    para el Reasoning Engine.
    """

    DIRECT = "DIRECT"

    PLAN = "PLAN"

    ANALYZE = "ANALYZE"

    DESIGN = "DESIGN"

    DEDUCE = "DEDUCE"