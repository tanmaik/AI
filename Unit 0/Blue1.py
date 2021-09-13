import sys

def is_even(y):
    if y % 2 == 0:
        return True
    return False

def is_prime(x):
    if x == 2: 
        return True
    if x <= 1 or is_even(x):
        return False
    for n in range(2, x//2):
        if x % n == 0:
            return False
    return True

# Problem 1
print(sum([i for i in range(1000) if (i % 3 == 0) or (i % 5 == 0)]))

# Problem 2
a = 1
b = 2
f = b
s = 2
while b <= 4000000:
    f = a + b
    if is_even(f):
        s += f
    a = b
    b = f
print(s)

# Problem 3
def maxPrime(n):
    div = 2
    while div * div < n:
        while n % div == 0:
            n /= div
        div += 1
    return int(n)

print(maxPrime(600851475143))

# Problem 4
palindromes = [num1*num2 for num1 in range(100, 1000) for num2 in range(100, 1000) if str(num1*num2) == str(num1*num2)[::-1]]
print(max(palindromes))

# # Problem 5
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
    
def smallest_divisor(n):
    i = n
    while True:
        for x in range(n, 1, -1):
            if gcd(i, x) % x != 0:
                break
            if x == 2:
                return i
        i += n


print(smallest_divisor(20))


# Problem 6
print(sum([x for x in range(101)])**2 - sum([x**2 for x in range(101)]))

# Problem 7
def find_prime(kth):
    count = 0
    i = 0
    while count < kth:
        if is_prime(i):
            count += 1
            if count == kth:
                return i
        i += 1
    return i

print(find_prime(10001))

# Problem 8
def greatest_product(n, digits):
    num = str(n)
    max_prod = 1
    current_prod = 1
    for i in range(0, len(num) - digits):
        for number in num[i:i+digits]:
            current_prod = current_prod * int(number)
        if current_prod > max_prod:
            max_prod = current_prod
        current_prod = 1
    return max_prod

print(greatest_product(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450, 13))

# Problem 9
def is_pythag(a, b, c):
    if (a**2 + b**2) == c**2:
        return True
    return False

def special_pythagorean_triplet(sum):
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = sum - a - b
            if a + b + c == 1000:
                if is_pythag(a, b, c):
                    return a * b * c
    return None
          
print(special_pythagorean_triplet(1000))

# Problem 29
def distinct_powers(lower, upper):
    upper += 1
    distinct = []
    for a in range(lower, upper):
        for b in range(lower, upper):
            if not a**b in distinct:
                distinct.append(a**b)
    return len(distinct)

print(distinct_powers(2, 100))

