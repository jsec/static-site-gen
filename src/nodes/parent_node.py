from nodes.html_node import HtmlNode


class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)
        self.children = children

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node requires a tag")

        if self.children is None or len(self.children) == 0:
            raise ValueError("Parent node must have at least one child")

        output = self.opening_tag()
        for child in self.children:
            output += child.to_html()

        output += self.closing_tag()

        return output
