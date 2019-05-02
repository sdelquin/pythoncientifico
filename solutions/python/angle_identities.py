import math

theta = 30

# Double angle identity

lhs = math.sin(2 * theta)
rhs = 2 * math.tan(theta) / (1 + math.pow(math.tan(theta), 2))

print(math.isclose(lhs, rhs))

# Tripe angle identity

lhs = math.sin(3 * theta)
rhs = 3 * math.sin(theta) - 4 * math.pow(math.sin(theta), 3)

print(math.isclose(lhs, rhs))

# Half angle identity

lhs = math.sin(theta / 2)
rhs = math.sqrt((1 - math.cos(theta)) / 2)

print(math.isclose(lhs, rhs))
