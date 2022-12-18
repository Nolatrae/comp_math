import slau as s
import matrix as m

def line_approximation(sys, x):
    A = [[sys[i][0], 1] for i in range(len(sys))]
    b = [[sys[i][-1]] for i in range(len(sys))]
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


