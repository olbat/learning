def rotate_matrix(matrix):
    '''
    matrix = array of rows
    '''
    ret = [[None for _ in range(len(matrix))] for _ in range(len(matrix))]
    for row in range(len(matrix)):
        assert(len(matrix) == len(matrix[row]))
        for col in range(len(matrix)):
            ret[col][len(matrix) - 1 -row] = matrix[row][col]
    return ret


import unittest
class TestCase(unittest.TestCase):
    def test_rotate_matrix(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual([[7,4,1],[8,5,2],[9,6,3]], rotate_matrix(matrix))


if __name__ == '__main__':
    unittest.main()
