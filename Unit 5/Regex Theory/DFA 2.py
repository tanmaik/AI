import sys

def print_dfa(alphabet, dictionary, final):
    toPrint = "*\t"
    # alphabet = [y for y in dfa_spec[0].split("\n")[0]]
    for a in alphabet: 
        toPrint += a + "\t"
    toPrint += "\n"
    for state in range(len(main_dfa)):
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

try:
    q_num = int(sys.argv[1])
    if q_num == 1:
        main_dfa = "ab\n4\n3\n\n0\na 1\n\n1\na 2\n\n2\nb 3\n\n3"
        main_dfa = {
            0: {
                'a': 1
            },
            1: {
                'a': 2
            },
            2: {
                'b': 3
            },
            3: {}
        }
        final = [3]
        alphabet = ['a', 'b']
    elif q_num == 2:
        main_dfa = "012\n"
    elif q_num == 3:
        main_dfa = ""
    elif q_num == 4:
        main_dfa = ""
    elif q_num == 5:
        main_dfa = ""
    elif q_num == 6:
        main_dfa = ""
    elif q_num == 7:
        main_dfa = ""
    print_dfa(alphabet, main_dfa, final)
    # dfa_spec = spec.split("\n\n")
except:
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
    print_dfa([y for y in dfa_spec[0].split("\n")[0]], main_dfa, final)

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