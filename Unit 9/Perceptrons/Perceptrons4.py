from matplotlib.pyplot import xkcd, xlabel
import numpy as np
import sys, ast

step = lambda elem: 1 if elem > 0 else 0
step = np.vectorize(step)
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

w_list = [None, ]
b_list = [None, ]




