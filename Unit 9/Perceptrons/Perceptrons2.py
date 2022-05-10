import copy
from operator import truth
import sys

bits = int(sys.argv[1])
n = int(sys.argv[2])

def truth_table(bits, n):
    size = 2 ** bits
    binaries = [('0'*(bits-len(bin(x)[2:])))+bin(x)[2:] for x in range(size)]
    binaries = binaries[::-1]
    binary_rep = '0'*(bits**2 - len(bin(n)[2:])) + bin(n)[2:]
    toReturn = []
    for index, binary in enumerate(binaries):
        b = [int(x) for x in binary]
        b = tuple(b)
        output = int(binary_rep[index])
        toAdd = (b, output)
        toReturn.append(toAdd)
    return tuple(toReturn)

def pretty_print_tt(table):
    bits = len(table[0][0])
    for point in table:
        print(*point[0], "|", point[1])

def step(num):
    if num > 0:
        return 1
    else:
        return 0

def perceptron(A, w, b, x):
    return A(sum([i*j for i, j in zip(w, x)]) + b)

def check(n, w, b):
    table = truth_table(len(w), n)
    correct = 0
    total = len(table)
    for row in table:
        p_output = perceptron(step, w, b, row[0])
        t_output = row[1]
        if p_output == t_output:
            correct += 1
    return correct / total 


def trainer(table): 
    w = [0 for x in range(bits)]
    b = 0
    initial_w = [0 for x in range(bits)]
    initial_b = 0
    for x in range(100):
        for row in table:
            p_output = perceptron(step, w, b, row[0])
            t_output = row[1]
            if p_output != t_output:
                error = t_output - p_output
                b += (t_output - p_output)
                w = [i + j for i, j in zip(w, [x * error for x in row[0]])]
        if initial_w == w and initial_b == b:
            return w, b
        initial_w = w
        initial_b = b
    return w, b

# total = 2 ** (2 ** bits)
# correct = 0
# for n in range(2 ** (2**bits)):
#     table = truth_table(bits, n)
#     w, b = trainer(table)
#     if check(n, w, b) == 1:
#         correct += 1

# print(f"{total} possible functions; {correct} can be correctly modeled.")

table = truth_table(bits, n)
w, b = trainer(table)
print(f"For the {bits}-bit #{n} Boolean function:")
print("w =", w)
print("b = ", b)
print("Accuracy:", str(check(n, w, b) * 100)+ "%")