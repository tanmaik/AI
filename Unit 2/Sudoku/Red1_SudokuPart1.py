import sys
from math import sqrt
from copy import copy

def open_file(filename):
    with open(filename) as f:
        line_list = [line.strip() for line in f]
    return line_list

def csp_backtracking(state):
    if test_solution(state):
        return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var):
        temp = copy(state)
        new_state = temp[0:var] + val + temp[var + 1:]
        #print(print_puzzle(new_state))
        result = csp_backtracking(new_state)
        if result is not None: 
            return result
    return None

def get_next_unassigned_var(state):
    try: 
        return state.index('.')
    except:
        return None
    
def get_sorted_values(state, var):
    n = neighbors[var]
    allowed = copy(symbol_set)
    non_allowed = set()
    for i in n:
        if state[i] in symbol_set:
            non_allowed.add(state[i])
    for x in non_allowed:
        allowed.remove(x)
    return allowed

def test_solution(state):
    test = find_num_symbols(state) 
    for x in test:
        if test[x] != N:
            return False
    return True

def determine_variables(p):
    N = int(sqrt(len(p)))
    symbols = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbol_set = {symbols[x] for x in range(N)}
    if '.0' in str(sqrt(N)):
        return int(N), symbol_set, int(sqrt(N)), int(sqrt(N))
    subblock_width = 0
    subblock_height = 0
    for i in range(int(sqrt(N)), 0, -1):
        if N % i == 0:
            subblock_height = i
            break
    for i in range(int(sqrt(N))+1, N):
        if N % i == 0:
            subblock_width = i
            break
    return N, symbol_set, subblock_width, subblock_height

def print_puzzle(puzzle):
    s = ''
    for i in range(1, len(puzzle) + 1):
        s += puzzle[i - 1] + " "       
        if i % N == 0:
            s += "\n"
    return s

def generate_constraint_sets(puzzle, s_w, s_h):
    size = int(sqrt(len(puzzle)))
    constraint_sets = []
    for n in range(size):
        constraint_sets.append({x + n*size for x in range(size)})
    for n in range(size):
        constraint_sets.append({n + x*size for x in range(size)})
    for y in range(0, s_w):
        for x in range(0, s_h):
            toAdd = set()
            for i in range(s_w*x, s_w*x+s_w): 
                for j in range(s_h*y, s_h*y+s_h): 
                    toAdd.add(i + (j * size))
            constraint_sets.append(toAdd)
    return constraint_sets

def find_neighbors():
    constraint_sets = generate_constraint_sets(puzzle, subblock_width, subblock_height)
    neighbors = dict()
    for n in range(N**2):
        neighbors[n] = set()
        for s in constraint_sets:
            if n in s:
                temp = copy(s)
                temp.remove(n)
                for elem in temp:
                    neighbors[n].add(elem)
    return neighbors

def find_num_symbols(puzzle):
    num_symbols = {symbol : 0 for symbol in sorted(list(symbol_set))}
    for x in puzzle:
        if x in symbol_set:
            num_symbols[x] += 1
    return num_symbols


puzzles = open_file(sys.argv[1])

for index, puzzle in enumerate(puzzles):
    N, symbol_set, subblock_width, subblock_height = determine_variables(puzzle)
    neighbors = find_neighbors()
    print(csp_backtracking(puzzle))