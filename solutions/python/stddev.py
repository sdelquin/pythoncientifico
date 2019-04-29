gravity = [2.8, 8.9, 9.81, 3.71, 22.9, 9.1, 7.8, 11.00]

mean, N = 0, len(gravity)
for g in gravity:
    mean += g
mean /= N

deltas = 0
for g in gravity:
    deltas += (g - mean) ** 2
deltas /= N

math.sqrt(deltas)
