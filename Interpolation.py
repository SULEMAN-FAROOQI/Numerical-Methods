import numpy as np

x = np.array([10, 20, 30, 40], float)
y = np.array([62, 75, 83, 88], float)

d1 = np.diff(y); d2 = np.diff(d1); d3 = np.diff(d2)      # differences
print('first, second, third differences:', d1, d2, d3)

h = 10
p = (12 - x[0]) / h                                       # forward formula
forward = y[0] + p*d1[0] + p*(p-1)/2*d2[0] + p*(p-1)*(p-2)/6*d3[0]

p = (38 - x[-1]) / h                                      # backward formula
backward = y[-1] + p*d1[-1] + p*(p+1)/2*d2[-1] + p*(p+1)*(p+2)/6*d3[-1]
print('y(12) =', round(forward, 3))
print('y(38) =', round(backward, 3))

coef = np.polyfit(x, y, 3)                # the same cubic polynomial
print('P(x) coefficients:', coef)
print('P(12), P(38) =', np.polyval(coef, [12, 38]))