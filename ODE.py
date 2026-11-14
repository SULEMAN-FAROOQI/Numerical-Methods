import numpy as np

f = lambda w: 2 - 0.4 * w          # dw/dt = 2 - 0.4 w
h, steps = 0.5, 4

euler = [0.0]; modified = [0.0]
for n in range(steps):
    euler.append(euler[-1] + h * f(euler[-1]))
    p = modified[-1] + h * f(modified[-1])                       # predictor
    modified.append(modified[-1] + h / 2 * (f(modified[-1]) + f(p)))   # corrector

t = np.arange(0, 2.01, h)
exact = 5 * (1 - np.exp(-0.4 * t))
print('t       ', t)
print('Euler   ', np.round(euler, 4))
print('Modified', np.round(modified, 4))
print('Exact   ', np.round(exact, 4))