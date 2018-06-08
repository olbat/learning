class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def isbalanced(self):
        balanced = True
        if self.left:
            balanced, lheight = self.left.isbalanced()
        else:
            lheight = 0
        if balanced and self.right:
            balanced, rheight = self.left.isbalanced()
        else:
            rheight = 0
        balanced = balanced and (abs(rheight - lheight) <= 1)
        return balanced, max(lheight, rheight) + 1


import unittest
class TestCase(unittest.TestCase):
    def test_isbalanced(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.left.left = Node(4)
        root.left.right = Node(5)
        root.right = Node(6)
        self.assertFalse(root.isbalanced())
        root.right.left = Node(7)
        root.right.right = Node(8)
        self.assertTrue(root.isbalanced())


if __name__ == '__main__':
    unittest.main()
