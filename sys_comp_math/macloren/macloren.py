import math

def macloren_e(x = 1, n=1):
    sum = 0
    for i in range(n+1):
        sum += (x**i)/math.factorial(i)
    return sum


def macloren_cos(x = 1, n=1):
    sum = 0
    for i in range(n+1):
        sum += (-1)**i * x**(2*i) / math.factorial(2 * i)
    return sum


def macloren_sin(x = 1, n=1):
    sum = 0
    for i in range(n+1):
        sum += (-1)**i * x**(2*i + 1) / math.factorial(2 * i + 1)
    return sum



def macloren_arcsin(x = 1, n=1):
    sum = 0
    for i in range(n+1):
        sum += (math.factorial(2 * n) * x ** (2 * n + 1)) / ((4 ** n) * (math.factorial(n) ** 2) * (2 * n + 1))
    return sum

def macloren_arccos(x = 1, n=1):
        return math.pi / 2 - macloren_arcsin(x, n)