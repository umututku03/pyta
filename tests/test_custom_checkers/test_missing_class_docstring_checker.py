import astroid
import pylint.testutils
from astroid import nodes

# import our custom checker
from python_ta.checkers.missing_class_docstring_checker import (
    MissingClassDocstringChecker,
)


class TestMissingClassDocstringChecker(pylint.testutils.CheckerTestCase):
    """
    Class for testing the custom checker created for missing class docstring.
    """

    CHECKER_CLASS = MissingClassDocstringChecker

    def test_missing_docstring(self) -> None:
        """
        Test the checker on a class with missing docstring.
        """
        src = '''
        class WrongClass:
            attr1: int

            def __init__(self):
                """Initialize this WrongClass/"""
                self.attr1 = 1

        '''
        mod = astroid.parse(src)  # obtain the AST from the given src
        class_node, *_ = mod.nodes_of_class(
            nodes.ClassDef
        )  # obtain the class Node from the given AST

        with self.assertAddsMessages(
            pylint.testutils.MessageTest(
                msg_id="missing-class-docstring", node=class_node, args=class_node.name
            ),
            ignore_position=True,
        ):
            self.checker.visit_classdef(class_node)

    def test_complete_docstring(self):
        """Test the checker on a class with complete docstring."""

        src = '''
        class CorrectClass:
            """All classes, including empty ones should have docstrings."""
            attr1: int

            def __init__(self):
                """Initialize this CorrectClass"""
                self.attr1 = 1

        '''
        mod = astroid.parse(src)  # obtain the AST from the given src
        class_node, *_ = mod.nodes_of_class(
            nodes.ClassDef
        )  # obtain the class Node from the given AST

        with self.assertNoMessages():
            self.checker.visit_classdef(class_node)


if __name__ == "__main__":
    import pytest

    pytest.main(["test_missing_class_docstring_checker.py"])
