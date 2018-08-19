class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    @classmethod
    def next_inorder(cls, root, node, next_visited=False):
        if not root:
            return None, False

        ret = None
        if root.left:
            rt, next_visited = cls.next_inorder(root.left, node, next_visited)
            ret = ret or rt

        if next_visited:
            if not ret:
                ret = root
            next_visited = False

        if root == node:
            next_visited = True

        if root.right:
            rt, next_visited = cls.next_inorder(root.right, node, next_visited)
            ret = ret or rt

        return ret, next_visited


import unittest
class TestCase(unittest.TestCase):
    def test_next_inorder(self):
        root = Node(6)
        node = Node(2)
        root.left = node
        root.left.left = Node(1)

        self.assertEqual(6, Node.next_inorder(root, node)[0].value)

        root.right = Node(7)
        self.assertEqual(7, Node.next_inorder(root, root)[0].value)

        root.left.right = Node(5)
        self.assertEqual(5, Node.next_inorder(root, node)[0].value)

        root.left.right.left = Node(4)
        self.assertEqual(4, Node.next_inorder(root, node)[0].value)

        root.left.right.left.left = Node(3)
        self.assertEqual(3, Node.next_inorder(root, node)[0].value)


if __name__ == '__main__':
    unittest.main()
