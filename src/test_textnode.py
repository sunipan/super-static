import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)
    
  def test_eq_w_url(self):
    node = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
    node2 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
    self.assertEqual(node, node2)
    
  def test_to_str(self):
    node = TextNode("This is a text node", TextType.ITALIC, "https://boot.dev")  
    self.assertEqual(f"TextNode(This is a text node, italic, https://boot.dev)", str(node))


if __name__ == "__main__":
    unittest.main()