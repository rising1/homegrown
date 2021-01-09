from unittest import TestCase

from ut import m_type


class TestMType(TestCase):

    def test_check_matrix_type(self):
        matrix = [[0, 0, 1]]
        result = m_type(matrix)
        self.assertEqual(result, [1, 3])

    def test_check_list(self):
        matrix = [0, 0, 1]
        result = m_type(matrix)
        self.assertEqual(result, [0, 3])

    def test_check_matrix(self):
        matrix = [[2.3, 5.0, 4.9, 10.25634],
                  [0, 2, 3, 125],
                  [10, 20, 30, 40]]
        result = m_type(matrix)
        self.assertEqual(result, [3, 4])