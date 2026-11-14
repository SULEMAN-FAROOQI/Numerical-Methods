from scipy.optimize import linprog

c = [-40, -30]                  # linprog minimises, so the profit is negated
A = [[2, 1], [1, 2], [0, 1]]    # GPU time, engineer time, chatbot demand
b = [20, 16, 6]

res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')
print('x, y =', res.x, ' Z =', -res.fun)
print('slack =', res.slack)