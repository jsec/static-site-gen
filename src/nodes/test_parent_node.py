import unittest

from nodes.leaf_node import LeafNode
from nodes.parent_node import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        result = node.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(result, expected)

    def test_to_html_no_tag(self):
        with self.assertRaises(ValueError) as ex:
            node = ParentNode(None, [LeafNode("b", "Bold text")])
            _ = node.to_html()

        exception = ex.exception
        self.assertEqual(exception.args[0], "Parent node requires a tag")

    def test_to_html_no_children(self):
        with self.assertRaises(ValueError) as ex:
            node = ParentNode("p", None)
            _ = node.to_html()

        exception = ex.exception
        self.assertEqual(exception.args[0], "Parent node must have at least one child")

    def test_to_html_nested(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "b", [LeafNode("i", "italic text"), LeafNode(None, "Normal text")]
                )
            ],
        )

        result = node.to_html()
        expected = "<p><b><i>italic text</i>Normal text</b></p>"
        self.assertEqual(result, expected)
