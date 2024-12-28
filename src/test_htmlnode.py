import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init_basic(self):
        node = HTMLNode("p", "Hello, World!", None, {"class": "greeting"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, World!")
        self.assertIsNone(node.children)
        self.assertEqual(node.props, {"class": "greeting"})

    def test_init_with_children(self):
        child = HTMLNode("span", "child text", None, {})
        parent = HTMLNode("div", None, [child], {"id": "parent"})
        self.assertEqual(parent.tag, "div")
        self.assertIsNone(parent.value)
        self.assertEqual(len(parent.children), 1)
        self.assertEqual(parent.children[0], child)

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "text", None, {})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode("p", "text", None, {"class": "text-bold"})
        self.assertEqual(node.props_to_html(), 'class="text-bold"')

    def test_props_to_html_multiple(self):
        node = HTMLNode("p", "text", None, {"class": "text-bold", "id": "para1"})
        props_html = node.props_to_html()
        self.assertTrue('class="text-bold"' in props_html)
        self.assertTrue('id="para1"' in props_html)
        # Check that properties are separated by exactly one space
        self.assertEqual(len(props_html.split()), 2)

    # def test_repr_no_children(self):
    #     node = HTMLNode("p", "Hello", None, {"class": "greeting"})
    #     expected = '<p class="greeting" >Hello</p>'
    #     self.assertEqual(repr(node), expected)

    # def test_repr_with_children(self):
    #     child = HTMLNode("em", "emphasized", None, {})
    #     parent = HTMLNode("p", None, [child], {"class": "parent"})
    #     self.assertTrue("<p" in repr(parent))
    #     self.assertTrue("class=\"parent\"" in repr(parent))
    #     self.assertTrue("<em" in repr(parent))
    #     self.assertTrue("emphasized" in repr(parent))

if __name__ == "__main__":
    unittest.main()