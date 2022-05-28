import colorama

for x in range(len("hi")):
    print('hello')

def is_prime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

def next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n

def test_prime(n):
    if is_prime(n):
        print(n, 'is prime')
    else:
        print(n, 'is not prime')


primne()
test_prime(2)
print(primne())
print(test_prime(2))

primne = 233
2prime = 233
2390342lkajdsflkasjdf = 3129
