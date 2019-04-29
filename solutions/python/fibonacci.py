fibonacci = [0, 1]
n = 20
for i in range(2, n):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
fibonacci
