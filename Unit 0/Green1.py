import sys

sum = 0

# A
if sys.argv[1] == 'A':
    sum = int(sys.argv[2]) + int(sys.argv[3]) + int(sys.argv[4])
    print(sum)
    sum = 0

# B
if sys.argv[1] == 'B':
    for number in sys.argv[2:]:
        sum += int(number)
    print(sum)
    sum = 0

# C
if sys.argv[1] == 'C':
    div3 = []
    for number in sys.argv[2:]:
        if int(number) % 3 == 0:
            div3.append(int(number))
    print(div3)

# D
def fibonacci(n):
    if n <= 1:
       return n
    else:
       return(fibonacci(n-1) + fibonacci(n-2))

if sys.argv[1] == 'D':
    for i in range(int(sys.argv[2]) + 1):
        fib = fibonacci(i)
        if fib == 0:
            continue
        print(fibonacci(i))

# E
if sys.argv[1] == 'E':
    n1, n2 = int(sys.argv[2]), int(sys.argv[3]) + 1
    for i in range(n1, n2):
        value = (i**2) - (3*i) + 2
        print(value)

# F
if sys.argv[1] == 'F':
    a, b, c = float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[3])
    valid = True
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        valid = False
    if valid:
        perim = (a + b + c)/2
        area = ((perim)*(perim-a)*(perim-b)*(perim-c))**(1/2)
        print(area)
    else:
        print("Not a valid triangle")

# G
if sys.argv[1] == 'G':
    word = sys.argv[2]
    word = word.upper()
    count = 0
    vowels = {'A':0, 'E':0, 'I':0, 'O':0, 'U':0}
    for letter in word: 
        if letter == 'A':
            vowels['A'] += 1
        elif letter == 'E':
            vowels['E'] += 1
        elif letter == 'I':
            vowels['I'] += 1
        elif letter == 'O':
            vowels['O'] += 1
        elif letter == 'E':
            vowels['U'] += 1
    print(vowels)