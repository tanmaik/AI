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


# w1 * in1 + w2 * in2 + b > 0



w_list = [None, np.array([[-1, 1, -1, 1], [-1, 1, 1, -1]]), np.array([[1], [1], [1], [1]])]
b_list = [None, np.array([[1, 1, 1, 1]]), np.array([[0]])]


correct = 0 
total = 0
for xm in range(-10, 10):
    for ym in range(-10, 10):
        x = xm / 10
        y = ym / 10
        if abs(x) + abs(y) < 1:
            calc_output = 1
        else:
            calc_output = 0
        p_output = p_net(step, (x, y), w_list, b_list)
        if p_output == calc_output:
            correct += 1
        total += 1
    
print(correct/total * 100, "%")


# output = p_net(step, (0, 0), w_list, b_list)
# print(output[0][0])




