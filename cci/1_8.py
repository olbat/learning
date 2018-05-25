def zero_matrix(matrix):
    'matrix is represented by an array of rows'
    #copy = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    skiplist = set()
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if c not in skiplist:
                if matrix[r][c] == 0:
                    # set previous values to 0
                    #for i in range(c, -1, -1):
                    #    copy[r][i] = 0
                    for i in range(len(matrix[r])):
                        matrix[r][i] = 0
                    #for i in range(r, -1, -1):
                    #    copy[i][c] = 0
                    for i in range(len(matrix)):
                        matrix[i][c] = 0
                    # add column to skiplist and skip the rest of the row
                    skiplist.add(c)
                    break
                #else:
                #    copy[r][c] = matrix[r][c]
    #return copy
    return matrix


import unittest
class TestCase(unittest.TestCase):
    def test_zero_matrix(self):
        m = [[1,2,3], [4,0,5], [0,6,7]]
        self.assertEqual([[0,0,3], [0,0,0], [0,0,0]], zero_matrix(m))
        m = [[1,2,3], [4,0,5], [6,7,8]]
        self.assertEqual([[1,0,3], [0,0,0], [6,0,8]], zero_matrix(m))
        m = [[1,2,0], [3,4,5], [6,7,8]]
        self.assertEqual([[0,0,0], [3,4,0], [6,7,0]], zero_matrix(m))


if __name__ == '__main__':
    unittest.main()
