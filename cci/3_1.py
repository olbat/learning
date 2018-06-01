class FullStackError(Exception):
    pass
class EmptyStackError(Exception):
    pass

class MultiStack():
    def __init__(self, num=3, capacity=100):
        self.data = [0 for _ in range(capacity)]
        self.bases = [(capacity//num) * i for i in range(num)]
        self.heads = self.bases.copy()

    def push(self, num, value):
        self.heads[num] += 1
        if num + 1 == len(self.heads):  # last element
            next_base = len(self.data) - 1
        else:
            next_base = self.bases[num+1]

        if self.heads[num] >= next_base:
            raise FullStackError

        self.data[self.heads[num]] = value

    def pop(self, num):
        ret = self.data[self.heads[num]]
        head = self.heads[num] - 1

        if head < self.bases[num]:
            raise EmptyStackError
        else:
            self.heads[num] = head

        return ret


import unittest
class TestCase(unittest.TestCase):
    def test_push_pop(self):
        s = MultiStack(3, 10)
        s.push(0, 1)
        s.push(0, 2)
        s.push(1, 3)
        self.assertEqual(2, s.pop(0))
        self.assertEqual(1, s.pop(0))
        self.assertEqual(3, s.pop(1))
        with self.assertRaises(EmptyStackError):
            s.pop(1)
        with self.assertRaises(FullStackError):
            for i in range(11):
                s.push(2, i)


if __name__ == '__main__':
    unittest.main()

