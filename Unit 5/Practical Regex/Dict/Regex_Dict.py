import re
import sys

with open(sys.argv[1]) as f:
    dictionary = [line.strip().lower() for line in f]

# 1
matches = []
pattern = r"^(?=\w*a)(?=\w*e)(?=\w*i)(?=\w*o)(?=\w*u)\w*$"
print(f"#1 re.compile({pattern}, re.I)")
exp = re.compile(pattern, re.I)

for word in dictionary: 
    for result in exp.finditer(word):
        if len(result[0]) != 0:
            matches.append(result[0])

min_length = 111110

for match in matches:
    if len(match) < min_length:
        min_length = len(match)
    
final_matches = []
for word in matches:
    if len(word) == min_length:
        final_matches.append(word)

print(str(len(final_matches)) + " total matches")
for index, word in enumerate(final_matches):
    if index == 5:
        break
    else:
        print(word)
print()

# 2
matches = []
pattern = r"^([bcdfghjklmnpqrstvwxyz]*[aeiou]){5}[bcdfghjklmnpqrstvwxyz]*$"
print(f"#2 re.compile({pattern}, re.I)")
exp = re.compile(pattern, re.I)

for word in dictionary: 
    for result in exp.finditer(word):
        if len(result[0]) != 0:
            matches.append(result[0])
max_length = 0
for match in matches:
    if len(match) > max_length:
        max_length = len(match)
    
final_matches = []
for word in matches:
    if len(word) == max_length:
        final_matches.append(word)

print(str(len(final_matches)) + " total matches")
for index, word in enumerate(final_matches):
    if index == 5:
        break
    else:
        print(word)
print()

# 3
matches = []
pattern = r"^(\w)((?!\1)\w)*\1$"
print(f"#3 re.compile({pattern}, re.I)")
exp = re.compile(pattern, re.I)

for word in dictionary: 
    for result in exp.finditer(word):
        if len(result[0]) != 0:
            matches.append(result[0])
max_length = 0
for match in matches:
    if len(match) > max_length:
        max_length = len(match)
    
final_matches = []
for word in matches:
    if len(word) == max_length:
        final_matches.append(word)

print(str(len(final_matches)) + " total matches")
for index, word in enumerate(final_matches):
    if index == 5:
        break
    else:
        print(word)
print()

# 4
matches = []
pattern = r"^(?=(\w)(\w)(\w))\w*(?=\3\2\1$)\w*"
print(f"#4 re.compile({pattern}, re.I)")
exp = re.compile(pattern, re.I)

for word in dictionary: 
    for result in exp.finditer(word):
        if len(result[0]) != 0:
            matches.append(result[0])

print(str(len(matches)) + " total matches")

for index, word in enumerate(matches):
    if index == 5:
        break
    else:
        print(word)
print()

# 5
matches = []
pattern = r"^[^bt]*(bt|tb)[^bt]*$"
print(f"#5 re.compile({pattern}, re.I)")
exp = re.compile(pattern, re.I)

for word in dictionary: 
    for result in exp.finditer(word):
        if len(result[0]) != 0:
            matches.append(result[0])

print(str(len(matches)) + " total matches")

for index, word in enumerate(matches):
    if index == 5:
        break
    else:
        print(word)
print()



# 6
for x in range(1, 1001001010120):
    matches = []
    pattern = r"^\w*(\w)\1{" + str(x) + r"}\w*$"
    # print(f"#1 re.compile({pattern}, re.I)")
    exp = re.compile(pattern, re.I)

    for word in dictionary: 
        for result in exp.finditer(word):
            if len(result[0]) != 0:
                matches.append(result[0])
    if len(matches) == 0:
        pattern = r"^\w*(\w)\1{" + str((x - 1)) + r"}\w*$"
        print(f"#6 re.compile({pattern}, re.I)")
        exp = re.compile(pattern, re.I)
        for word in dictionary: 
            for result in exp.finditer(word):
                if len(result[0]) != 0:
                    matches.append(result[0])
        break
print(str(len(matches)) + " total matches")

for index, word in enumerate(matches):
    if index == 5:
        break
    else:
        print(word)
print()

# 7
for x in range(1, 1001001010120):
    matches = []
    pattern = r"^\w*(\w)(\w*\1){" + str(x) + r"}\w*$"
    # print(f"#1 re.compile({pattern}, re.I)")
    exp = re.compile(pattern, re.I)

    for word in dictionary: 
        for result in exp.finditer(word):
            if len(result[0]) != 0:
                matches.append(result[0])
    if len(matches) == 0:
        pattern = r"^\w*(\w)(\w*\1){" + str(x -1) + r"}\w*$"
        print(f"#7 re.compile({pattern}, re.I)")
        exp = re.compile(pattern, re.I)
        for word in dictionary: 
            for result in exp.finditer(word):
                if len(result[0]) != 0:
                    matches.append(result[0])
        break
print(str(len(matches)) + " total matches")

for index, word in enumerate(matches):
    if index == 5:
        break
    else:
        print(word)
print()

# 8
for x in range(1, 1001001010120):
    matches = []
    pattern = r"^\w*(\w\w)(\w*\1){" + str(x) + r"}\w*$"
    # print(f"#1 re.compile({pattern}, re.I)")
    exp = re.compile(pattern, re.I)

    for word in dictionary: 
        for result in exp.finditer(word):
            if len(result[0]) != 0:
                matches.append(result[0])
    if len(matches) == 0:
        pattern =  r"^\w*(\w\w)(\w*\1){" + str(x - 1) + r"}\w*$"
        print(f"#8 re.compile({pattern}, re.I)")
        exp = re.compile(pattern, re.I)
        for word in dictionary: 
            for result in exp.finditer(word):
                if len(result[0]) != 0:
                    matches.append(result[0])
        break
print(str(len(matches)) + " total matches")

for index, word in enumerate(matches):
    if index == 5:
        break
    else:
        print(word)
print()


# 9
for x in range(1, 1001001010120):
    matches = []
    pattern = r"^([aeiou]*[^aeiou]){" + str(x) + r",}[aeiou]*$"
    # print(f"#1 re.compile({pattern}, re.I)")
    exp = re.compile(pattern, re.I)

    for word in dictionary: 
        for result in exp.finditer(word):
            if len(result[0]) != 0:
                matches.append(result[0])
    if len(matches) == 0:
        pattern = r"^([aeiou]*[^aeiou]){" + str(x - 1) + r",}[aeiou]*$"
        print(f"#9 re.compile({pattern}, re.I)")
        exp = re.compile(pattern, re.I)
        for word in dictionary: 
            for result in exp.finditer(word):
                if len(result[0]) != 0:
                    matches.append(result[0])
        break
print(str(len(matches)) + " total matches")

for index, word in enumerate(matches):
    if index == 5:
        break
    else:
        print(word)
print()

# 10
matches = []
pattern = r"^((\w)(?!(\w*\2){2}))*$"
print(f"#10 re.compile({pattern}, re.I)")
exp = re.compile(pattern, re.I)

for word in dictionary: 
    for result in exp.finditer(word):
        if len(result[0]) != 0:
            matches.append(result[0])
max_length = 0
for match in matches:
    if len(match) > max_length:
        max_length = len(match)
    
final_matches = []
for word in matches:
    if len(word) == max_length:
        final_matches.append(word)

print(str(len(final_matches)) + " total matches")
for index, word in enumerate(final_matches):
    if index == 5:
        break
    else:
        print(word)
