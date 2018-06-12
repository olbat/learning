class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def find_fca(self, node1, node2):
        # uncomment lines to handle the case: node1 or node2 not in the tree
        if (self == node1) or (self == node2):
            #return None, True
            return self
        else:
            rightval = leftval = None
            #rightfound = leftfound = False
            if self.right:
                #rightval, rightfound = self.right.find_fca(node1, node2)
                rightval = self.right.find_fca(node1, node2)
            if self.left:
                #leftval, leftfound = self.left.find_fca(node1, node2)
                leftval = self.left.find_fca(node1, node2)

            #if rightfound and leftfound:
            #    return self, True
            if rightval and leftval:
                return self
            else:
                return rightval or leftval
                #return (rightval or leftval), (rightfound or leftfound)


import unittest
class TestCase(unittest.TestCase):
    def test_find_fca(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.left.left = Node(4)
        root.left.left.left.left = Node(4)
        root.left.left.left.left.right = Node(5)
        root.left.right = Node(6)
        root.left.right.left = Node(7)
        root.left.right.right = Node(8)

        #n, _ = root.find_fca(root.left.left.left.left.right, root.left.right.right)
        n = root.find_fca(root.left.left.left.left.right, root.left.right.right)
        self.assertEqual(root.left, n)

        #n, _ = root.find_fca(root.left.left.left.left.right, Node(9))
        #self.assertIsNone(n)
            

if __name__ == '__main__':
    unittest.main()
