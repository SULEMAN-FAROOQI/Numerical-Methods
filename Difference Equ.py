e = [30.0, 20.0]
for n in range(0, 10):
    e.append((5 * e[n + 1] - e[n] + 12) / 6)      # the difference equation

formula = lambda n: 36 * 0.5 ** n - 12 * (1 / 3) ** n + 6
for n in range(11):
    print(n, round(e[n], 4), round(formula(n), 4))