import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_value_required(self):
        with self.assertRaises(ValueError):
            LeafNode()
        with self.assertRaises(ValueError):
            LeafNode(tag="p")
        with self.assertRaises(ValueError):
            LeafNode(value=None)

    def test_init_with_value_only(self):
        node = LeafNode(value="Hello, World!")
        self.assertIsNone(node.tag)
        self.assertEqual(node.value, "Hello, World!")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_init_with_tag_value(self):
        node = LeafNode(tag="p", value="Hello, World!")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, World!")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_init_with_props(self):
        props = {"class": "text-bold", "id": "greeting"}
        node = LeafNode(value="Hello", tag="span", props=props)
        self.assertEqual(node.tag, "span")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.props, props)
        self.assertIsNone(node.children)

    def test_to_html_simple(self):
        node = LeafNode(tag="p", value="Hello, World!")
        expected = "<p>Hello, World!</p>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_props(self):
        props = {"class": "text-bold", "id": "greeting"}
        node = LeafNode(value="Hello", tag="div", props=props)
        expected = '<div class="text-bold" id="greeting">Hello</div>'
        self.assertEqual(node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()