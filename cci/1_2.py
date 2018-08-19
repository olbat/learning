from collections import defaultdict
def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    count = defaultdict(int)
    for c in s1:
        count[c] += 1
    for c in s2:
        count[c] -= 1
        if count[c] < 0:
            return False

    ## useless since no neg values => no pos ones
    #for i in count.values():
    #    if i:
    #        return False

    return True


import unittest
class TestCase(unittest.TestCase):
    def test_permutation(self):
        self.assertTrue(is_permutation('a', 'a'))
        self.assertTrue(is_permutation('abc', 'cba'))

    def test_not_permutation(self):
        self.assertFalse(is_permutation('a', 'b'))
        self.assertFalse(is_permutation('a', 'aa'))
        self.assertFalse(is_permutation('abc', 'cbd'))


if __name__ == '__main__':
    unittest.main()
