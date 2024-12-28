from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.props is None:
            props_str = " "
        else:
            props_str = " " + self.props_to_html() + ""
            
        if self.tag is None:
            return self.value
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"