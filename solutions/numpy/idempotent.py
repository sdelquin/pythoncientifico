A = np.array([[25, -20], [30, -24]])
B = np.array([[4, -3], [2, -1]])
C = np.array([[3, -1], [6, -2]])

print('A idempotente? ->', np.array_equal(A, np.dot(A, A)))
print('B idempotente? ->', np.array_equal(B, np.dot(B, B)))
print('C idempotente? ->', np.array_equal(C, np.dot(C, C)))
