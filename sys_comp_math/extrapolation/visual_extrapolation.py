import unittest
import extrapolation as ap


class tester(unittest.TestCase):
    def test_lower_square_method_1_variable(self):
        data_ay = [[2, 4], [3, 9]]
        answer = 2.69
        self.assertEqual(round(ap.lower_square_method(data_ay)[0], 2), answer)

    def test_lower_square_method_2_variables(self):
        data = [[2, 3, 7], [3, 3, 7], [4, 7, 3]]
        answer = [4.68, -2.06]
        self.assertEqual([round(item, 2) for item in ap.lower_square_method(data)], answer)

    def test_linear_approximation_1_x_values(self):
        data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
        x = [4]
        answer = [[4, 4.62]]
        self.assertEqual([[round(item[0], 2), round(item[1], 2)] for item in ap.linear_approximation(data_xy, x)], answer)


    def test_linear_approximation_2_x_values(self):
        data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
        x = [2, 3]
        answer = [[2, 2.65], [3, 3.63]]
        self.assertEqual([[round(item[0], 2), round(item[1], 2)] for item in ap.linear_approximation(data_xy, x)], answer)

    def test_polinom_approximation_therd(self):
        coesf = [0.48, -4.8, 13.96, -7.64]
        x = [1, 3, 5]
        answer = [[1, 2.0], [3, 4.0], [5, 2.16]]
        self.assertEqual([[round(item[0], 2), round(item[1], 2)] for item in ap.polinom_approximation(coesf, x)], answer)

    def test_polinom_approximation_second(self):
        coesf = [0.13, 0.07, 1.89]
        x = [1, 3, 5]
        answer = [[1, 2.09], [3, 3.27], [5, 5.49]]
        self.assertEqual([[round(item[0], 2), round(item[1], 2)] for item in ap.polinom_approximation(coesf, x)], answer)

if __name__ == '__main__':
    unittest.main()
