import unittest

from nodes.html_node import HtmlNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HtmlNode(
            "a", "value", None, {"href": "http://example.com", "target": "_blank"}
        )
        result = node.props_to_html()
        expected = 'href="http://example.com" target="_blank"'
        self.assertEqual(result, expected)

    def test_props_to_html_no_props(self):
        node = HtmlNode("a", "value")
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_props_to_html_empty_props(self):
        node = HtmlNode("a", "value", None, {})
        result = node.props_to_html()
        self.assertEqual(result, "")
