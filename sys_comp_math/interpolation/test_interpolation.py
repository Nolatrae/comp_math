import unittest
import interpolation as int


class Tests_Interpolation(unittest.TestCase):

    def test_union(self):
        info = [[2, 5], [6, 9]]
        responce = [[2, 1], [6, 1]], [5, 9]
        self.assertEqual(int.union(info), (responce))

    def test_equation_of_the_line(self):
        info = [[2, 5], [6, 9]]
        responce = [1, 3]
        self.assertEqual(int.equation_of_the_line(info), responce)

    def test_line_interpolation(self):
        info = [[2, 5], [6, 9]]
        responce = [4, 7]
        self.assertEqual(int.line_interpolation(info), responce)

    def test_line_extrapolation(self):
        info = [[2, 5], [6, 9]]
        responce = [1, 4]
        self.assertEqual(int.line_extrapolation(info, 1), responce)

    def test_piecemeal(self):
        info = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
        responce = [[-2, -1], [2, 3], [3.25, 3.500000000000007], [4.75, 5.000000000000001], [6.5, 7.8000000000000025]]
        self.assertEqual(int.piecemeal(info), responce)

    def test_base_polinom(self):
        info = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
        responce = 1
        self.assertEqual(int.base_polinom(info, info[0][0], 0), responce)

    def test_lagrange_polinom(self):
        info = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
        for i in range(len(info)):
            self.assertEqual(int.lagrange_polinom(info, info[i][0]), info[i][1])




if __name__ == '__main__':
    unittest.main()