class EmptyStackError(Exception):
    pass
class FullStackError(Exception):
    pass

class Stack():
    def __init__(self, capacity=100):
        self.data = [None] * capacity
        self.top = -1

    def push(self, value):
        if self.is_full():
            raise FullStackError()
        else:
            self.top += 1
            self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            raise EmptyStackError()
        else:
            ret = self.data[self.top]
            self.top -= 1
            return ret

    def peek(self):
        if self.is_empty():
            raise EmptyStackError()
        else:
            return self.data[self.top - 1]

    def is_empty(self):
        return self.top < 0

    def is_full(self):
        return (self.top + 1) >= len(self.data)


class MultiStack():
    def __init__(self, capacities=100):
        self.capacities = capacities
        self.stacks = []
        #self.stacks = Stack(100)
        #self.stacks.push(Stack(self.capacities))

    def push(self, value):
        #if self.stacks.peek().is_full():
        #    self.stacks.push(Stack(self.capacities))
        #self.stacks.peek().push(value)
        if not self.stacks or self.stacks[-1].is_full():
            self.stacks.append(Stack(self.capacities))
        self.stacks[-1].push(value)

    def pop(self):
        #ret = self.stacks.peek().pop()
        #if self.stacks.peek().isempty():
        #    self.stacks.pop()
        ret = self.stacks[-1].pop()
        if self.stacks[-1].is_empty():
            self.stacks.pop()
        return ret

    def __len__(self):
        return len(self.stacks)


import unittest
class TestCase(unittest.TestCase):
    def test_push_pop(self):
        s = MultiStack(2)
        s.push(1)
        s.push(2)
        self.assertEqual(1, len(s))
        s.push(3)
        self.assertEqual(2, len(s))
        self.assertEqual(3, s.pop())
        self.assertEqual(1, len(s))
        self.assertEqual(2, s.pop())
        self.assertEqual(1, s.pop())
        self.assertEqual(0, len(s))


if __name__ == '__main__':
    unittest.main()
