import unittest


def get_zero_entries(rows,columns, matrix):
    zero_entries = []
    for m in range(rows):
        for n in range(columns):
            if matrix[m][n] == 0:
                zero_entries.append((m, n))

    return zero_entries


def set_matrix_to_zero(matrix):

    rows = len(matrix)
    columns = len(matrix[0])

    zero_entries = get_zero_entries(rows, columns, matrix)

    for m in range(rows):
        for entry in zero_entries:
            matrix[m][entry[1]] = 0

    for m in range(columns):
        for entry in zero_entries:
            matrix[entry[0]][m] = 0

    return matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = set_matrix_to_zero(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()