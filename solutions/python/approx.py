def factorial(h):
    result = 1
    for i in range(2, h+1):
        result *= i
    return result

x = 4
n = 100

approx = 0
for i in range(0, n+1):
    approx += (x**i / factorial(i))

approx - math.exp(x)
