import math

import numpy as np

theta = 30
k = 20

values = np.arange(1, k, dtype='float64')
z = np.cos(theta / np.power(2, values))

lhs = np.sin(theta) / theta
rhs = np.prod(z)

print(math.isclose(lhs, rhs))
