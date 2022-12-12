from slau import *
from matrix import *


data_ay = [[2, 4], [3, 9]]
data = [[2, 3, 7], [3, 3, 7], [4, 7, 3]]
data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]

def lower_square_method(data):
    coefs = []
    for i in range(len(data)):
        coefs_line = []
        for j in range(len(data[i])):
            coefs_line += [data[i][j]]
        coefs += [coefs_line]

    A = []
    b = []
    for j in range(len(coefs) - 1):
        b += [0]
        for i in range(len(coefs)):
            b[-1] += coefs[i][j] * coefs[i][-1]

    for j in range(len(coefs) - 1):
        A_line = [0 for i in range(len(coefs) - 1)]
        for c in range(len(A_line)):
            for i in range(len(coefs)):
                A_line[c] += coefs[i][c] * coefs[i][j]
        A += [A_line]

    return slau(A, b)


def linear_approximation(data_xy, x):
    A = [[data_xy[i][0], 1] for i in range(len(data_xy))]
    b = [[data_xy[i][-1]] for i in range(len(data_xy))]
    A_d = mul(transponir(A), A)
    b_d = [value[0] for value in mul(transponir(A), b)]
    coefs = slau(A_d, b_d)
    return [[item, coefs[0] * item + coefs[1]] for item in x]

def polinom_approximation(coefs, x):
    A = []
    b = [[item] for item in coefs]
    for i in range(len(x)):
        A_line = []
        for j in range(len(coefs)):
            A_line = [x[i]**j] + A_line
        A += [A_line]
    y = mul(A, b)
    return  [[x[i], y[i][0]] for i in range(len(y))]


coefs = [0.13, 0.07, 1.89]
coefs_2 = [0.48, -4.8, 13.96, -7.64]
x = [1, 3, 5]

# print(lower_square_method(data))
# print(linear_approximation(data_xy, [1, 2]))
# print(polinom_approximation(coefs_2, x))
