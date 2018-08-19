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
        node = Node(value)
        for cur in self:
            pass
        cur.next = node

    def remove_duplicates(self):
        seen = {}

        ret = self
        prev = None
        for cur in self:
            if cur.value in seen:
                if prev:
                    prev.next = cur.next
                else:
                    ret = cur.next
            else:
                seen[cur.value] = True
            prev = cur

        return ret


import unittest
class TestCase(unittest.TestCase):
    def test_add(self):
        li = Node(1)
        li.add(2)
        li.add(3)
        self.assertEqual([1,2,3], [n.value for n in li])
    def test_remove_duplacates(self):
        # duplicate in the middle
        li = Node(1)
        li.add(2)
        li.add(2)
        li.add(3)
        li.add(4)
        li.add(4)
        li.add(5)
        self.assertEqual([1,2,3,4,5], [n.value for n in li.remove_duplicates()])

        # duplicate at the begining
        li = Node(1)
        li.add(1)
        li.add(2)
        li.add(3)
        self.assertEqual([1,2,3], [n.value for n in li.remove_duplicates()])

        # duplicate at the end
        li = Node(1)
        li.add(2)
        li.add(3)
        li.add(3)
        self.assertEqual([1,2,3], [n.value for n in li.remove_duplicates()])


if __name__ == '__main__':
    unittest.main()
