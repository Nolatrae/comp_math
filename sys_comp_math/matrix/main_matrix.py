import vector as v
import matrix as m
import numpy as np


first_vector = [0, 3, 5]
second_vector = [2, 4, 7]

v3 = [1, 5, 4]
v4 = [3, 9, 1]
v5 = [2, 4, 5]

m1 = [first_vector, second_vector]
m2 = [v3, v4, v5]
m3 = [second_vector, first_vector]
print("1 матрица")
print(np.array(m1))
print("2 матрица")
print(np.array(m2))


scalar = 2
index = 1

print("Сложение матриц")  # 1
print(np.array(m.adding_matrices(m1, m2)))


print('Транспонирование матрицы')  # 3
print(np.array(m.matrix_transposition(m1)))


print('Умножение матрицы на скаляр')  # 4
print(np.array(m.multiplying_a_matrix_by_a_scalar(m1, scalar)))

print('Умножение матриц')  # 5
print(np.array(m.multy_matrix(m1, m2)))


print('Получение строки по индексу')  # 6
print(m.get_row(m1, index))

print('Получение столбца по индексу')  # 7
print(m.get_coll(m1, index))

print('Перестановка строк матрицы местами')  # 8
print(np.array(m.change_rows(m1, 1, 0)))

print('Умножение одной строки матрицы по заданному индексу на скаляр')  # 9
print(np.array(m.multiply_row_index(m1, index, scalar)))

print('Сложение строк, умноженных на число')  # 10
print(np.array(m.add_rows(m2, 1, 2, scalar)))

print('Вычитание строк строк, умноженных на число')  # 10
print(np.array(m.subtraction_rows(m2, 1, 2, scalar)))
