def permutations(string, buildstr=tuple(), ret=[]):
    #ret.append(''.join(buildstr))
    #if string:
    if not string:
        ret.append(''.join(buildstr))
    else:
        for c in string:
            permutations(string.replace(c, ''), buildstr + (c,), ret)
    return ret


import unittest
class TestCase(unittest.TestCase):
    def test_permutations(self):
        self.assertEqual(sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']),
            sorted(permutations('abc')))


if __name__ == '__main__':
    unittest.main()
