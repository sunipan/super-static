from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if self.tag is None:
      raise ValueError("ParentNode must have a tag")
    html_string = f'<{self.tag}'
    if self.props != None:
      html_string += f' {self.props_to_html()}'
    html_string += f'>'
    return f'{html_string}{"".join([child.to_html() for child in self.children])}</{self.tag}>'