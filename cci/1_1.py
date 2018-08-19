def has_only_unique(s):
    seen = {}
    for c in s:
        if c in seen:
            return False
        else:
            seen[c] = True
    return True


import unittest
class TestCase(unittest.TestCase):
    def test_unique(self):
        self.assertTrue(has_only_unique('abcdefg'))

    def test_non_unique(self):
        self.assertFalse(has_only_unique('abcdefag'))


if __name__ == '__main__':
    unittest.main()
