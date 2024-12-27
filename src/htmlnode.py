class HTMLNode:

  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError
    pass

  def props_to_html(self):
    props_string = ""
    for key, value in self.props.items():
      props_string += f'{key}="{value}" '
    return props_string

  def __repr__(self):
    node_string = ""
    node_string += f'<{self.tag} {self.props_to_html()}>'
    if self.value:
      node_string += f'{self.value}'
    if self.children:
      for child in self.children:
        node_string += f'{child.to_html()}'
    node_string += f'</{self.tag}>'
    return node_string