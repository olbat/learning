def count_possible_jumps(n, cache={}, jumps=(1,2,3)):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        ret = 0
        for j in jumps:
            if (n,j) not in cache:
                cache[(n,j)] = count_possible_jumps(n-j, cache, jumps)
            ret += cache[(n,j)]
        return ret



import unittest
class TestCase(unittest.TestCase):
    def test_count_possible_jumps(self):
        self.assertEqual(4, count_possible_jumps(3))


if __name__ == '__main__':
    unittest.main()
