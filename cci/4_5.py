class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    ## check using in-order traversal
    #def isbst(self, checklist=None):
    #    if not checklist:
    #        checklist = []
    #    if self.left:
    #        self.left.isbst(checklist)
    #    checklist.append(self.value)
    #    if self.right:
    #        self.right.isbst(checklist)
    #    return checklist == sorted(checklist)

    def isbst(self, vmin=float('-inf'), vmax=float('inf')):
        bst = (self.value >= vmin) and (self.value < vmax)
        if self.left:
            bst = bst and self.left.isbst(vmin, self.value) 
        if self.right:
            bst = bst and self.right.isbst(self.value, vmax) 
        return bst


import unittest
class TestCase(unittest.TestCase):
    def test_isbst(self):
        root = Node(5)
        root.left = Node(2)
        root.left.left = Node(1)
        root.right = Node(7)
        root.right.left = Node(6)
        root.right.right = Node(3)
        self.assertFalse(root.isbst())

        root.right.right = Node(8)
        self.assertTrue(root.isbst())

        root = Node(4)
        root.left = Node(3)
        root.left.left = Node(2)
        root.left.left.left = Node(1)
        self.assertTrue(root.isbst())


if __name__ == '__main__':
    unittest.main()
