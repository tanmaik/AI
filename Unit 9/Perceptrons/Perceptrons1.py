import ast
import sys

n = int(sys.argv[1])
w = ast.literal_eval(sys.argv[2])
b = float(sys.argv[3])


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

print(check(n, w, b))
