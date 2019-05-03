A = {1, 3, 5, 8, 9}
B = {1, 2, 3, 6, 7, 8}
C = {3, 4, 8, 10}

lhs = A - (B & C)
rhs = (A - B) | (A - C)

if lhs == rhs:
    print(lhs)
else:
    print('Fallo del sistema!')
