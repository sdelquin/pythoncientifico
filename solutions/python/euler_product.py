import math
from functools import reduce


def prod(k, theta):
    values = map(lambda i: math.cos(theta / math.pow(2, i)), range(1, k+1))
    return reduce(lambda x, y: x * y, values)


k = 1
theta = 30
rhs = math.sin(theta) / theta

while True:
    lhs = prod(k, theta)
    if math.isclose(lhs, rhs):
        print(f'Aproximación válida para k={k}')
        break
    k += 1
