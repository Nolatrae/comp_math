import macloren as mac
from matplotlib import pyplot as plt
import math

def draw_data(x, y, data_x, data_y):
    plt.ylim(ymax=max(data_y))
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.plot(data_x, data_y, color="purple")
    plt.scatter(x, y, color="orange")
    plt.grid("true")
    plt.show()

def visual_teylor_e(n, x = 0, d = 6, show_standart = True):
    y = mac.macloren_e(n, x)
    data_x = [i / 10 for i in range(x - int(d * 10), x + int(d * 10))]
    data_y = [mac.macloren_e(n, x) for x in data_x]
    if show_standart:
        plt.plot(data_x, [math.e(x) for x in data_x], color="gray", label="e")
    draw_data(x, y, data_x, data_y)

def visual_teylor_sin(n, x = 0, d = 6, show_standart = True):
    y = mac.mcaloren_sin(n, x)
    data_x = [i / 10 for i in range(x - int(d * 10), x + int(d * 10))]
    data_y = [mac.macloren_sin(n, x) for x in data_x]
    if show_standart:
        plt.plot(data_x, [math.sin(x) for x in data_x], color="gray", label="e")
    draw_data(x, y, data_x, data_y)


def visual_macloren_cos(n, x = 0, d = 6, show_standart = True):
    y = mac.macloren_sin(n, x)
    data_x = [i / 10 for i in range(x - int(d * 10), x + int(d * 10))]
    data_y = [mac.macloren(n, x) for x in data_x]
    if show_standart:
        plt.plot(data_x, [math.cos(x) for x in data_x], color="gray", label="e")
    draw_data(x, y, data_x, data_y)

def visual_macloren_arcsin(n, x = 0, d = 1.5):
    y = mac.macloren_arcsin(n, x)
    data_x = [i / 10 for i in range(x - int(d * 10), x + int(d * 10))]
    data_y = [tey.macloren_arcsin(n, x) for x in data_x]

    draw_data(x, y, data_x, data_y)

def visual_macloren_arccos(n, x = 0, d = 1.5):
    y = mac.macloren_arccos(n, x)
    data_x = [i / 10 for i in range(x - int(d * 10), x + int(d * 10))]
    data_y = [tey.macloren_arccos(n, x) for x in data_x]

    draw_data(x, y, data_x, data_y)



visual_teylor_e(2)