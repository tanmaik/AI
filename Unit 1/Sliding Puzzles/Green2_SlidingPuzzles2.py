import sys
import time
from collections import deque
import math

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
    return -1
def kDFS(start_node, k):
    fringe = []
    fringe.append((start_node, 0, {start_node}))
    while fringe:
        v = fringe.pop()
        if goal_test(v[0]):
            return v
        if v[1] < k:
            for c in get_children(v[0]):
                old_set = v[2]
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
# def find_path_length(v):
    print_order = []
    print_order.append(v[0])
    while v != None:
        v = v[2]
        if v != None:
            print_order.append(v[0])
    path_length = len(print_order) - 1
    return path_length
def get_children(puzzle):
    children = []
    size = int(puzzle[0:1])
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
        start = time.perf_counter()
        path_length = BFS(puzzle)[1]
        end = time.perf_counter()
        time_taken = end - start
        print(f"Line {index}: {puzzle[2:]}, BFS - {path_length} moves found in {time_taken} seconds")
        start1 = time.perf_counter()
        path_length = ID_DFS(puzzle)[1]
        end1 = time.perf_counter()
        time_taken = end1 - start1
        print(f"Line {index}: {puzzle[2:]}, ID-DFS - {path_length} moves found in {time_taken} seconds\n")
def use_file(filename):
    with open(filename) as f:
        #str(int(len(line.strip())**(1/2))) + " " + 
        line_list = [str(int(len(line.strip())**(1/2))) + " " + line.strip() for line in f]
    return line_list
def taxicab(puzzle):
    size = puzzle[0]
    puzzle = puzzle[2: ]
    return size

# NON-FUNCTION CODE
line_list = use_file('/Volumes/GoogleDrive-104048612014867030298/My Drive/11th Grade/AI/Unit 1/Sliding Puzzles/15_puzzles.txt')
print_for_submission()