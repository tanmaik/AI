from colorama import init, Back, Fore
init()
import sys
import re


s = sys.argv[2]
reg = sys.argv[1]
reg = reg[1:]
flags = reg[reg.index("/")+1:]
reg = reg[:reg.index("/")]


for index, char in enumerate(flags):
    if index == 0: 
        if char == "s":
            f = re.S
        if char == "i":
            f = re.I
        if char == "m":
            f = re.M
    else:
        if char == "s":
            f = f | re.S
        if char == "i":
            f = f | re.I
        if char == "m":
            f = f | re.M

if flags:
    exp = re.compile(reg, f)
else:
    exp = re.compile(reg)

matches_list = []

for result in exp.finditer(s):
    # print("This regex:", result.re)
    # print("Searched in this string:")
    # print(result.string)
    # print("And found a match from index", result.start(), "to index", result.end(), "that looks like this:")
    # print(result[0])
    # for index in range(result.start(), result.end()):
    matches_list.append(result.span())
    # matches_list.append(result.start())
    # matches_list.append(result.end()-1)
    # print("Here are the start and end indices as a tuple:", result.span())
    # print()

highlighted = ""
current_color = Back.LIGHTBLUE_EX
for index, match in enumerate(matches_list):
    if index != 0 and matches_list[index-1][1] == match[0]:
        if current_color == Back.LIGHTBLUE_EX:
            current_color = Back.LIGHTGREEN_EX
        else:
            current_color = Back.LIGHTBLUE_EX
        highlighted += (current_color + s[match[0]:match[1]] + Back.RESET)
    else:
        if index == 0:
            highlighted += (s[:match[0]] + current_color + s[match[0]:match[1]] + Back.RESET)
        else:
            highlighted += (s[matches_list[index-1][1]:match[0]] + current_color + s[match[0]:match[1]] + Back.RESET)

highlighted += s[matches_list[len(matches_list)-1][1]:]

print(highlighted)