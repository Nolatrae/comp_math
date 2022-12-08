import slau as s
from copy import deepcopy


def union(mat):
    mat = deepcopy(mat)
    res = []
    for i in range(len(mat)):
        res += [mat[i][-1]]
        mat[i][-1] = 1
    return mat, res


def equation_of_the_line(mat):
    mat, res = union(mat)
    return s.inverse_slau(mat, res)


def line_interpolation(mat):
    equation_line = equation_of_the_line(mat)
    x = min(mat[1][0], mat[0][0]) + \
        (max(mat[1][0], mat[0][0]) - min(mat[1][0], mat[0][0])) / 2
    res = [x, x * equation_line[0] + equation_line[-1]]
    return res


def line_extrapolation(mat, delt=3):
    equation_line = equation_of_the_line(mat)
    x = min(mat[1][0], mat[0][0]) - delt
    res = [x, x * equation_line[0] + equation_line[-1]]
    return res


def piecemeal(data_xy, delt=3):
    coordinates = []
    for coord_line_x in range(len(data_xy) - 1):
        copy_xy = [elem[:] for elem in data_xy]
        mat = copy_xy[coord_line_x:coord_line_x + 2]
        if coord_line_x == 0:
            coordinates += [line_extrapolation(mat, delt=delt)]
        coordinates += [line_interpolation(mat)]
        if coord_line_x == len(data_xy) - 2:
            coordinates += [line_extrapolation(mat, delt=-delt)]
    return coordinates


def base_polinom(data_xy, x, i):
    m = 1
    for j in range(len(data_xy)):
        if j != i:
            m = (x - data_xy[j][0]) / (data_xy[i][0] - data_xy[j][0]) * m
    return m


def lagrange_polinom(data_xy, x):
    s = 0
    for i in range(len(data_xy)):
        s = data_xy[i][1] * base_polinom(data_xy, x, i) + s
    return s
