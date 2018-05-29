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

    def partition(self, x):
        prev = self
        pivot = None
        prevpivot = None
        for n in self:
            if pivot:
                if n.value < x:
                    prev.next = n.next
                    n.next = pivot
                    prevpivot.next = n
                    prevpivot = n
            elif n.value >= x:
                pivot = n
                prevpivot = prev
            prev = n
        return self


import unittest
class TestCase(unittest.TestCase):
    def test_partition(self):
        li = Node(1)
        li.add(6)
        li.add(4)
        li.add(3)
        li.add(2)
        li.add(5)
        self.assertEqual([1,2,6,4,3,5], [n.value for n in li.partition(3)])

        li = Node(2)
        li.add(6)
        li.add(4)
        li.add(3)
        li.add(5)
        self.assertEqual([2,6,4,3,5], [n.value for n in li.partition(2)])


if __name__ == '__main__':
    unittest.main()
