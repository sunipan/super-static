from textnode import TextNode, TextType
from utils import text_node_to_html_node

def main():
  tn = TextNode("This is a text node", TextType.BOLD)
  html_node = text_node_to_html_node(tn)
  print(html_node)

if __name__ == "__main__":
  main()