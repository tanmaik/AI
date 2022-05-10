import ast
import sys

input = ast.literal_eval(sys.argv[1])

def step(num):
    if num > 0:
        return 1
    else:
        return 0

def perceptron(A, w, b, x):
    return A(sum([i*j for i, j in zip(w, x)]) + b)

# XOR HAPPENS HERE
out3 = perceptron(step, (2, -2), -1, input)
out4 = perceptron(step, (-2, 2), -1, input)
out5 = perceptron(step, (1, 1), 0, (out3, out4))

print(out5)


