import matrix as m
import unittest


class test_vector(unittest.TestCase):
  def test_adding_matrices_1(self):
    a = [[5, 4], [1, 4], [2, 2]]
    scalar = [[2, 4], [2, 4], [2, 4]]
    responce = [[7, 8], [3, 8], [4, 6]]
    self.assertEqual(m.adding_matrices(a, scalar), responce)

  def test_adding_matrices_2(self):
    a = [[5, 4], [1, 4], [2, 2]]
    scalar = [[-32, 4], [2, -4.5], [-2, 0]]
    responce = [[-27, 8], [3, -0.5], [0, 2]]
    self.assertEqual(m.adding_matrices(a, scalar), responce)

  def test_adding_matrices_error_1(self):
    a = [[5, 4], [1, 4], [2, 2]]
    wrong_scalar = "3"
    with self.assertRaises(TypeError):
      m.adding_matrices(a, wrong_scalar)

  def test_adding_matrices_error_2(self):
    a = [[5, 4], [1, 4], [2, 2]]
    unright_2 = [[5, 6], [8, 6], ["3", 3]]
    with self.assertRaises(TypeError):
    	m.adding_matrices(a, unright_2)

  def test_add_values_scalar_typeError_2(self):
    a = [[2, 3], [5, 3], [2, 3]]
    unright_3 = [[5, 6], [8, 6], "23"]
    with self.assertRaises(TypeError):
      m.adding_matrices(a, unright_3)

#////////////////////////////////

  def test_sub_matrices_1(self):
    a = [[5, 4], [1, 4], [2, 2]]
    scalar = [[2, 4], [2, 4], [2, 4]]
    responce = [[3, 0], [-1, 0], [0, -2]]
    self.assertEqual(m.subtraction_of_matrices(a, scalar), responce)

  def test_sub_matrices_2(self):
    a = [[5, 4], [1, 4], [2, 2]]
    scalar = [[-32, 4], [2, -4.5], [-2, 0]]
    responce = [[37, 0], [-1, 8.5], [4, 2]]
    self.assertEqual(m.subtraction_of_matrices(a, scalar), responce)

  def test_sub_error_1(self):
    a = [[5, 4], [1, 4], [2, 2]]
    wrong_scalar = "3"
    with self.assertRaises(TypeError):
      m.subtraction_of_matrices(a, wrong_scalar)

  def test_sub_error_2(self):
    a = [[5, 4], [1, 4], [2, 2]]
    unright_2 = [[5, 6], [8, 6], ["3", 3]]
    with self.assertRaises(TypeError):
    	m.subtraction_of_matrices(a, unright_2)

  def test_sub_typeError_2(self):
    a = [[2, 3], [5, 3], [2, 3]]
    unright_3 = [[5, 6], [8, 6], "23"]
    with self.assertRaises(TypeError):
      m.subtraction_of_matrices(a, unright_3)

###############################

  def test_mul_1(self):
    a = [[5, 4], [1, 4], [2, 2]]
    scalar = [[2, 4, 1], [2, 4, 5]]
    responce = [[18, 36, 25], [10, 20, 21], [8, 16, 12]]
    self.assertEqual(m.multy_matrix(a, scalar), responce)

  def test_mul_2(self):
    a = [[-22.3, -4.2, 1], [2, 4, 5]]
    scalar = [[5.5, -4.3], [-1.9, 4.2], [-2, -2.2]]
    responce = [[-116.67, 76.05], [-6.6, -2.799999999999999]]
    self.assertEqual(m.multy_matrix(a, scalar), responce)


  def test_mul_error_1(self):
    a = [[5, 4], [1, 4], [2, 2]]
    unright_2 = [[5, 6], [8, 6], ["3", 3]]
    with self.assertRaises(TypeError):
    	m.mul_matrix(a, unright_2)

  def test_mul_error_2(self):
    a = [[5, 8], [2, 9], [7, 9]]
    unright_2 = [[1, 3], ["9", 4]]
    with self.assertRaises(TypeError):
    	m.multy_matrix(a, unright_2)

  def test_mul_error_3(self):
    a = [[5, 8], [2, 9], [7, 9]]
    unright_3 = [[1, 3], "87"]
    with self.assertRaises(TypeError):
    	m.multy_matrix(a, unright_3)


################################

  def test_change_row(self):
    a = [[1, 2], [3, 4], [5, 6]]
    row_1 = 0
    row_2 = 2
    responce = [[5, 6], [3, 4], [1, 2]]
    self.assertEqual(m.change_rows(a, row_1, row_2), responce)

  def test_multiply_row_index(self):
    a = [[5, 2.5], [8, 4], [3, 5]]
    scalar = 2
    index = 0
    responce = [[10, 5], [8, 4], [3, 5]]
    self.assertEqual(m.multiply_row_index(a, index,scalar), responce)


  def test_add_rows(self):
    a = [[2, 3], [5, 4], [4, 5]]
    scalar = 2
    row_1 = 0
    row_2 = 1
    responce = [[12, 11], [5, 4], [4, 5]]
    self.assertEqual(m.add_rows(a, row_1, row_2, scalar), responce)


  def test_sub_rows(self):
    a = [[2, 3], [5, 4], [4, 5]]
    scalar = 2
    row_1 = 0
    row_2 = 1
    responce = [[-8, -5], [5, 4], [4, 5]]
    self.assertEqual(m.subtraction_rows(a, row_1, row_2, scalar), responce)

















if __name__ == '__main__':
    unittest.main()
