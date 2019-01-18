# O(NxN)
import unittest

def rotate_matrix(matrix):
    new_matrix = []
    dim = len(matrix)

    for new_matrix_index in range(dim):
        new_matrix_column = []
        for old_matrix_index in reversed(range(dim)):
            new_matrix_column.append(matrix[old_matrix_index][new_matrix_index])
        new_matrix.append(new_matrix_column)

    return new_matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()