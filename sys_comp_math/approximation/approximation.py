import slau as s
import matrix as m

sys_two = [[2, 4], [3, 9]]
sys_three = [[2, 3, 7], [3, 3, 7], [4, 7, 3]]
sys_four = [[1, 2], [3, 4], [3.5, 3], [6, 7]]

def MNK(sys_three):
    values = []
    for i in range(len(sys_three)):
        values_str = []
        for j in range(len(sys_three[i])):
            values_str += [sys_three[i][j]]
        values = [values_str] + values
    responce = []
    b = []
    for j in range(len(values) - 1):
        b += [0]
        for i in range(len(values)):
            b[-1] += values[i][j] * values[i][-1]
    for j in range(len(values) - 1):
        responce_line = [0 for i in range(len(values) - 1)]
        for c in range(len(responce_line)):
            for i in range(len(values)):
                responce_line[c] += values[i][c] * values[i][j]
        responce += [responce_line]
    return s.slau_GJ(responce, b)

def line_approximation(sys_four, x):
    A = [[sys_four[i][0], 1] for i in range(len(sys_four))]
    b = [[sys_four[i][-1]] for i in range(len(sys_four))]
    A_turn = m.mul_matrix(m.matrix_transposition(A), A)
    b_turn = [value[0] for value in m.mul_matrix(m.matrix_transposition(A), b)]
    values = s.slau_GJ(A_turn, b_turn)
    return [[item, values[0] * item + values[1]] for item in x]

def approximation_by_polinom(values, x):
    A = []
    b = [[item] for item in values]
    for i in range(len(x)):
        A_str = []
        for j in range(len(values)):
            A_str = [x[i]**j] + A_str
        A += [A_str]
    y = m.mul_matrix(A, b)
    return [[x[i], y[i][0]] for i in range(len(y))]

values = [0.48, -4.8, 13.96, -7.64]
x = [1, 3, 5]

