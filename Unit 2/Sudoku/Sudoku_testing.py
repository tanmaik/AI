import sys
from math import sqrt
from copy import copy
import time

def open_file(filename):
    with open(filename) as f:
        line_list = [line.strip() for line in f]
    return line_list

def csp_backtracking_with_forward_looking(state):
    if test_solution(state): return state
    var = get_most_constrained_var(state)
    for val in get_sorted_values(state, var):
        new_state = copy(state)
        new_state[var] = val
        checked_board = forward_looking(new_state)
        if checked_board is not None:
            result = csp_backtracking_with_forward_looking(checked_board)
            if result is not None: 
                return result
    return None


def forward_looking(state):
    solved_indices = [index for index, elem in enumerate(state) if len(elem) == 1 and index not in visited]
    for elem in solved_indices:
        visited.add(elem)
    while len(solved_indices) > 0:
        index = solved_indices.pop(0)
        value = state[index]
        for n in neighbors[index]:
            if value in state[n]:
                state[n] = state[n].replace(value, "")
            if len(state[n]) == 0:
                return None
            if len(state[n]) == 1:
                if n not in visited:
                    solved_indices.append(n)
                    visited.add(n)
    return state


def get_most_constrained_var(state):
    constraints = [len(elem) for elem in state]
    for x in range(2, 30):
        try:
            return constraints.index(x)
        except:
            continue
    return None

def get_sorted_values(state, var):
    return [x for x in state[var]]

def test_solution(state):
    for var in state:
        if len(var) > 1:
            return False
    return True

def goal(state):
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

def stringToBoard(puzzle):
    board = []
    for index, char in enumerate(puzzle):
        if char != '.':
            board.append(char)
        else:
            allowed = copy(symbol_set)
            toAdd = ""
            for neighbor in neighbors[index]:
                if puzzle[neighbor] != '.' and puzzle[neighbor] in allowed:
                    allowed.remove(puzzle[neighbor])
            for q in allowed:
                toAdd += q
            board.append(toAdd)
    return board
            

puzzles = open_file(sys.argv[1])
start = time.perf_counter()

for index, puzzle in enumerate(puzzles):
    N, symbol_set, subblock_width, subblock_height = determine_variables(puzzle)
    neighbors = find_neighbors()
    state = stringToBoard(puzzle)
    visited = set()
    new_state = state.copy()
    state = forward_looking(new_state)
    s = csp_backtracking_with_forward_looking(state)
    p = ""
    for elem in s:
        p += elem
    print(print_puzzle(p))
    print(goal(p))
    visited = None


end = time.perf_counter()
print(end - start)


