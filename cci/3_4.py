class EmptyError(Exception):
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
            raise EmptyError()

    def peek(self):
        if self:
            return self.data[0]
        else:
            raise EmptyError()

class Queue():
    def __init__(self):
        self.enq_stack = Stack()
        self.deq_stack = Stack()

    def enqueue(self, value):
        self.enq_stack.push(value)

    def dequeue(self):
        if not self.deq_stack:
            while self.enq_stack:
                self.deq_stack.push(self.enq_stack.pop())
        return self.deq_stack.pop()


import unittest
class TestCase(unittest.TestCase):
    def test_enqueue_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(1, q.dequeue())
        self.assertEqual(2, q.dequeue())
        q.enqueue(4)
        self.assertEqual(3, q.dequeue())
        self.assertEqual(4, q.dequeue())


if __name__ == '__main__':
    unittest.main()
