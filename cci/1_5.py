def one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    edited = False
    i1 = i2 = 0
    while (i1 < len(s1)) and (i2 < len(s2)):
        if s1[i1] != s2[i2]:
            if edited:
                return False
            else:
                if len(s1) < len(s2):  # insert
                    i2 += 1
                elif len(s1) > len(s2):  # remove
                    i1 += 1
                else:  # replace
                    i1 += 1
                    i2 += 1
                edited = True
        else:
            i1 += 1
            i2 += 1
    return True


import unittest
class TestCase(unittest.TestCase):
    def test_one_away(self):
        self.assertTrue(one_away('pale', 'ple'))
        self.assertTrue(one_away('pales', 'pale'))
        self.assertTrue(one_away('pale', 'bale'))
        self.assertFalse(one_away('pale', 'bake'))
        self.assertTrue(one_away('', 'a'))
        self.assertTrue(one_away('a', ''))
        self.assertTrue(one_away('a', 'b'))


if __name__ == '__main__':
    unittest.main()
