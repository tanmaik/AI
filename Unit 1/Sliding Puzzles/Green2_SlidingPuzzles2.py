import sys
import time
from collections import deque
import math
from heapq import heappush, heappop, heapify
import copy

# SEARCH ALGORITHMS
def BFS(start_node):
    fringe = deque()
    visited = {start_node}
    fringe.append((start_node, 0, None))
    goal_node = find_goal(start_node)
    while fringe:
        v = fringe.popleft()
        if v[0] == goal_node:
            return v
        for c in get_children(v[0]):
            if c not in visited:
                fringe.append((c, v[1] + 1, v))
                visited.add(c)
    return None
def kDFS(start_node, k):
    fringe = []
    fringe.append((start_node, 0, {start_node}))
    while fringe:
        v = fringe.pop()
        if goal_test(v[0]):
            return v
        if v[1] < k:
            for c in get_children(v[0]):
                if c not in v[2]:
                    old_set = v[2].copy()
                    old_set.add(c)
                    temp = (c, v[1] + 1, old_set)
                    fringe.append(temp)
    return None
def ID_DFS(start_node):
    max_depth = 0
    result = None
    while not result:
        result = kDFS(start_node, max_depth)
        max_depth += 1
    return result
def a_star(start_state):
    closed = set()
    fringe = []
    heappush(fringe, (taxicab(start_state), 0, start_state))
    while fringe:
        v = heappop(fringe)
        if goal_test(v[2]):
            return (v[2], v[1], v[0])
        if v[2] not in closed:
            closed.add(v[2])
            for c in get_children(v[2]):
                temp = (v[1] + 1 + taxicab(c), v[1] + 1, c)
                heappush(fringe, temp)
    return None

# BOARD MOVING
def up(puzzle):
    modified_puzzle = puzzle[2:]
    size = int(puzzle[0])
    arr = [x for x in modified_puzzle]
    index = arr.index(".")
    temp = arr[index - size]
    arr[index - size] = "."
    arr[index] = temp
    modified_puzzle = str(size) + " "
    for elem in arr:
        modified_puzzle += elem
    return modified_puzzle
def down(puzzle):
    modified_puzzle = puzzle[2:]
    size = int(puzzle[0])
    arr = [x for x in modified_puzzle]
    index = arr.index(".")
    temp = arr[index + size]
    arr[index + size] = "."
    arr[index] = temp
    modified_puzzle = str(size) + " "
    for elem in arr:
        modified_puzzle += elem
    return modified_puzzle
def left(puzzle):
    modified_puzzle = puzzle[2:]
    size = int(puzzle[0])
    arr = [x for x in modified_puzzle]
    index = arr.index(".")
    temp = arr[index - 1]
    arr[index - 1] = "."
    arr[index] = temp
    modified_puzzle = str(size) + " "
    for elem in arr:
        modified_puzzle += elem
    return modified_puzzle
def right(puzzle):
    modified_puzzle = puzzle[2:]
    size = int(puzzle[0])
    arr = [x for x in modified_puzzle]
    index = arr.index(".")
    temp = arr[index + 1]
    arr[index + 1] = "."
    arr[index] = temp
    modified_puzzle = str(size) + " "
    for elem in arr:
        modified_puzzle += elem
    return modified_puzzle

# SUPPLEMENTARY FUNCTIONS
def get_children(puzzle):
    children = []
    size = int(puzzle[0])
    mod_puzzle = puzzle[2:]
    period_index = mod_puzzle.index(".")
    valid_moves = [True, True, True, True] #left, right, top, bottom
    if period_index % size == 0: # left
        valid_moves[0] = False
    if (period_index % size) == (size - 1): # right
        valid_moves[1] = False
    if period_index < size: # top
        valid_moves[2] = False
    if period_index >= (size ** 2 - size): # bottom
        valid_moves[3] = False
    if valid_moves[0]:
        children.append(left(puzzle))
    if valid_moves[1]:
        children.append(right(puzzle))        
    if valid_moves[2]:  
        children.append(up(puzzle))      
    if valid_moves[3]:    
        children.append(down(puzzle))
    return children
def goal_test(puzzle):
    if puzzle == find_goal(puzzle):
        return True
    else:
        return False
def print_puzzle(puzzle):
    size = int(puzzle[0])
    puzzle = puzzle[2:]
    final_puzzle = ""
    for index, char in enumerate(puzzle):
        final_puzzle += char
        if (((index + 1) % size) == 0) and index != ((size**2)-1):
            final_puzzle += "\n"
        else:
            final_puzzle += " "
    return final_puzzle
def find_goal(puzzle):
    goal_puzzle = ""
    puzzle = puzzle[2:]
    for char in puzzle:
        if char.isalpha() or char.isdigit():
            goal_puzzle += char
    goal_puzzle = ''.join(sorted(goal_puzzle))
    goal_puzzle += '.'
    length = str(int(math.sqrt((len(goal_puzzle)))))
    goal_puzzle = length + " " + goal_puzzle
    return goal_puzzle
def print_path(v):
    print_order = []
    print_order.append(v[0])
    while v != None:
        v = v[2]
        if v != None:
            print_order.append(v[0])
    path_length = len(print_order) - 1
    print_order = print_order[::-1]
    path = "\n"
    for index, elem in enumerate(print_order):
        path += ("State %s: \n" % index) + (print_puzzle(elem))
        path += ("\n\n")
    return (path, path_length)
def solvable(puzzle):
    size = int(puzzle[:2])
    old_puzzle = puzzle[2:]
    dot = old_puzzle.index('.')
    puzzle = old_puzzle[:dot] + old_puzzle[dot+1:]
    unordered_pairs = 0
    for index, char in enumerate(puzzle):
        for i in range(index, len(puzzle)):
            if char == '.' or puzzle[i] == '.':
                continue
            if char > puzzle[i]:
                unordered_pairs += 1
    if size % 2 != 0:
        if unordered_pairs % 2 == 0:
            return True
        else:
            return False
    else:
        if dot < size or (size * 2 < dot < (size * 2) + (size -  1)):
            if unordered_pairs % 2 != 0:
                return True
            else:
                return False
        else:
            if unordered_pairs % 2 == 0:
                return True
            else:
                return False
def print_for_submission():
    for index, puzzle in enumerate(line_list):
        time0 = time.perf_counter()
        search_method = puzzle[-1]
        puzzle = puzzle[:len(puzzle)-2]
        if solvable(puzzle):
            start = time.perf_counter()
            if search_method == 'B':
                path_length = BFS(puzzle)[1]
                end = time.perf_counter()
                time_taken = end - start
                print(f"Line {index}: {puzzle[2:]}, BFS - {path_length} moves in {time_taken} seconds\n")  
            elif search_method == 'I':
                path_length = ID_DFS(puzzle)[1]
                end = time.perf_counter()
                time_taken = end - start
                print(f"Line {index}: {puzzle[2:]}, ID-DFS - {path_length} moves in {time_taken} seconds\n")
            elif search_method == 'A':
                path_length = a_star(puzzle)[1]
                end = time.perf_counter()
                time_taken = end - start
                print(f"Line {index}: {puzzle[2:]}, A* - {path_length} moves in {time_taken} seconds\n")
            elif search_method == '!':
                path_length = BFS(puzzle)[1]
                end = time.perf_counter()
                time_taken = end - start
                print(f"Line {index}: {puzzle[2:]}, BFS - {path_length} moves in {time_taken} seconds")
                start1 = time.perf_counter()
                path_length = ID_DFS(puzzle)[1]
                end1 = time.perf_counter()
                time_taken = end1 - start1
                print(f"Line {index}: {puzzle[2:]}, ID-DFS - {path_length} moves in {time_taken} seconds")
                start2 = time.perf_counter()
                path_length = a_star(puzzle)[1]
                end2 = time.perf_counter()
                time_taken = end2 - start2
                print(f"Line {index}: {puzzle[2:]}, A* - {path_length} moves in {time_taken} seconds\n")
        else:
            time1 = time.perf_counter()
            time_taken = time1 - time0
            print(f"Line {index}: {puzzle[2:]}, no solution determined in {time_taken} seconds\n")
def use_file(filename):
    with open(filename) as f:
        #str(int(len(line.strip())**(1/2))) + " " + 
        line_list = [line.strip() for line in f]
    return line_list
def get2d(puzzle, char):
    size = int(puzzle[0])
    puzzle = puzzle[2: ]
    try:
        index = puzzle.index(char)
    except:
        return 'No solution found!'
    count = 0
    for i in range(0, size):
        for j in range(0, size):
            if count == index:
                return [i, j]
            count += 1
def taxicab(puzzle):
    goal = find_goal(puzzle)
    moves = 0
    for char in puzzle[2: ]:
        if char == '.':
            continue
        first = get2d(puzzle, char)
        second = get2d(goal, char)
        # print(first, second)
        y_dis = int(abs(second[1] - first[1]))
        x_dis = int(abs(second[0] - first[0]))
        moves += y_dis + x_dis
    return moves

# NON-FUNCTION CODE
line_list = sys.argv[1]
print_for_submission()