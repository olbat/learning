class Stack():
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.insert(0, value)

    def pop(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

    def __bool__(self):
        return len(self.data) > 0


class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.minstack = Stack()

    def push(self, value):
        super().push(value)
        if not self.minstack or value <= self.minstack.peek():
            self.minstack.push(value)

    def pop(self):
        ret = super().pop()
        if self.minstack.peek() == ret:
            self.minstack.pop()
        return ret

    def min(self):
        if self.minstack:
            return self.minstack.peek()
        else:
            return False


import unittest
class TestCase(unittest.TestCase):
    def test_push(self):
        s = MinStack()
        s.push(2)
        s.push(3)
        s.push(1)
        self.assertEqual(1, s.min())
        s.pop()
        self.assertEqual(2, s.min())
        s.pop()
        self.assertEqual(2, s.min())


if __name__ == '__main__':
    unittest.main()
