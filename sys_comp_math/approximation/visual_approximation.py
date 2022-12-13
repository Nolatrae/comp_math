import approximation as ap
import matplotlib.pyplot as plt

def show_graph(x, y):
    plt.plot(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()

def visual_linear_approximation(info, x):
    ax = x
    ay =[item[1] for item in ap.line_approximation(info, x)]
    x = [ap.line_approximation(info, [i])[0] for i in range(min(ax) - 10, max(ax) + 10)]
    y = [ap.line_approximation(info, x[i])[1] for i in range(len(x))]
    plt.scatter([item[0] for item in info], [item[1] for item in info], color='red')
    plt.scatter(ax, ay, color="black")
    show_graph(x, y)

visual_linear_approximation([[1, 2], [3, 4], [3.5, 3], [6, 7]], [2, 3])