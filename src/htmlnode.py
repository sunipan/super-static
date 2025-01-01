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
    if self.props == None:
      return props_string

    length = len(self.props)
    counter = 0
    for key, value in self.props.items():
      props_string += f'{key}="{value}"'
      counter += 1
      if counter < length:
        props_string += " "

    return props_string
    pass

  def __repr__(self):
    node_string = f'<{self.tag}'
    if self.props != None:
      node_string += f' {self.props_to_html()}'
    node_string += '>'
    
    if self.value:
      node_string += f'{self.value}'
    if self.children:
      for child in self.children:
        node_string += f'{child.to_html()}'
    node_string += f'</{self.tag}>'
    return node_string
    pass