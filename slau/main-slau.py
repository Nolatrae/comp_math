import slau as s
import numpy as np

matrix = [
    [2, 3, 5],
    [3, 7, 4],
    [1, 2, 2]
]

matrix2 = [[4, 5, 5], [1, 2, 3], [1, 2, 8]]
answers = [
    10, 3, 3
]

matrix2 = [[5, 2], [2, 1]]
answers2 = [7, 9]

print(np.array(matrix), np.array(answers))
print()
print(s.slau_GJ(matrix, answers))
print()
print(s.inverse_slau(matrix, answers))
print()
print(np.array(s.inverse(matrix2)))
print()
print(np.array(matrix2), answers2)
print()
print(s.slau_GJ(matrix2, answers2))
print()
print(s.inverse_slau(matrix2, answers2))
print()
print(np.array(s.inverse(matrix2)))
print()

