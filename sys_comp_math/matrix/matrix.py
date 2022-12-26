import vector
import vector as v
from copy import deepcopy


def matrix_transposition(m1):
    trans = [[m1[j][i] for j in range(len(m1))] for i in range(len(m1[0]))]
    return trans


def adding_matrices(a, b):
    copy_a = deepcopy(a)
    copy_b = deepcopy(b)
    res = []
    for i in range(len(copy_a)):
        res += [v.addition_of_vectors(copy_a[i], copy_b[i])]
    return res


def multiplying_a_matrix_by_a_scalar(m, scalar):
    copy_m = deepcopy(m)
    matrix = []
    for i in range(len(m)):
        matrix.append(v.mul(copy_m[i], scalar))
    return matrix


def mul_matrix(a, b):
    copy_mat = []
    if check_matrix(a, b):
        check_size(a, b)
        for i in range(len(a)):
                temp = []
                for c in range(len(b[i])):
                    temp += [0]
                    for j in range(len(a[i])):
                        temp[-1] += a[i][j] * b[j][c]
                copy_mat += [temp]
    return copy_mat


def multy_matrix(m1, m2):
    sum = 0
    temp = []
    res = []
    if len(m2) != len(m1[0]):
        return False
    else:
        r1 = len(m1)
        c1 = len(m1[0])
        r2 = c1
        c2 = len(m2[0])
        for z in range(0, r1):
            for j in range(0, c2):
                for i in range(0, c1):
                    sum = sum+m1[z][i]*m2[i][j]
                temp.append(sum)
                sum = 0
            res.append(temp)
            temp = []
    return res


def subtraction(a, b):
    if check_matrix(a, b):
        return adding_matrices(a, mul_matrix(b, -1))
    else:
        mat, scal = checking(a, b)
        return adding_matrices(mat, 0 - scal)


def subtraction_of_matrices(m1, m2):
    result = []
    for i in range(0, len(m1)):
        result.append(v.subtracting_vectors(m1[i], m2[i]))
    return result


def multiply_row_index(m1, index, scalar):
    check_mat(m1)
    copy_m1 = deepcopy(m1)
    copy_m1 = [[elem for elem in item] for item in copy_m1]
    for i in range(len(copy_m1[index - 1])):
        copy_m1[index][i] *= scalar
    return copy_m1


def get_row(a, index):
    return a[index]


def get_coll(a, index):
    return get_row(matrix_transposition(a), index)


def change_rows(a, row1, row2):
    copy_mat = deepcopy(a)
    temp = get_row(copy_mat, row2)
    copy_mat[row2] = copy_mat[row1]
    copy_mat[row1] = temp
    return copy_mat


def add_rows(a, row1, row2, scalar=1):
    check_mat(a)
    copy_mat = deepcopy(a)
    copy_mat[row1] = v.addition_of_vectors(
        copy_mat[row1], v.mul(get_row(copy_mat, row2), scalar))
    return copy_mat


def subtraction_rows(a, row1, row2, scalar=1):
    check_mat(a)
    copy_mat = deepcopy(a)
    copy_mat[row1] = v.subtracting_vectors(
        copy_mat[row1], v.mul(get_row(copy_mat, row2), scalar))
    return copy_mat

##################################################################################################


def check_mat(mat):
    if type(mat) != list:
        return False
    elif type(mat) == list:
        if check_cells(mat):
            return True
    else:
        raise TypeError(f"Must be not list, not {type(mat)}")


def check_cells(mat):
    for row in mat:
        if type(row) == list:
            for cell in row:
                if not (type(cell) in (int, float)):
                    mess = f"{cell} is not int or float"
                    raise TypeError(mess)
        else:
            return False
    return True


def check_matrix(mat1, mat2):
    return (check_mat(mat1) and check_mat(mat2)) or (check_mat(mat1) and v.check_vec(mat2))


def check_size(mat1, mat2):
    for row in mat1:
        if len(row) != len(mat2):
            raise ValueError("Size error")


def checking(mat, num):
    if type(mat) == list:
        if check_mat(mat) and check_cells(mat) and type(num) in (int, float):
            return mat, num
    elif type(num) == list:
        if check_mat(num) and check_cells(num) and type(mat) in (int, float):
            return num, mat
    else:
        raise TypeError("must be only list or num")
