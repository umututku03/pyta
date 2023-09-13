"""Examples for C00115 Missing Class Docstring"""


class CorrectClass:
    """All classes, including empty ones should """
    attr1: int

    def __init__(self):
        """Initialize this CorrectClass"""
        self.attr1 = 1


class WrongClass:
    # Error raised, ass all classes should have docstrings.
    attr1: int

    def __init__(self):
        """Initialize this WrongClass"""
        self.attr1 = 1
