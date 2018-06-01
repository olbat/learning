class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __iter__(self):
        ptr = self
        while ptr.next:
            yield ptr
            ptr = ptr.next
        yield ptr

    def add(self, node):
        for ptr in self:
            pass
        ptr.next = node

    def intersects(self, other):
        nodes = {}
        for node in self:
            nodes[node] = True
        for node in other:
            if node in nodes:
                return True
        return False


import unittest
class TestCase(unittest.TestCase):
    def test_intersects(self):
        l1 = Node(1)
        l1.add(Node(2))
        l1.add(Node(3))
        l1.add(Node(4))

        l2 = Node(1)
        l2.add(Node(2))

        self.assertFalse(l1.intersects(l2))
        self.assertFalse(l2.intersects(l1))

        n = Node(5)
        l1.add(n)
        l2.add(n)
        self.assertTrue(l1.intersects(l2))
        self.assertTrue(l2.intersects(l1))

        l1.add(Node(7))
        l2.add(Node(8))
        self.assertTrue(l1.intersects(l2))
        self.assertTrue(l2.intersects(l1))


if __name__ == '__main__':
    unittest.main()
