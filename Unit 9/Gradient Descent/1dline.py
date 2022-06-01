from functools import partial
import math
import sys
import numpy as np
def one_d_minimize(f, left, right, tolerance):
    if right - left < tolerance:
        return (left + right) / 2
    else:
        one_third = left + (right - left) / 3
        two_third = left + ((right - left) / 3 * 2)
        if f(one_third) > f(two_third):
            return one_d_minimize(f, one_third, right, tolerance)
        else:
            return one_d_minimize(f, left, two_third, tolerance)
    

x, y = 0, 0
if sys.argv[1] == "A":
    func = lambda x, y: 4*x**2 - 3*x*y + 2*y**2 + 24*x - 20*y
    partialX = lambda x, y: 8*x - 3*y + 24
    partialY = lambda x, y: 4 * (y - 5) - 3*x
else:
    func = lambda x, y: (1 - y)**2 + (x - y**2)**2
    partialX = lambda x, y: 2 * (x - y**2)
    partialY = lambda x, y: 2 * (-2 * x * y + 2 * y ** 3 + y - 1)


while np.linalg.norm(np.array([partialX(x, y), partialY(x, y)])) >= (10 ** -8):
    def temp(lamb):
        return func(x - lamb*partialX(x,y), y - lamb*partialY(x,y))
    lamb = one_d_minimize(temp, 0, 1, 10**-8)
    x = x - (lamb * partialX(x, y))
    y = y - (lamb * partialY(x, y))
    print(f"Location: ({x}, {y}). Gradient vector: ({partialX(x,y)}, {partialY(x,y)})")


print(f"\n\nFinal minimization: {x}, {y}")