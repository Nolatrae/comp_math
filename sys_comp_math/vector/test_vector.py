import vector as v
import unittest


class test_vector(unittest.TestCase):
    def test_addition_of_vectors_1(self):
        v1 = [0, 3, 5]
        v2 = [2, 4, 7]
        responce = [2, 7, 12]
        self.assertEqual(v.addition_of_vectors(v1, v2), responce)

    def test_addition_of_vectors_2(self):
        v1 = [-3, -5, -4]
        v2 = [-1, -1, -5]
        responce = [-4, -6, -9]
        self.assertEqual(v.addition_of_vectors(v1, v2), responce)

    def test_addition_of_vectors_3(self):
        v1 = [-3.33, 5.8, -4]
        v2 = [1.28, 0, 12.34]
        responce = [-2.05, 5.8, 8.34]
        self.assertEqual(v.addition_of_vectors(v1, v2), responce)



    def test_add(self):
      a = [1, 2, 3]
      unright_v1 = ['1', 2, 3, 0]
      unright_v2 = [[1, 2], [3, 4]]

      with self.assertRaises(TypeError):
        v.addition_of_vectors(a, unright_v1)
      with self.assertRaises(TypeError):
        v.addition_of_vectors(a, unright_v2)
      with self.assertRaises(TypeError):
        v.addition_of_vectors(a, '12')
# ///////////////////////////////////////////////////////////////////

    def test_subtracting_vectors_1(self):
        v1 = [0, 3, 5]
        v2 = [2, 4, 7]
        responce = [-2, -1, -2]
        self.assertEqual(v.subtracting_vectors(v1, v2), responce)

    def test_subtracting_vectors_2(self):
        v1 = [-3, -5, -4]
        v2 = [-1, -1, -5]
        responce = [-2, -4, 1]
        self.assertEqual(v.subtracting_vectors(v1, v2), responce)

    def test_subtracting_vectors_3(self):
        v1 = [-3.33, 5.8, -4]
        v2 = [1.28, 0, 12.34]
        responce = [-4.61, 5.8, -16.34]
        self.assertEqual(v.subtracting_vectors(v1, v2), responce)

    def test_sub(self):
        a = [5, 2, 6, 4]
        unright_v1 = ['2', 8, 9, 0]
        unright_v2 = [[4, 3], [5, 4]]
        with self.assertRaises(TypeError):
          v.subtracting_vectors(a, unright_v1)
        with self.assertRaises(TypeError):
          v.subtracting_vectors(a, unright_v2)
        with self.assertRaises(TypeError):
          v.subtracting_vectors(a, '12')

# ////////////////////////////////////////////////////////////

    def test_mul_1(self):
      v1 = [0, 3, 5]
      responce = [0, 6, 10,]
      self.assertEqual(v.mul(v1, 2), responce)

    def test_mul_2(self):
      v1 = [4, 3, 5]
      responce = [13.6, 10.2, 17]
      self.assertEqual(v.mul(v1, 3.4), responce)

    def test_mul_3(self):
      v1 = [6, 1, 3]
      v2 = [13.4, 3.3, 5.4]
      responce = [80.4, 3.3, 16.2]
      self.assertEqual(v.mul(v1, v2), responce)

    def test_mul(self):
      a = [5, 1, 49, 1]

      unright_v1 = ['1', 2, 5, 0]
      unright_v2 = [True, 2, 7, 3]
      unright_v3 = [[7, 1], [9, 5]]
      unright_v4 = [9, 1, 1, 5, 16]

      with self.assertRaises(TypeError):
        v.mul(a, unright_v1)
      with self.assertRaises(TypeError):
        v.mul(a, unright_v2)
      with self.assertRaises(TypeError):
        v.mul(a, unright_v3)
      with self.assertRaises(TypeError):
        v.mul(a, '12')
      with self.assertRaises(ValueError):
        v.mul(a, unright_v4)

# //////////////////////////////

    def test_div_equal_1(self):
      v1 = [0, 3, 5]
      responce = [0, 1.5, 2.5]
      self.assertEqual(v.div(v1, 2), responce)

    def test_div_equal_2(self):
      v1 = [23, 45,76]
      responce = [6.96969696969697, 13.636363636363637, 23.03030303030303]
      self.assertEqual(v.div(v1, 3.3), responce)

    def test_div_equal_3(self):
      v1 = [44, 16, 32]
      v2 = [11, 4, 16]
      responce = [4, 4, 2]
      self.assertEqual(v.div(v1, v2), responce)

    def test_div(self):
      a = [44, 16, 32]
      unright_v1 = ['1', 2, 3]
      unright_v2 = [True, 7, 5]
      unright_v3 = [[7, 2], [4]]
      unright_v4 = [1, 5, 7, 8]

      with self.assertRaises(TypeError):
        v.div(a, unright_v1)
      with self.assertRaises(TypeError):
        v.div(a, unright_v2)
      with self.assertRaises(TypeError):
        v.div(a, unright_v3)
      with self.assertRaises(TypeError):
        v.div(a, '12')
      with self.assertRaises(ValueError):
        v.div(a, unright_v4)

# //////////////////////////////

    def test_cos_1(self):
      v1 = [1, 0, 0]
      v2 = [0, 1, 1]
      self.assertEqual(v.cos(v1, v2) , 0)

    def test_cos_2(self):
      v1 = [3, 4]
      v2 = [4, 3]
      self.assertEqual(v.cos(v1, v2), 0.96)

    def test_cos_3(self):
      v1 = [3, 4, 0]
      v2 = [4, 4, 2]
      self.assertEqual(v.cos(v1, v2), 14/15)

    def test_cos(self):
      v1 = [1, 2]
      v2 = [1, 2, 3]
      with self.assertRaises(TypeError):
        v.cos(v1, 2)
      with self.assertRaises(ValueError):
        v.cos(v1, v2)

# ///////////////////////////////

    def test_scalar_product_of_vectors_1(self):
      a = [3, 5]
      b = [-2, 7]
      self.assertEqual(v.scalar_product_of_vectors(a, b), 29)

    def test_scalar_product_of_vectors_2(self):
      a = [4, 1]
      b = [2.5, 0]
      self.assertEqual(v.scalar_product_of_vectors(a, b), 10)

    def test_scalar_equeal_3(self):
      a = [-2, -1]
      b = [0, -4]
      self.assertEqual(v.scalar_product_of_vectors(a, b), 4)

    def test_scalar(self):
      v1 = [3, 4]
      v2 = ['3', 4]
      v3 = [3, 4, 5]

      with self.assertRaises(TypeError):
        v.scalar_product_of_vectors(v1, v2)
      with self.assertRaises(ValueError):
        v.scalar_product_of_vectors(v1, v3)


if __name__ == '__main__':
    unittest.main()
