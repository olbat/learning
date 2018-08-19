class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __iter__(self):
        cur = self
        while cur.next:
            yield(cur)
            cur = cur.next
        yield(cur)

    def add(self, value):
        for cur in self:
            pass
        cur.next = Node(value)
        return cur.next

    def selfremove(self):
        if self.next:
            self.value = self.next.value
            self.next = self.next.next


import unittest
class TestCase(unittest.TestCase):
    def test_selfremove(self):
        li = Node(1)
        li.add(2)
        li.add(3)
        toremove = li.add(4)
        li.add(5)
        toremove.selfremove()
        self.assertEqual([1,2,3,5], [n.value for n in li])


if __name__ == '__main__':
    unittest.main()
