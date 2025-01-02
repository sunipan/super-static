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
  split_nodes = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      split_nodes.append(node)
      continue
    
    delim_count = 0
    for char in node.text:
      if char == delimiter:
        delim_count += 1
    
    # Check for missing closing delimiter
    if delim_count % 2 != 0:
      raise Exception(f"Missing closing delimiter '{delimiter}'")
    
    split_text = node.text.split(delimiter)

    for i, split in enumerate(split_text):
      if split == '':
        continue
      if i % 2 == 0:
        split_nodes.append(TextNode(split, TextType.TEXT))
      else:
        split_nodes.append(TextNode(split, text_type))
        
  return split_nodes