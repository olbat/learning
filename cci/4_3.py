class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "({})".format(self.value)

    def create_lists(self, lvl=0, lists=[]):
        if len(lists) <= lvl:
            lists.append([])
        lists[lvl].append(self)
        if self.left:
            self.left.create_lists(lvl+1, lists)
        if self.right:
            self.right.create_lists(lvl+1, lists)
        return lists


import unittest
class TestCase(unittest.TestCase):
    def test_create_lists(self):
        root = Node(4)
        root.left = Node(2)
        root.left.left = Node(1)
        root.left.right = Node(3)
        root.right = Node(6)
        root.right.left = Node(5)
        root.right.right = Node(7)
        lists = root.create_lists()
        self.assertEqual([[4], [2,6], [1,3,5,7]],
                [[n.value for n in l] for l in lists])


if __name__ == '__main__':
    unittest.main()
