from copy import copy
import time
import random

def csp_backtracking(state):
    if None not in state:
        if test_solution(state):
            return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var):
        new_state = copy(state)
        new_state[var] = val
        # print(new_state)
        result = csp_backtracking(new_state)
        if result: return result
    return None

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
    
def create_board(size):
    return [None for x in range(size)]

def test_solution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
        for compare in range(var + 1, len(state)):
            left -= 1
            right += 1
            if state[compare] == middle:
                # print(var, "middle", compare)
                return False
            if left >= 0 and state[compare] == left:
                # print(var, "left", compare)
                return False 
            if right < len(state) and state[compare] == right:
                # print(var, "right", compare)
                return False
    return True

def print_board(board):
    print("-"*len(board))
    for elem in board:
        s = ("*") * elem
        s += ("Q")
        s += ("*") * (len(board) - len(s))
        print(s)
    print("-"*len(board))

start = time.perf_counter()
for x in range(30, 45):
    print(f"{x}x{x} board:", csp_backtracking(create_board(x)))
end = time.perf_counter()
print((end-start), "seconds")
