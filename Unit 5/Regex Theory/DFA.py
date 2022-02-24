import sys

def print_dfa(alphabet, dictionary, final):
    toPrint = "*\t"
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
        alphabet = ['0', '1', '2']
        main_dfa = {
            0: {
                '0': 0,
                '1': 1,
                '2': 0
            },
            1: {
                '0': 0,
                '1': 1,
                '2': 0
            }
        }
        final = [1]
    elif q_num == 3:
        alphabet = ['a', 'b', 'c']
        main_dfa = {
            0: {
                'a': 0,
                'b': 1,
                'c': 0
            },
            1: {  
                'a': 1,
                'b': 1,
                'c': 1
            }
        }
        final = [1]
    elif q_num == 4:
        alphabet = ['0', '1']
        main_dfa = {
            0: {
                '1': 0,
                '0': 1
            },
            1: {
                '1': 1,
                '0': 0
            }
        }
        final = [0]
    elif q_num == 5:
        alphabet = ['0', '1']
        main_dfa = {
            0: {
                '1': 2,
                '0': 1
            },
            1: {
                '1': 3,
                '0': 0
            },
            2: {
                '1': 0,
                '0': 3
            },
            3: {
                '1': 1,
                '0': 2
            }
        }
        final = [0]
    elif q_num == 6:
        alphabet = ['a', 'b', 'c']
        main_dfa = {
            0: {
                'a': 1,
                'b': 0,
                'c': 0
            },
            1: {  
                'a': 1,
                'b': 2,
                'c': 0
            },
            2: {  
                'a': 1,
                'b': 0,
                'c': 3
            },
            3: {  
            }
        }
        final = [0, 1, 2]
    elif q_num == 7:
        alphabet = ['0', '1']
        main_dfa = {
            0: {
                '1': 1,
                '0': 0
            },
            1: {
                '1': 1,
                '0': 2
            },
            2: {
                '1': 3,
                '0': 2
            },
            3: {
                '1': 4,
                '0': 2
            },
            4: {
                '1': 4,
                '0': 4
            }
        }
        final = [4]
    print_dfa(alphabet, main_dfa, final)
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