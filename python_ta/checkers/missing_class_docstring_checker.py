"""Checker for C0115 (missing-class-docstring) """
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.checkers.utils import only_required_for_messages
from pylint.lint import PyLinter


class MissingClassDocstringChecker(BaseChecker):
    """
    Checker for missing docstrings in classes (even empty classes should have docstrings).
    """

    # Using name to generate a special configuration section for the checker.
    name = "missing_class_docstring"

    # Problems being displayed to the user through these messages
    msgs = {
        "W0000": (  # the message id
            "Missing docstring for the class",  # template of the displayed message
            "new-missing-class-docstring",  # message symbol
            "Used when a given class does not have a docstring.",
        )
    }

    # An optional argument for making sure that this checker is executed before others
    priority = -1

    @only_required_for_messages("new-missing-class-docstring")
    def visit_classdef(self, node: nodes.ClassDef):
        """
        Visit a class definition.
        """
        if node.doc_node is None:
            self.add_message("new-missing-class-docstring", node=node, args=node.name)


def register(linter: "PyLinter") -> None:
    """required method to auto register this checker"""
    linter.register_checker(MissingClassDocstringChecker(linter))
