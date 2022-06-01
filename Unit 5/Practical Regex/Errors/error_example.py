import colorama

for x in range(len("hi")):
    print('hello')

def is_prime(n):
    # Error 3: Find erroneous = instead of ==.
    if n = 1:
        return False
    for x in range(2, n):
        if n % x = 0:
            return False
    return True

def next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n

def test_even(n):
    q = 2
    if n % q = 0:
        return True
    return False

primne = 233

# Error 2: Find function calls to variable names.
primne()
print(primne()) 

# Error 1: Find invalid variable names.
2prime = 233
2390342lkajdsflkasjdf = 3129

# Error 4: Find erroneous == instead of = .
hello == 12
fortund102 == 129

# Error 5: Find missing colons.
if True
    print('hello')

for x in range(10)
    print(x)