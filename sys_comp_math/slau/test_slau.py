import unittest
import slau as s
import matrix.matrix as m


class test_slau(unittest.TestCase):

    def test_slau_GJ_1(self):
        matrix = [[2, 3, 5], [3, 7, 4], [1, 2, 2]]
        answers = [10, 3, 3]
        responce = [3.0000000000000044, -
                    2.0000000000000013,  1.999999999999999]
        self.assertEqual(s.slau_GJ(matrix, answers), responce)

    def test_slau_GJ_2(self):
        matrix = [[4.5, 2, 3], [1, -2, 2.5], [-5, 6, 4]]
        answers = [2.5, -4, 3]
        responce = [0.43434343434343436,
                    1.333333333333333,  -0.7070707070707068]
        self.assertEqual(s.slau_GJ(matrix, answers), responce)

    def test_slau_GJ_3(self):
        matrix = [[1, 5], [4, 5], ]
        answers = [3, 6]
        responce = [1.0, 0.4]
        self.assertEqual(s.slau_GJ(matrix, answers), responce)

    def test_slau_GJ_errors(self):
        matrix = [[5, -4], [3, -4]]
        keys = [3, 11]

        unright_1 = [['19', 5], [72, 3]]

        unright_answers_1 = [3, '5']
        unright_answers_2 = "8, 9"

        with self.assertRaises(TypeError):
            s.slau_GJ(matrix, unright_answers_1)
        with self.assertRaises(TypeError):
            s.slau_GJ(matrix, unright_answers_2)
        with self.assertRaises(TypeError):
            s.slau_GJ(unright_1, keys)

    def test_inverse_matrix_1(self):
        matrix = [[4, 5, 5], [1, 2, 3], [1, 2, 8]]
        responce = [[0.6666666666666666, -2.0, 0.33333333333333326],
                    [-0.3333333333333333, 1.7999999999999998, -0.4666666666666666], [0.0, -0.2, 0.2]]
        self.assertEqual(s.inverse(matrix), responce)

    def test_inverse_matrix_2(self):
        matrix = [[-2, -6, 2], [4, 3, -1], [-8, 3, -4]]
        responce = [[0.16666666666666674, 0.33333333333333326, 0.0], [-0.4444444444444444, -
                                                                      0.4444444444444444, -0.1111111111111111], [-0.6666666666666666, -1.0, -0.3333333333333333]]
        self.assertEqual(s.inverse(matrix), responce)


    def test_inverse_slau_errors_1(self):
        matrix = [[5, 7], [-8, 2]]
        answers = [3, 15]

        unright_matrix = [['5', 2], [2, 4]]
        unright_answers_1 = [2, '5']

        with self.assertRaises(TypeError):
            s.inverse_slau(matrix, unright_answers_1)
        with self.assertRaises(TypeError):
            s.inverse_slau(unright_matrix, answers)

    def test_inverse_slau_errors_2(self):
        matrix = [[3, 4], [2, 1]]
        unright_answers_1 = [7, 5, 9]
        unright_answers_2 = []

        with self.assertRaises(ValueError):
            s.inverse_slau(matrix, unright_answers_1)
        with self.assertRaises(ValueError):
            s.inverse_slau(matrix, unright_answers_2)

    def test_union(self):
        info = [[2, 5], [6, 9]]
        responce = [[2, 1], [6, 1]], [5, 9]
        self.assertEqual(s.union(info), (responce))

    def test_MNK_with_2_sys(self):
        info = [[2, 4], [3, 9]]
        responce = 2.69
        self.assertEqual(round(s.MNK(info)[0], 2), responce)

    def test_MNK_with_3_sys(self):
        info = [[2, 3, 7], [3, 3, 7], [4, 7, 3]]
        responce = [4.68, -2.06]
        self.assertEqual([round(item, 2) for item in s.MNK(info)], responce)


if __name__ == '__main__':
    unittest.main()
