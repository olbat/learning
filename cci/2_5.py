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

    def sum(self, other):
        p1 = iter(self)
        p2 = iter(other)

        v1 = next(p1).value
        v2 = next(p2).value

        dec = 0
        carry = 0
        ret = 0
        done1 = done2 = False
        while not (done1 and done2):
            sm = v1 + v2 + carry
            carry = sm // 10
            ret += (sm % 10) * (10**dec)
            dec += 1
            if done1:
                v1 = 0
            else:
                try:
                    v1 = next(p1).value
                except StopIteration:
                    done1 = True
            if done2:
                v2 = 0
            else:
                try:
                    v2 = next(p2).value
                except StopIteration:
                    done2 = True
        return ret


import unittest
class TestCase(unittest.TestCase):
    def test_sum(self):
        l1 = Node(7)
        l1.add(1)
        l1.add(6)
        l2 = Node(5)
        l2.add(9)
        l2.add(2)
        self.assertEqual(912, l1.sum(l2))


if __name__ == '__main__':
    unittest.main()
