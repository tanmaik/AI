import tqdm
import numpy

def find_next_prime(n):
    for x in range(n, 1000):
        if is_prime(x):
            return x
    return "Next prime not found"

print(find_next_prime(n))
