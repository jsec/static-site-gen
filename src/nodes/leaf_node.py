from nodes.html_node import HtmlNode


class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leaf node has no value")

        if self.tag is None:
            return self.value

        return f"{self.opening_tag()}{self.value}{self.closing_tag()}"
