from matplotlib import pyplot as plot
import interpolation as int
import matrix as m


def show_graph(x, y):
    plot.plot(x, y)
    plot.xlabel("X")
    plot.ylabel("Y")
    plot.grid()
    plot.show()


def get_xy(matrix_xy):
    x = m.matrix_transposition(matrix_xy)[0]
    y = m.matrix_transposition(matrix_xy)[1]
    return x, y


def plot_interpolation(data, delt=1):
    plot.title("Линейная интерполяция")
    x, y = get_xy(data)
    plot.scatter(x, y, color='blue')
    intr_point = int.line_interpolation(data)
    extr_point = int.line_extrapolation(data, delt=delt)
    plot.scatter(intr_point[0], intr_point[1], color="orange")
    plot.scatter(extr_point[0], extr_point[1], color="orange")
    show_graph(x, y)


def plot_peacemeal(data):
    plot.title("Кусочно-линейная интерполяция")
    x, y = get_xy(data)
    plot.scatter(x, y, color="blue")
    coord = int.piecemeal(data)
    in_coord = coord[1:-1]
    out_coord = [coord[0], coord[-1]]
    plot.scatter(m.matrix_transposition(in_coord)[0], m.matrix_transposition(in_coord)[1], color="blue")
    plot.scatter(m.matrix_transposition(out_coord)[0], m.matrix_transposition(out_coord)[1], color="blue")
    show_graph(x, y)


def plot_lagrange_polynom(data, delt=1):
    plot.title("Интерполяционный полином Лагранжа")
    arr_x = m.matrix_transposition(data)[0][:]
    x, y = get_xy(data)
    plot.scatter(x, y, color="blue")
    plot.axis([min(x) - 1, max(x) + delt, min(y) - delt, max(y) + delt])
    x = [i / 10 for i in range((min(arr_x) - delt) * 10, (max(arr_x) + delt) * 10 + 1)]
    y = [int.lagrange_polinom(data, x[i]) for i in range(len(x))]
    show_graph(x, y)


plot_interpolation([[2, 5], [6, 9]])
# plot_peacemeal([[1, 2], [3, 4], [3.5, 3], [6, 7]])
# plot_lagrange_polynom([[1, 2], [3, 4], [3.5, 3], [6, 7]])
