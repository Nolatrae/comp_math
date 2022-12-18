import unittest
import approximation as ap

class tester_approximation(unittest.TestCase):

    def test_line_approximation_with_1_x(self):
        info = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
        x = [4]
        responce = [[4, 4.62]]
        self.assertEqual([[round(item[0], 2), round(item[1], 2)] for item in ap.line_approximation(info, x)], responce)

    def test_line_approximation_with_2_x(self):
        info = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
        x = [2, 3]
        responce = [[2, 2.65], [3, 3.63]]
        self.assertEqual([[round(item[0], 2), round(item[1], 2)] for item in ap.line_approximation(info, x)], responce)

    def test_approximation_by_a_2_degree_polynomial(self):
        info = [0.13, 0.07, 1.89]
        x = [1, 3, 5]
        responce = [[1, 2.09], [3, 3.27], [5, 5.49]]
        self.assertEqual([[round(item[0], 2), round(item[1], 2)] for item in ap.approximation_by_polinom(info, x)], responce)

    def test_approximation_by_a_3_degree_polynomial(self):
        info = [0.48, -4.8, 13.96, -7.64]
        x = [1, 3, 5]
        responce = [[1, 2.0], [3, 4.0], [5, 2.16]]
        self.assertEqual([[round(item[0], 2), round(item[1], 2)] for item in ap.approximation_by_polinom(info, x)], responce)

if __name__ == '__main__':
    unittest.main()