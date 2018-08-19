def subsets(s, ret=set()):
    if s not in ret:
        ret.add(s)
    for e in s:
        s_without_e = list(s)
        s_without_e.remove(e)
        s_without_e = frozenset(s_without_e)
        if s_without_e not in ret:
            ret.add(s_without_e)
            subsets(s_without_e, ret)
    return ret


import unittest
class TestCase(unittest.TestCase):
    def test_subsets(self):
        ss = {frozenset(s) for s in
                [{}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}]}
        self.assertEqual(ss, subsets(frozenset([1,2,3])))


if __name__ == '__main__':
    unittest.main()
