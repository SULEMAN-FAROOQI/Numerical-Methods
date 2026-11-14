import numpy as np

A = np.array([[10, 2, 1], [2, 10, 1], [1, 2, 10]], float)
b = np.array([240, 200, 150], float)

x = np.zeros(3)
for k in range(1, 20):
    old = x.copy()
    for i in range(3):
        x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
    change = np.max(abs(x - old))
    print(k, np.round(x, 4), round(change, 4))
    if change < 0.001:
        break

print('Exact solution:', np.linalg.solve(A, b))
