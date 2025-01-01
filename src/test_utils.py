import unittest
from textnode import TextNode, TextType
from leafnode import LeafNode
from utils import text_node_to_html_node
from enum import Enum

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_conversion(self):
        text_node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertIsNone(html_node.tag)
        self.assertEqual(html_node.value, "Hello, world!")
        self.assertIsNone(html_node.props)

    def test_bold_conversion(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")
        self.assertIsNone(html_node.props)

    def test_italic_conversion(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")
        self.assertIsNone(html_node.props)

    def test_code_conversion(self):
        text_node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code text")
        self.assertIsNone(html_node.props)

    def test_link_conversion(self):
        text_node = TextNode("Click me", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me")
        self.assertEqual(html_node.props["href"], "https://example.com")

    def test_image_conversion(self):
        text_node = TextNode("Alt text", TextType.IMAGE, "image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "image.png")
        self.assertEqual(html_node.props["alt"], "Alt text")

    def test_invalid_type(self):
        # Create a TextNode with an invalid type to test error handling
        class InvalidType(Enum):
            INVALID = "invalid"
        
        text_node = TextNode("Invalid", InvalidType.INVALID)
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(text_node)
        self.assertTrue("Invalid TextNode type" in str(context.exception))

if __name__ == "__main__":
    unittest.main()
