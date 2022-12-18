# import math
# # from decimal import Decimal
#
# def teylor_e(n, x = 1):
#     if n == 0:
#         return 1
#     else:
#         return x ** n / math.factorial(n) + teylor_e(n - 1, x)
#
# def teylor_cos(n, x = 1):
#     if n == 0:
#         return 1
#     else:
#         return ((-1) ** n  * x ** (2 * n)) / math.factorial(2 * n) + teylor_cos(n - 1, x)
#
# def teylor_sin(n, x = 1):
#     if n == 0:
#         return x
#     else:
#         return ((-1) ** n * x ** (2 * n + 1)) / math.factorial(2 * n + 1) + teylor_sin(n - 1, x)
#
# def teylor_arcsin(n, x = 1):
#     if n == 0:
#         return x
#     else:
#         return (math.factorial(2 * n) * x ** (2 * n + 1)) / ((4 ** n) * (math.factorial(n) ** 2) * (2 * n + 1)) + teylor_arcsin(n - 1, x)
#
# def teylor_arccos(n, x=1):
#     if n == 0:
#         return x
#     else:
#         return math.pi / 2 - teylor_arcsin(n, x)

import math

def sure_tailor_rows(n, x):
    if n < 0:
        mess = f"n must be bigger then 0, not {n}"
        raise ValueError(mess)
    if type(n) != int:
        mess = f"n must be int type, not {type(n)}"
        raise TypeError(mess)
    if type(x) not in (int, float):
        mess = f"x must be int or float type, not {type(x)}"
        raise TypeError(mess)

def factorial(n):
    if n < 0:
        return 1
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def macloren_e(n, x = 1):
    sure_tailor_rows(n, x)
    if n == 0:
        return 1
    else:
        return x ** n / factorial(n) + macloren_e(n - 1, x)

def macloren_sin(n, x = 1):
    sure_tailor_rows(n, x)
    if n == 0:
        return x
    else:
        return ((-1) ** n * x ** (2 * n + 1)) / factorial(2 * n + 1) + macloren_sin(n - 1, x)

def macloren_cos(n, x = 1):
    sure_tailor_rows(n, x)
    if n == 0:
        return 1
    else:
        return ((-1) ** n  * x ** (2 * n)) / factorial(2 * n) + macloren_cos(n - 1, x)

def macloren_arcsin(n, x = 1):
    sure_tailor_rows(n, x)
    if n == 0:
        return x
    else:
        return (factorial(2 * n) * x ** (2 * n + 1)) / ((4 ** n) * (factorial(n) ** 2) * (2 * n + 1)) + macloren_arcsin(n - 1, x)

def macloren_arccos(n, x = 1):
    sure_tailor_rows(n, x)
    if n == 0:
        return x
    else:
        return math.pi / 2 - macloren_arcsin(n, x)