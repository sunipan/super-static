from typing import Text
from textnode import TextType, TextNode
from leafnode import LeafNode


def text_node_to_html_node(text_node):
  if text_node.text_type is TextType.TEXT:
    return LeafNode(None, text_node.text, None)
  elif text_node.text_type is TextType.BOLD:
    return LeafNode("b", text_node.text, None)
  elif text_node.text_type is TextType.ITALIC:
    return LeafNode("i", text_node.text, None)
  elif text_node.text_type is TextType.CODE:
    return LeafNode("code", text_node.text, None)
  elif text_node.text_type is TextType.LINK:
    return LeafNode("a", text_node.text, {"href": text_node.url})
  elif text_node.text_type is TextType.IMAGE:
    return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
  else:
    raise Exception(f"Invalid TextNode type: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  raise NotImplementedError



