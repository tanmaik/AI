def is_even(y):
    if y % 2 == 0:
        return True
    return False

# Problem 12
def hdtn(divisors):
    i = 1
    while True:
        s = sum([x for x in range(0, i+1)])
        sqrt_s = int(s**(1/2))
        count = 0
        for n in range(1, sqrt_s + 1):
            if s % n == 0:
                count += 2  
        if count > divisors:
            return s
        i += 1

print(hdtn(500))

# Problem 14
def collatz_sequence(x):
    sequence = [x]
    count = 0
    while sequence[count] != 1:
        if is_even(sequence[count]):
            sequence.append(int(sequence[count]/2))
        else:
            sequence.append(int((3*sequence[count]) + 1))
        count += 1
    return sequence

def longest_cs(max_start):
    max = {"start": 1, "length": 1}
    for i in range(2, max_start + 1):
        if max["length"] < len(collatz_sequence(i)):
            max["length"] = len(collatz_sequence(i))
            max["start"] = i
    return max["start"]

print(longest_cs(1000000))

# Problem 17
number_letter_counts = 0
ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
tens_len = sum([len(word) for word in tens])
teens_len = sum([len(word) for word in teens])
ones_len = sum([len(word) for word in ones])
one_99 = ones_len + teens_len + (tens_len*10 + (ones_len * 8))

number_letter_counts += (ones_len * 100)
number_letter_counts += (one_99 * 9)

hundreds_len = len("hundred")
number_letter_counts += (hundreds_len * 9)
and_len = len("hundredand")
number_letter_counts += (and_len * 891)
number_letter_counts += len("onethousand")
number_letter_counts += one_99

print(number_letter_counts)

# Problem 21
def find_factors(n):
    sqrt_n = int(n**(1/2))
    factors = []
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            factors.append(int(i))
            factors.append(int(n/i))
    factors.remove(n)
    return sorted(factors)

print(find_factors(24))

def sum_amicable_numbers(under):
    amicable = []
    for i in range(2, under):
        if i == sum(find_factors(sum(find_factors(i)))):
            if i != sum(find_factors(i)):
                if i not in amicable:
                    amicable.append(i)
                if sum(find_factors(i)) not in amicable:
                    amicable.append(sum(find_factors(i)))
    return sum(amicable)

print(sum_amicable_numbers(10000))

# Problem 28 
def number_spiral_diagonals(size):
    s = 1
    count = 1
    spirals = int(size / 2)
    length = spirals * 4 + 1
    added = 2
    start = 1
    while count < length:
        for i in range(4):
            start += added
            s += start
            count += 1
        added += 2
    return s

print(number_spiral_diagonals(1001))

# Problem 30
def digit_powers(x):
    arr = []
    for n in range(2, 500000):
        num = str(n)
        s = 0
        for char in num:
            s += (int(char)**x)
        if s == n:
            arr.append(n)
    return sum(arr)

print(digit_powers(5))