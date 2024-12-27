import unittest

from src.textnode import TextNode, TextType


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
        self.assertEqual("TextNode(This is a text node, italic, https://boot.dev)", str(node))

    def test_not_equal_different_text(self):
        node1 = TextNode("Text 1", TextType.TEXT)
        node2 = TextNode("Text 2", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_type(self):
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_url(self):
        node1 = TextNode("Same text", TextType.LINK, "https://example1.com")
        node2 = TextNode("Same text", TextType.LINK, "https://example2.com")
        self.assertNotEqual(node1, node2)

    def test_all_text_types(self):
        test_text = "Test text"
        for text_type in TextType:
            node = TextNode(test_text, text_type)
            self.assertEqual(node.text_type, text_type)
            self.assertEqual(node.text, test_text)

    def test_image_node(self):
        alt_text = "Beautiful sunset"
        image_url = "https://example.com/sunset.jpg"
        node = TextNode(alt_text, TextType.IMAGE, image_url)
        self.assertEqual(node.text, alt_text)
        self.assertEqual(node.text_type, TextType.IMAGE)
        self.assertEqual(node.url, image_url)

    def test_link_node(self):
        link_text = "Click here"
        url = "https://example.com"
        node = TextNode(link_text, TextType.LINK, url)
        self.assertEqual(node.text, link_text)
        self.assertEqual(node.text_type, TextType.LINK)
        self.assertEqual(node.url, url)

    def test_str_no_url(self):
        node = TextNode("Plain text", TextType.TEXT)
        self.assertEqual("TextNode(Plain text, text, None)", str(node))


if __name__ == "__main__":
    unittest.main()