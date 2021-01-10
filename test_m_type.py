from unittest import TestCase

from ut import m_type
from ut import m
from ut import times

class TestMType(TestCase):

    global matrix1, list1, matrix2, matrix3, matrix4
    global matrix5, matrix6, matrix7

    matrix1 = [[0, 0, 1]]
    list1 = matrix1[0]
    matrix2 = [[2.3, 5.0, 4.9, 10.2],
               [0, 2, 3, 125],
               [10, 20, 30, 40]]
    matrix3 = [[1, 1, 0]]
    matrix4 = [[2, 3, 4]]
    matrix5 = [[3, 3, 3]]
    matrix6 = [[1], [2]]
    matrix7 = [[2.3, 5.0, 4.9, 10.2]]



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

    def test_check_mDot2(self):
        result = m('add', matrix1, matrix3)
        self.assertEqual(result, [[1, 1, 1]])

    def test_check_mDot3(self):
        result = m('minus', matrix1, matrix3)
        self.assertEqual(result, [[1, 1, -1]])

    def test_check_mDot4(self):
        result = m('mse', matrix5, matrix4)
        self.assertEqual(result, [[9]])

    def test_check_times(self):
        result = times(2, 1, matrix4)
        self.assertEqual(result, [[4, 6, 8]])

    def test_check_mDot5(self):
        result = m('mult', matrix6, matrix7)
        self.assertEqual(result,
         [[2.3, 5.0, 4.9, 10.2], [4.6, 10.0, 9.8, 20.4]])