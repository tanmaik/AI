# Back Prop
# Tanmai Kalisipudi

import numpy as np
import random
import math

epochs = 1

lamb = .1

sigmoid = lambda x: 1 / (1 + ((math.e) ** -x))
sigmoid = np.vectorize(sigmoid)

sigmoid_prime = lambda x: sigmoid(x) * (1 - sigmoid(x))
sigmoid_prime = np.vectorize(sigmoid_prime)

def back_prop(epochs, w_list, b_list, training, A, Aprime):
    for epoch in range(epochs):

        dot_list = [None for x in range(len(w_list))]
        delta_list = [None for x in range(len(w_list))]
        a_list = [None for x in range(len(w_list))]

        for x, y in training:
            a_list[0] = x
            for layer in range(1, len(w_list)):
                dot_list[layer] = a_list[layer - 1] @ w_list[layer] + b_list[layer]
                a_list[layer] = A(dot_list[layer])

            delta_list[len(delta_list) - 1] = Aprime(dot_list[len(dot_list) - 1]) * (y - a_list[len(a_list) - 1])
            
            for layer in range(len(w_list) - 2, 0, -1):
                delta_list[layer] =  Aprime(dot_list[layer]) * (delta_list[layer + 1] @ np.transpose(w_list[layer + 1]))
            
            for layer in range(1, len(w_list)):
                b_list[layer] = b_list[layer] + (lamb * delta_list[layer])
                w_list[layer] = w_list[layer] + (lamb * np.transpose(a_list[layer - 1]) * delta_list[layer])
                
            error = (1 / 2) * (np.linalg.norm(y-a_list[len(a_list) - 1]) ** 2)
            print(error)

    return w_list, b_list

w_list = [None, np.array([[1, -.5], [1, .5]]), np.array([[1, 2], [-1, -2]])]
b_list = [None, np.array([[1, -1]]), np.array([[-.5, .5]])]
training = [(np.array([[0, 0]]), np.array([[0, 0]])), (np.array([[0, 1]]), np.array([[0, 1]])), (np.array([[1, 0]]), np.array([[0, 1]])), (np.array([[1, 1]]), np.array([[1, 0]]))]

print(back_prop(100, w_list, b_list, training, sigmoid, sigmoid_prime))

