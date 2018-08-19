import re
from collections import defaultdict
def has_palindrome_permutation(string):
    # preprocess the string
    string = string.lower()
    string = re.sub(r'[^a-z]', '', string)

    # get the frequency of each character
    ccount = defaultdict(int)
    for c in string:
        ccount[c] += 1

    # there should be at most one odd char frequence
    had_odd = False
    for f in ccount.values():
        if (f % 2) == 1:
            if had_odd:
                return False
            else:
                had_odd = True

    return True


import unittest
class TestCase(unittest.TestCase):
    def test_has_palindrome_permutation(self):
        self.assertTrue(has_palindrome_permutation(''))
        self.assertTrue(has_palindrome_permutation('AA'))
        self.assertTrue(has_palindrome_permutation('Tact Coa'))
        self.assertTrue(has_palindrome_permutation('Tact Coa...'))

    def test_has_no_palindrome_permutation(self):
        self.assertFalse(has_palindrome_permutation('A B'))


if __name__ == '__main__':
    unittest.main()
