class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented yet")

    def props_to_html(self):
        if self.props is None or self.props == {}:
            return ""

        return " ".join([f'{key}="{self.props[key]}"' for key in self.props])

    def opening_tag(self):
        if self.props:
            return f"<{self.tag} {self.props_to_html()}>"
        else:
            return f"<{self.tag}>"

    def closing_tag(self):
        return f"</{self.tag}>"

    def __repr__(self) -> str:
        return ""
