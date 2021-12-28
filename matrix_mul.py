import numpy as np

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

r1, c1 = np.shape(A)
r2, c2 = np.shape(B)
print(c1 == r2)
precomputed = np.matmul(A, B)
print(precomputed)
product_matrix = np.zeros((c1, r2))
for i in range(0, r1):
    for j in range(0, c1):
        for k in range(c2):
            product_matrix[i][j] += A[i][k] * A[k][j]
print(product_matrix)
product_matrix[0][0]=0
test_out = precomputed==product_matrix
print(test_out, test_out.all())

