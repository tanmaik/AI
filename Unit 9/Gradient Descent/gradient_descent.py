import numpy

x, y = 1, 1

funcA = eval("4*x**2 - 3*x*y + 2*y**2 + 24*x - 20*y")
partialAx = eval("8*x - 3*y + 24")
partialAy = eval("4 * (y - 5) - 3*x")

funcB = eval("(1 - y)**2 + (x - y**2)**2")
partialBx = eval("2 * (x - y**2)")
partialBy = eval("2 * (-2 * x * y + 2 * y ** 3 + y - 1)")

print(partialBy)