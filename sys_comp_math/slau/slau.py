import matrix as m
from copy import deepcopy


def inverse(matrix):
    diagonal_mat = unit_matrix(len(matrix))
    return slau_GJ(matrix, diagonal_mat)


def inverse_slau(mat, answers):
    return m.mul_matrix(inverse(mat), answers)


def slau_GJ(matrix, answers):
    copy_mat = deepcopy(matrix)
    copy_answers = deepcopy(answers)
    changed_matrix(copy_mat, copy_answers)

    #print(copy_mat, '\t', copy_answers)
    copy_mat, copy_answers = up_back(copy_mat, copy_answers)
    # print(copy_mat)
    copy_mat, copy_answers = back_up(copy_mat, copy_answers)
    # print(copy_mat)
    return copy_answers


def up_back(mat, answers):
    answers_are_mat = m.check_mat(answers)
    for i in range(len(mat)):
        for j in range(i + 1):
            if i != j:
                if mat[i][j] != 0:
                    if mat[j][j] == 0:
                        m.change_rows(mat, i, j)
                        if answers_are_mat:
                            m.change_rows(answers, i, j)
                        else:
                            temp = answers[j]
                            answers[j] = answers[i]
                            answers[i] = temp
                    if answers_are_mat:
                        answers = m.subtraction_rows(answers, i, j, mat[i][j])
                    else:
                        answers[i] -= answers[j] * mat[i][j]
                    mat = m.subtraction_rows(mat, i, j, mat[i][j])
                    #print(mat,'\t', answers)
            else:
                if mat[i][i] == 0:
                    continue
                elif mat[i][i] != 1:
                    if answers_are_mat:
                        answers = m.multiply_row_index(
                            answers, i, 1 / mat[i][i])
                    else:
                        answers[i] /= mat[i][i]
                    mat = m.multiply_row_index(mat, i, 1 / mat[i][i])
    return mat, answers


def back_up(mat, answers):
    answers_are_mat = m.check_mat(answers)
    for i in range(len(mat) - 1, -1, -1):
        for j in range(len(mat) - 1, -1, -1):
            if i != j:
                if mat[i][j] != 0:
                    if answers_are_mat:
                        answers = m.subtraction_rows(answers, i, j, mat[i][j])
                    else:
                        answers[i] -= answers[j] * mat[i][j]
                    mat = m.subtraction_rows(mat, i, j, mat[i][j])
                    #print(mat,'\t', answers)
            else:
                if mat[i][i] != 1:
                    if answers_are_mat:
                        answers = m.multiply_row_index(
                            answers, i, 1 / mat[i][i])
                    else:
                        answers[i] /= mat[i][i]
                    mat = m.multiply_row_index(mat, i, 1 / mat[i][i])
    return mat, answers


def unit_matrix(size):
    mat = []
    for i in range(size):
        temp = []
        for j in range(size):
            if i == j:
                temp += [1]
            else:
                temp += [0]
        mat += [temp]
        temp = []
    return mat


def changed_matrix(mat, answers):
    for i in range(len(mat)):
        if mat[i][i] == 0:
            changed = False
            for j in range(len(mat)):
                if mat[j][i] != 0 and mat[i][j] != 0:
                    m.change_rows(mat, i, j)
                    temp = answers[i]
                    answers[j] = answers[i]
                    answers[i] = temp
                    changed = True
                    break