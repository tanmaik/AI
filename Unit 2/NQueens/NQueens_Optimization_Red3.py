from copy import copy
import time
import random

def incremental(state):
    while not test_solution(state):
        worst_queen = find_worst_queen(state)
        best_spot = find_best_column(state, worst_queen)
        state[worst_queen] = best_spot
    return state
        
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
    return sum([get_conflicts(state, i) for i in range(len(state))])

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
    r = size % 6
    if r == 2:
        even = []
        odd = []
        place = 1
        for i in range(0, int(size/2)):
            even.append(place)
            place += 2
        place = 0
        for i in range(int(size/2), size):
            if place == 0:
                odd.append(2)
            elif place == 2:
                odd.append(0)
            elif place != 4: 
                odd.append(place)
            place += 2
        return even + odd + [5]
    elif r == 3:
        even = []
        odd = []
        place = 1
        for i in range(0, int(size/2)):
            if place != 1:
                even.append(place)
            place += 2
        place = 0
        for i in range(int(size/2), size):
            if place != 0 and place != 2:
                odd.append(place)
            place += 2
        return even + [1] + odd + [0, 2]
    else:
        even = []
        odd = []
        place = 1
        for i in range(0, int(size/2)):
            even.append(place)
            place += 2
        place = 0
        for i in range(int(size/2), size):
            odd.append(place)
            place += 2
        return even + odd

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
i = 8
solution_list = []
while time.perf_counter() - start < 30 and i < 200:
    solution_list.append(incremental(create_board(i)))
    i += 1


def test_solutions(solution_list):
    for elem in solution_list:
        if not test_solution(elem):
            return False
    return True

print("Puzzles 8 to 200 finished and stored in the list called solution_list")
print("All puzzles verified with test_solution code and output is:", test_solutions(solution_list))
