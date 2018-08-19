class EmptyStackError(Exception):
    pass

class Stack():
    def __init__(self):
        self.data = []

    def __bool__(self):
        return len(self.data) > 0

    def push(self, value):
        self.data.insert(0, value)

    def pop(self):
        if self:
            return self.data.pop(0)
        else:
            raise EmptyStackError()

    def peek(self):
        if self:
            return self.data[0]
        else:
            raise EmptyStackError()

    def sort(self):
        tmps = Stack()

        while self:
            v = self.pop()
            while tmps and (tmps.peek() > v):
                self.push(tmps.pop())
            tmps.push(v)

        while tmps:
            self.push(tmps.pop())


import unittest
class TestCase(unittest.TestCase):
    def test_sort(self):
        s = Stack()
        s.push(2)
        s.push(1)
        s.push(4)
        s.push(3)
        s.push(5)
        s.sort()

        a = []
        while s:
            a.append(s.pop())
        self.assertEqual([1,2,3,4,5], a)

if __name__ == '__main__':
    unittest.main()
