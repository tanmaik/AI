from matplotlib.pyplot import xkcd, xlabel
import numpy as np
import sys, ast
import math
from random import randrange

step = lambda x: 1 if x > 0 else 0
step = np.vectorize(step)

sigmoid = lambda x: 1 / (1 + ((math.e) ** -x))
sigmoid = np.vectorize(sigmoid)

def p_net(A, x, w_list, b_list):
        # vectorize A
        aL = x
        aC = None
        for L in range(1, len(w_list)):
            aC = A((aL@w_list[L]) + b_list[L])
            aL = aC
        return aC

if len(sys.argv) == 2:
    input = ast.literal_eval(sys.argv[1])

    # XOR HAPPENS HERE
    w_list = [None, np.array([[2, -2], [-2, 2]]), np.array([[1], [1]])]
    b_list = [None, np.array([[-1, -1]]), np.array([[0]])]

    output = p_net(step, np.array([list(input)]), w_list, b_list)
    print(f"XOR output for vector {input}:", output[0][0])


elif len(sys.argv) == 3:
    w_list = [None, np.array([[-1, 1, -1, 1], [-1, 1, 1, -1]]), np.array([[1], [1], [1], [1]])]
    b_list = [None, np.array([[1, 1, 1, 1]]), np.array([[-3]])]

    output = p_net(step, (float(sys.argv[1]), float(sys.argv[2])), w_list, b_list)
    if output == 1:
        print("inside")
    else:
        print("outside")

elif len(sys.argv) == 1:
    w_list = [None, np.array([[-1, 1, -1, 1], [-1, 1, 1, -1]]), np.array([[1], [1], [1], [1]])]
    b_list = [None, np.array([[1, 1, 1, 1]]), np.array([[-2.77]])]
    points = []
    for i in range(500):
        points.append((randrange(-100, 100)/100, randrange(-100, 100)/100))
    correct = 0 
    total = 0
    print("Misclassified points: ")
    for x, y in points:
        if ((x**2 + y**2)**0.5) < 1:
            calc_output = 1
        else:
            calc_output = 0
        p_output = round(p_net(sigmoid, (x, y), w_list, b_list)[0][0])
        if p_output == calc_output:
            correct += 1
        else:
            print(f"({x}, {y})")
        total += 1
    print(correct/total * 100, "%")

else:
    print("too many command lines arguments")
