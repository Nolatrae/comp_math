import unittest
import interpolation as int


class Tests_Interpolation(unittest.TestCase):

    def test_union(self):
        info = [[2, 5], [6, 9]]
        responce = [[2, 1], [6, 1]], [5, 9]
        self.assertEqual(int.union(info), (responce))


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