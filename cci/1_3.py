import array

def urlify(string, sz):
    wi = len(string) - 1
    for ri in range(sz - 1, -1, -1):
        if string[ri] == ' ':
            string[wi] = '0'
            wi -= 1
            string[wi] = '2'
            wi -= 1
            string[wi] = '%'
        else:
            string[wi] = string[ri]
        wi -= 1


import unittest
class TestCase(unittest.TestCase):
    def test_urlify(self):
        s = 'Mr John Smith    '
        r = array.array('u', s)
        urlify(r, 13)
        self.assertEqual('Mr%20John%20Smith', r.tounicode())


if __name__ == '__main__':
    unittest.main()
