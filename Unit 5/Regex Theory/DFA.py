import sys

with open(sys.argv[1]) as f:
    dfa_spec = f.read().split("\n\n")

states = int(dfa_spec[0].split("\n")[1])
final = [int(x) for x in dfa_spec[0].split("\n")[2].split(" ")]
main_dfa = dict()
for x in range(states):
    main_dfa[x] = dict()

for i in range(1, states + 1):
    s = int(dfa_spec[i][0])
    for x in dfa_spec[i].split("\n")[1:]:
        y = x.split(" ")
        main_dfa[s][y[0]] = int(y[1])

toPrint = "*\t"
alphabet = [y for y in dfa_spec[0].split("\n")[0]]
for a in alphabet: 
    toPrint += a + "\t"
toPrint += "\n"
for state in range(states):
    toAdd = str(state) + "\t"
    for a in alphabet: 
        if a in main_dfa[state]:
            toAdd += str(main_dfa[state][a]) + "\t"
        else:
            toAdd += "_\t"
    toAdd += "\n"
    toPrint += toAdd
print(toPrint[:len(toPrint)-2])
print("Final nodes: " + str(final))

with open(sys.argv[2]) as f:
    line_list = [line.strip() for line in f]

for line in line_list:
    checkAgain = True
    state = 0
    for char in line:
        try:
            state = main_dfa[state][char]
        except:
            print(f"False {line}")
            checkAgain = False
            break
    if checkAgain:
        if state in final:
            print(f"True {line}")
        else:
            print(f"False {line}")