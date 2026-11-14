import numpy as np

t = np.array([1, 2, 3, 4, 5], float)
L = np.array([6.0, 3.6, 2.2, 1.3, 0.8])
Y = np.log10(L)                      # Y = log L = A + B t
n = len(t)

B = (n * np.sum(t * Y) - t.sum() * Y.sum()) / (n * np.sum(t ** 2) - t.sum() ** 2)
A = (Y.sum() - B * t.sum()) / n
a, b = 10 ** A, 10 ** B              # L = a * b**t
print('A =', round(A, 4), ' B =', round(B, 4), ' a =', round(a, 3), ' b =', round(b, 4))

fit = a * b ** t
print('fitted:', np.round(fit, 3), ' SSE =', round(np.sum((L - fit) ** 2), 4))
print('loss at epochs 6-10:', np.round(a * b ** np.arange(6, 11), 3))
print('epoch where loss = 0.1:', round(np.log10(a / 0.1) / -B, 2))