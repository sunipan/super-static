import unittest
from textnode import TextNode, TextType
from leafnode import LeafNode
from utils import text_node_to_html_node, split_nodes_delimiter
from enum import Enum

class TestTextNodeToHtmlNode(unittest.TestCase):

    # Test the text_node_to_html_node function
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

    # Test split_nodes_delimiter function
    def test_split_basic(self):
        node = TextNode("hello `world` goodbye", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "hello ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "world")
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertEqual(nodes[2].text, " goodbye")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

    def test_multiple_delimiters(self):
        node = TextNode("hello `world` middle `code`", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 4)
        self.assertEqual(nodes[0].text, "hello ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "world")
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertEqual(nodes[2].text, " middle ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text, "code")
        self.assertEqual(nodes[3].text_type, TextType.CODE)

    def test_no_delimiters(self):
        node = TextNode("hello world", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "hello world")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

    def test_empty_text(self):
        node = TextNode("", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 0)

    def test_multiple_nodes(self):
        node1 = TextNode("hello `world`", TextType.TEXT)
        node2 = TextNode("another `code`", TextType.TEXT)
        nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        self.assertEqual(len(nodes), 4)
        self.assertEqual(nodes[0].text, "hello ")
        self.assertEqual(nodes[1].text, "world")
        self.assertEqual(nodes[2].text, "another ")
        self.assertEqual(nodes[3].text, "code")

    def test_non_text_node(self):
        node = TextNode("hello `world`", TextType.BOLD)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "hello `world`")
        self.assertEqual(nodes[0].text_type, TextType.BOLD)

    def test_missing_closing_delimiter(self):
        node = TextNode("hello `world", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertTrue("Missing closing delimiter" in str(context.exception))

    def test_adjacent_delimiters(self):
        node = TextNode("hello``world", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text, "hello")
        self.assertEqual(nodes[1].text, "world")

    def test_starts_with_delimiter(self):
        node = TextNode("`code` hello", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text, "code")
        self.assertEqual(nodes[0].text_type, TextType.CODE)
        self.assertEqual(nodes[1].text, " hello")
        self.assertEqual(nodes[1].text_type, TextType.TEXT)

if __name__ == "__main__":
    unittest.main()
