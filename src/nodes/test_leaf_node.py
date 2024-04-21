import unittest

from nodes.leaf_node import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        result = node.to_html()
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(result, expected)

    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a raw value.")
        result = node.to_html()
        expected = "This is a raw value."
        self.assertEqual(result, expected)

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = node.to_html()
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(result, expected)
