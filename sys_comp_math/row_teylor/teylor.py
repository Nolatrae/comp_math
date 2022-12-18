import math
# from decimal import Decimal

def teylor_e(x,n=1000):
    sum = 0
    for i in range(0, n+1):
        sum += 1 * (x**i)/math.factorial(i)
    return sum

def teylor_cos(x,n=1000):
    sum = 0
    for i in range(0, n+1):
        sum += ((-1) ** i) * (x**(2*i)/math.factorial(2*i))
    return sum

def teylor_sin(x,n = 1000):
    sum = 0
    for i in range(0, n+1):
        sum += ((-1) ** i) * (x**(2*i+1)/math.factorial(2*i+1))
    return sum

def teylor_arcsin(x, n=85):
    sum = 0.0
    # n = round(x)
    # x_float = float(x)
    for i in range(1, n+1):
        sum += (math.factorial(2 * i)*(x**(2 * i + 1)))/(4**i * math.factorial(i)**2) * (2 * i + 1)
        # print((math.factorial(2*i)*x**(2*i+1))/(4**i*math.factorial(i)**2)*(2*i+1))
    return sum
print(teylor_arcsin(1))
print(math.asin(1))
#
# def teylor_arccos(x,n = 1000):
#     sum = 0
#     for i in range(0, n+1):
#         sum += ((-1) ** i) * (x**(2*i)/math.factorial(2*i))
#     return sum