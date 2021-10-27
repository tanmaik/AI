from copy import copy
import time
import random

def incremental(state):
    while not test_solution(state):
        print(f"{state} with {sum_conflicts(state)} conflicts")
        worst_queen = find_worst_queen(state)
        best_spot = find_best_column(state, worst_queen)
        state[worst_queen] = best_spot
    if test_solution(state):
        print(state, " with 0 conflicts")
        return state
    return None
        
def find_best_column(state, var):
    temp = copy(state)
    diff_conflicts = []
    for i in range(len(temp)):
        temp[var] = i
        diff_conflicts.append(get_conflicts(temp, var))
    m = min(diff_conflicts)
    m1 = []
    for index, elem in enumerate(diff_conflicts):
        if elem == m:
            m1.append(index)
    return random.choice(m1)

def find_worst_queen(state): 
    c = [get_conflicts(state, x) for x in range(0, len(state))]
    m = max(c)
    maxs = []
    for index, elem in enumerate(c):
        if elem == m:
            maxs.append(index)
    return random.choice(maxs)

def sum_conflicts(state):
    sum = 0
    for i in range(0, len(state)):
        sum += get_conflicts(state, i)
    return sum

def get_next_unassigned_var(state):
    l = [] 
    for index, elem in enumerate(state):
        if not elem:
            l.append(index)
    return random.choice(l)

def get_sorted_values(state, var):
    non_allowed = set()
    allowed = [x for x in range(len(state))]
    vals = []
    for index, elem in enumerate(state):
        if elem is not None:
            non_allowed.add(elem)
            non_allowed.add(abs(var - index) + elem) 
            non_allowed.add(elem - abs(var - index))
    for n in non_allowed:
        if n >= 0 and n < len(state):
            allowed.remove(n)
    return allowed

def get_conflicts(state, var):
    conflicts = 0
    temp = copy(state)
    q = temp[var]
    for index, elem in enumerate(temp):
        if index != var:
            if elem == q:
                conflicts += 1
            if abs(index - var) == abs(elem - q):
                conflicts += 1
    return conflicts

def create_board(size):
    board = [None for x in range(0, size)]
    place = 1
    for i in range(0, int(size/2)):
        board[i] = place
        place += 2
    place = 0
    for i in range(int(size/2), size):
        board[i] = place
        place += 2
    return board

def test_solution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
        for compare in range(var + 1, len(state)):
            left -= 1
            right += 1
            if state[compare] == middle:
                return False
            if left >= 0 and state[compare] == left:
                return False 
            if right < len(state) and state[compare] == right:
                return False
    return True

def print_board(board):
    print("- "*len(board))
    for elem in board:
        s = ("*") * elem
        t = ("* ") * elem
        s += ("Q")
        t += ("Q ")
        q = (len(board) - len(s))
        t += ("* ") * q
        print(t)
    print("- "*len(board))


start = time.perf_counter()
for i in range(32, 34):
    print(f"{i}x{i} board: {incremental(create_board(i))}")
end = time.perf_counter()
print(f"in {end-start} seconds")
