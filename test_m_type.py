from unittest import TestCase

from ut import m_type
from ut import m

class TestMType(TestCase):

    global matrix1, list1, matrix2

    matrix1 = [[0, 0, 1]]
    list1 = matrix1[0]
    matrix2 = [[2.3, 5.0, 4.9, 10.25634],
               [0, 2, 3, 125],
               [10, 20, 30, 40]]
    matrix3 = [[1, 1, 0]]

    def test_check_matrix_type(self):
        result = m_type(matrix1)
        self.assertEqual(result, [1, 3])

    def test_check_list(self):
        result = m_type(list1)
        self.assertEqual(result, [0, 3])

    def test_check_matrix(self):
        result = m_type(matrix2)
        self.assertEqual(result, [3, 4])

    def test_check_mDot(self):
        result = m('dot', matrix1, matrix2)
        self.assertEqual(result, [[10, 20, 30, 40]])

    def test_check_mDot(self):
        result = m('add', matrix1, matrix2)
        self.assertEqual(result, [[1, 1, 1]])
