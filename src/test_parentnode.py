import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_init_basic(self):
        """Test basic initialization of ParentNode"""
        children = [LeafNode("p", "child1"), LeafNode("span", "child2")]
        node = ParentNode("div", children)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children, children)
        self.assertIsNone(node.value)
        self.assertEqual(node.props, None)

    def test_init_with_props(self):
        """Test initialization with properties"""
        children = [LeafNode("p", "child")]
        props = {"class": "container", "id": "main"}
        node = ParentNode("div", children, props)
        self.assertEqual(node.props, props)

    def test_to_html_basic(self):
        """Test basic HTML generation"""
        children = [LeafNode("p", "Hello"), LeafNode("span", "World")]
        node = ParentNode("div", children)
        expected = '<div><p>Hello</p><span>World</span></div>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_props(self):
        """Test HTML generation with properties"""
        children = [LeafNode("p", "Content")]
        props = {"class": "main", "id": "content"}
        node = ParentNode("div", children, props)
        expected = '<div class="main" id="content"><p>Content</p></div>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_nested(self):
        """Test HTML generation with nested ParentNodes"""
        inner_children = [LeafNode("span", "Inner")]
        inner_node = ParentNode("div", inner_children, {"class": "inner"})
        outer_children = [LeafNode("p", "Outer"), inner_node]
        outer_node = ParentNode("div", outer_children, {"class": "outer"})
        expected = '<div class="outer"><p>Outer</p><div class="inner"><span>Inner</span></div></div>'
        self.assertEqual(outer_node.to_html(), expected)

    def test_no_tag_error(self):
        """Test that ParentNode raises error when tag is None"""
        children = [LeafNode("p", "content")]
        node = ParentNode(None, children)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have a tag")

    def test_empty_children(self):
        """Test HTML generation with no children"""
        node = ParentNode("div", [])
        expected = '<div></div>'
        self.assertEqual(node.to_html(), expected)

    def test_mixed_children(self):
        """Test HTML generation with mix of LeafNode and ParentNode children"""
        inner_node = ParentNode("nav", [LeafNode("a", "Link")], {"class": "menu"})
        children = [
            LeafNode("h1", "Title"),
            inner_node,
            LeafNode("p", "Content")
        ]
        node = ParentNode("div", children, {"id": "main"})
        expected = '<div id="main"><h1>Title</h1><nav class="menu"><a>Link</a></nav><p>Content</p></div>'
        self.assertEqual(node.to_html(), expected)

    def test_deeply_nested_structure(self):
        """Test HTML generation with a deeply nested structure"""
        menu_item = LeafNode("a", "Home", {"href": "/"})
        menu = ParentNode("nav", [menu_item], {"class": "menu"})
        header = ParentNode("header", [
            LeafNode("h1", "Welcome"),
            menu
        ])
        content = ParentNode("main", [
            LeafNode("h2", "Content"),
            LeafNode("p", "Some text")
        ])
        footer = ParentNode("footer", [
            LeafNode("span", "Copyright 2024")
        ])
        
        page = ParentNode("div", [header, content, footer], {"class": "page"})
        expected = '<div class="page"><header><h1>Welcome</h1><nav class="menu"><a href="/">Home</a></nav></header><main><h2>Content</h2><p>Some text</p></main><footer><span>Copyright 2024</span></footer></div>'
        self.assertEqual(page.to_html(), expected)

if __name__ == '__main__':
    unittest.main()