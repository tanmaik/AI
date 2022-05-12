import numpy as np
import sys

from pkg_resources import yield_lines

LEARNING_RATE = .1

x, y = 0, 0
if sys.argv[1] == "A":
    func = eval("4*x**2 - 3*x*y + 2*y**2 + 24*x - 20*y")
    partialX = eval("8*x - 3*y + 24")
    partialY = eval("4 * (y - 5) - 3*x")
else:
    func = eval("(1 - y)**2 + (x - y**2)**2")
    partialX = eval("2 * (x - y**2)")
    partialY = eval("2 * (-2 * x * y + 2 * y ** 3 + y - 1)")


if sys.argv[1] == "B":
    while np.linalg.norm(np.array([eval("2 * (x - y**2)"), eval("2 * (-2 * x * y + 2 * y ** 3 + y - 1)")])) >= (10 ** -8):
        x = x - (LEARNING_RATE * eval("2 * (x - y**2)"))
        y = y - (LEARNING_RATE * eval("2 * (-2 * x * y + 2 * y ** 3 + y - 1)"))
        partialX = eval("2 * (x - y**2)")
        partialY = eval("2 * (-2 * x * y + 2 * y ** 3 + y - 1)")
        print(f"Location: ({x}, {y}). Gradient vector: ({partialX}, {partialY})")
else:
    while np.linalg.norm(np.array([eval("8*x - 3*y + 24"), eval("4 * (y - 5) - 3*x")])) >= (10 ** -8):
        x = x - (LEARNING_RATE * eval("8*x - 3*y + 24"))
        y = y - (LEARNING_RATE * eval("4 * (y - 5) - 3*x"))
        partialX = eval("8*x - 3*y + 24")
        partialY = eval("4 * (y - 5) - 3*x")
        print(f"Location: ({x}, {y}). Gradient vector: ({partialX}, {partialY})")


print(f"\n\nFinal minimization: {x}, {y}")