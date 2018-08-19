class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __len__(self):
        return sum(1 for _ in self)

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

    def kth_to_last(self, k):
        assert(k > 0)
        runner = iter(self)
        slow = iter(self)

        try:
            for _ in range(k):
                next(runner)
        except StopIteration:  # in the case k > len(self)
            return self

        ret = next(slow)
        try:
            while True:
                next(runner)
                ret = next(slow)
        except StopIteration:
            pass

        return ret


import unittest
class TestCase(unittest.TestCase):
    def test_kth_to_last(self):
        li = Node(1)
        li.add(2)
        li.add(3)
        li.add(4)
        li.add(5)
        self.assertEqual([4,5], [v.value for v in li.kth_to_last(2)])
        self.assertEqual([5], [v.value for v in li.kth_to_last(1)])
        self.assertEqual([1,2,3,4,5], [v.value for v in li.kth_to_last(5)])
        self.assertEqual([1,2,3,4,5], [v.value for v in li.kth_to_last(6)])


if __name__ == '__main__':
    unittest.main()
