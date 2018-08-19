from math import ceil

#def has_magic_index(array, idx=None):
#    if idx is None:  # initial value
#        idx = len(array) // 2
#    elif (idx <= 0) or (idx >= (len(array) - 1)):  # termination condition
#        return array[idx] == idx
#
#    if array[idx] < idx:  # go right
#        return has_magic_index(array, idx + ceil(idx / 2))
#    elif array[idx] > idx:  # go left
#        return has_magic_index(array, idx - ceil(idx / 2))
#    else:
#        return True

def has_magic_index(array):
    idx = len(array) // 2
    while (idx > 0) and (idx < len(array) - 1):
        if array[idx] < idx:  # go right
            idx += ceil(idx / 2)
        elif array[idx] > idx:  # go left
            idx -= ceil(idx / 2)
        else:  # found a magic index
            return True
    return array[idx] == idx


import unittest
class TestCase(unittest.TestCase):
    def test_has_magic_index(self):
        self.assertTrue(has_magic_index([0,4,5,6]))
        self.assertTrue(has_magic_index([1,1,2,4]))
        self.assertTrue(has_magic_index([1,1,1,3]))
        self.assertTrue(has_magic_index([-1,1,5,6]))
        self.assertFalse(has_magic_index([3,4,5,6]))


if __name__ == '__main__':
    unittest.main()
