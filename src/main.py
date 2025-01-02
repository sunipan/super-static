from textnode import TextNode, TextType
from utils import split_nodes_delimiter, text_node_to_html_node

def main():
  tn = TextNode("This is a text node `code block` hello word", TextType.TEXT)
  split_nodes = split_nodes_delimiter([tn], '`', TextType.CODE)
  print(split_nodes)

if __name__ == "__main__":
  main()