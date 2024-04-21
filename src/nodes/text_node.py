from nodes.leaf_node import LeafNode


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        if self.text != node.text:
            return False

        if self.text_type != node.text_type:
            return False

        if self.url != node.url:
            return False

        return True

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(node: TextNode):
    match node.text_type:
        case "text":
            return LeafNode(None, node.text)
        case "bold":
            return LeafNode("b", node.text)
        case "italic":
            return LeafNode("i", node.text)
        case "code":
            return LeafNode("code", node.text)
        case "link":
            return LeafNode("a", node.text, {"href": node.url})
        case "image":
            return LeafNode("img", "", {"src": node.url, "alt": node.text})
        case _:
            raise ValueError("invalid text_type for TextNode")
