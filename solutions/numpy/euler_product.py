import math

import numpy as np

theta = 30
n = 20

values = np.arange(1, n, dtype='float64')
z = np.cos(theta / np.power(2, values))

lhs = np.sin(theta) / theta
rhs = np.prod(z)

print(math.isclose(lhs, rhs))
