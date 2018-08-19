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

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __iter__(self):
        cur = self
        while cur.next:
            yield cur
            cur = cur.next
        yield cur

    def add(self, node):
        for cur in self:
            pass
        cur.next = node

    def ispalindrome(self):
        # use a stack to store the values up to the middle of the list
        stack = Stack()

        # use two pointers that move at different speed
        slow = self
        fast = self

        while fast and fast.next:  # iterate to the middle of the list
            stack.push(slow.value)
            slow = slow.next
            fast = fast.next.next

        if fast:  # the list has an odd number of elements
            slow = slow.next

        while slow:
            if slow.value != stack.pop():
                return False
            slow = slow.next

        return True

    #def ispalindrome(self):
    #    sz = sum(1 for _ in self)
    #    palin, _ = self._check_palindrome(self, sz // 2, (sz % 2) == 1)
    #    return palin

    def _check_palindrome(self, node, count, odd=False):
        if count <= 0:
            if odd:
                return True, node.next
            else:
                return True, node
        else:
            palin, ptr = self._check_palindrome(node.next, count - 1, odd)
            if ptr:
                return (palin and (node.value == ptr.value)), ptr.next
            else:
                return False, None


import unittest
class TestCase(unittest.TestCase):
    def test_ispalindrome(self):
        li = Node('a')
        li.add(Node('b'))
        li.add(Node('b'))
        li.add(Node('a'))
        self.assertTrue(li.ispalindrome())

        li = Node('a')
        li.add(Node('b'))
        li.add(Node('c'))
        li.add(Node('b'))
        li.add(Node('a'))
        self.assertTrue(li.ispalindrome())

        li.add(Node('a'))
        self.assertFalse(li.ispalindrome())

        li = Node('a')
        self.assertTrue(li.ispalindrome())


if __name__ == '__main__':
    unittest.main()

