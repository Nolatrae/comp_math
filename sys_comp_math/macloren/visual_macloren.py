import macloren as mac
from matplotlib import pyplot as plt
import math

def draw_coord(x, y, coord_x, coord_y):
    plt.ylim(ymax=max(coord_y))
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.plot(coord_x, coord_y, color="purple")
    plt.scatter(x, y, color="orange")
    plt.grid("true")
    plt.show()

def visual_macloren_e(x = 1, n = 1, delt = 6):
    y = mac.macloren_e(x, n)
    coord_x = [i / 10 for i in range(x - int(delt * 10), x + int(delt * 10))]
    coord_y = [mac.macloren_e(x, n) for x in coord_x]
    draw_coord(x, y, coord_x, coord_y)

def visual_macloren_sin(x = 0, n = 1, delt = 6):
    y = mac.macloren_sin(x, n)
    coord_x = [i / 10 for i in range(x - int(delt * 10), x + int(delt * 10))]
    coord_y = [mac.macloren_sin(x, n) for x in coord_x]
    draw_coord(x, y, coord_x, coord_y)

def visual_macloren_cos(x = 1, n = 1, delt = 6):
    y = mac.macloren_sin(x, n)
    coord_x = [i / 10 for i in range(x - int(delt * 10), x + int(delt * 10))]
    coord_y = [mac.macloren_cos(x, n) for x in coord_x]
    draw_coord(x, y, coord_x, coord_y)

def visual_macloren_arcsin(x = 1, n = 1, delt = 1.5):
    y = mac.macloren_arcsin(x, n)
    coord_x = [i / 10 for i in range(x - int(delt * 10), x + int(delt * 10))]
    coord_y = [mac.macloren_arcsin(x, n) for x in coord_x]
    draw_coord(x, y, coord_x, coord_y)

def visual_macloren_arccos(x = 1, n=1, delt = 1.5):
    y = mac.macloren_arccos(x, n)
    coord_x = [i / 10 for i in range(x - int(delt * 10), x + int(delt * 10))]
    coord_y = [mac.macloren_arccos(x, n) for x in coord_x]
    draw_coord(x, y, coord_x, coord_y)


#visual_macloren_e(1, 5)
#visual_macloren_cos(1, 5)
#visual_macloren_sin(2, 0)
#visual_macloren_arcsin(1, 0)
#visual_macloren_arccos(1, 2)
