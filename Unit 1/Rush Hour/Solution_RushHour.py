from collections import deque

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
evens = {character for character in alphabet[::2]}
odds = {character for character in alphabet[1::2]}
cars = {character for character in alphabet[:26]}
trucks = {character for character in alphabet[26:]}

direction_to_index_shift = {"U": -8, "D": 8, "R": 1, "L": -1}

def print_puzzle(state):
    print("/------\\")
    for row in range(1, 7):
        char = "|"
        if row == 3:
            char = ">"
        print("|" + state[row*8 + 1:(row+1)*8 - 1] + char)
    print("\\------/")

def build_puzzle():
    puzzle = list("?????????      ??      ??      ??      ??      ??      ?????????")
    red = int(input("From 1 to 5, left to right, what is the left-most index of the red car? "))
    puzzle[24 + red] = "X"
    puzzle[24 + red + 1] = "X"
    print_puzzle("".join(puzzle))
    v_car, h_car, v_truck, h_truck = 0, 1, 26, 27
    while True:
        char = input("Input a size 2 car (C) or size 3 truck (T) or solve (S)? ")
        if char == "S":
            break
        elif char == "C":
            code = "C"
            size = 2
        elif char == "T":
            code = "T"
            size = 3
        else:
            continue
        char = input("Does it face up and down (U) or side to side (S)? ")
        if char == "U":
            code += "U"
            r = int(input("From 1 to 5, top to bottom, what is the top-most index of the vehicle? "))
            c = int(input("From 1 to 6, left to right, what is the index of the column of the vehicle? "))
            index = r * 8 + c
            step = 8
        elif char == "S":
            code += "S"
            r = int(input("From 1 to 6, top to bottom, what is the top-most index of the vehicle? "))
            c = int(input("From 1 to 5, left to right, what is the index of the column of the vehicle? "))
            index = r * 8 + c
            step = 1
        else:
            continue
        if code == "CU":
            character = alphabet[v_car]
            v_car += 2
        elif code == "CS":
            character = alphabet[h_car]
            h_car += 2
        elif code == "TU":
            character = alphabet[v_truck]
            v_truck += 2
        elif code == "TS":
            character = alphabet[h_truck]
            h_truck += 2
        for count in range(size):
            puzzle[index + count * step] = character
        print_puzzle("".join(puzzle))
    return "".join(puzzle)

def move(st, index, dir, dist):
    state = list(st)
    character = state[index]
    diff = direction_to_index_shift[dir]
    state[index] = " "
    state[index-diff] = " "
    if character in trucks:
        state[index - 2 * diff] = " "
    state[index + diff * dist] = character
    state[index + diff * (dist - 1)] = character
    if character in trucks:
        state[index+diff * (dist - 2)] = character
    return "".join(state)

def get_spaces(state, index, dir):
    diff = direction_to_index_shift[dir]
    total = 0
    index += diff
    while state[index] == " ":
        total += 1
        index += diff
    return total

def get_children(state):
    children = []
    for index, character in enumerate(state):
        if character in odds:
            for count in range(1, get_spaces(state, index, "L") + 1):
                children.append(move(state, index, "L", count))
            for count in range(1, get_spaces(state, index, "R") + 1):
                children.append(move(state, index, "R", count))
        if character in evens:
            for count in range(1, get_spaces(state, index, "U") + 1):
                children.append(move(state, index, "U", count))
            for count in range(1, get_spaces(state, index, "D") + 1):
                children.append(move(state, index, "D", count))
    return children

def goal_test(state):
    if state[29:31] == "XX":
        return True
    return False

def bfs_search(state):
    visited = {state}
    fringe = deque()
    fringe.append((state, ()))
    while fringe:
        position, path = fringe.popleft()
        path = path + (position, )
        if goal_test(position):
            return path
        for child in get_children(position):
            if child not in visited:
                visited.add(child)
                fringe.append((child, path))

for board, state in enumerate(bfs_search(build_puzzle())):
    print()
    print("Board number:", board)
    print_puzzle(state)
            
            