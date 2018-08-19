def fbtw(number):
    firstzerocnt = lastzerocnt = curmax = 0
    for i in range(number.bit_length()):
        if (number & (1 << i)) == 0:
            curval = i - firstzerocnt
            if curval > curmax:
                curmax = curval
            firstzerocnt = lastzerocnt
            lastzerocnt = i

    curval = number.bit_length() - firstzerocnt
    if curval > curmax:
        curmax = curval

    return curmax


import unittest
class TestCase(unittest.TestCase):
    def test_fbtw(self):
        self.assertEqual(8, fbtw(0b11011101111))


if __name__ == '__main__':
    unittest.main()
