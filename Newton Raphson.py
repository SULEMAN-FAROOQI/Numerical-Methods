f  = lambda x: x**4 - 25*x**2 + 144      # f(x)
fp = lambda x: 4*x**3 - 50*x             # f'(x)

x = 4.5
for k in range(1, 6):
    x_new = x - f(x) / fp(x)             # Newton-Raphson formula
    print(k, round(x, 4), round(f(x), 4), round(fp(x), 4), round(x_new, 4))
    x = x_new

print('x =', round(x, 4), '  y = 12/x =', round(12 / x, 4))