import math
from collections import deque
import time
import sys

def BFS(start_node):
    fringe = deque()
    count = 0
    visited = {start_node}
    fringe.append((start_node, count, None))
    goal_node = find_goal(start_node)
    while fringe:
        v = fringe.popleft()
        if v[0] == goal_node:
            return v
        for c in get_children(v[0]):
            if c not in visited:
                fringe.append((c, count + 1, v))
                visited.add(c)
        count += 1
    return -1

def find_path_length(v):
    print_order = []
    print_order.append(v[0])
    while v != None:
        v = v[2]
        if v != None:
            print_order.append(v[0])
    path_length = len(print_order) - 1
    return path_length

# def BFS_hardest_puzzles(start_node):
    fringe = deque()
    count = 0
    hardest = []
    visited = {start_node}
    fringe.append((start_node, count, None))
    while fringe:
        v = fringe.popleft()
        for c in get_children(v[0]):
            if c not in visited:
                fringe.append((c, count + 1, v))
                visited.add(c)
        count += 1
    i = find_path_length(v)
    hardest.append(v)
    count = 0
    visited = {start_node}
    fringe = deque()
    fringe.append((start_node, count, None))
    while fringe:
        v = fringe.popleft()
        length = len(fringe) + 0
        for c in get_children(v[0]):
            if c not in visited:
                t = (c, count + 1, v)
                fringe.append(t)
                if find_path_length(t) == i and t not in hardest:
                    hardest.append(t)
                visited.add(c)
    return hardest

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

def use_file(filename):
    with open(filename) as f:
        line_list = [line.strip() for line in f]
    return line_list

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

file_name = '/Volumes/GoogleDrive-104048612014867030298/My Drive/11th Grade/AI/Unit 1/Sliding Puzzles/slide_puzzle_tests.txt'
line_list = use_file(file_name)

def print_for_submission():
    for index, puzzle in enumerate(line_list):
        start = time.perf_counter()
        path_length = find_path_length(BFS(puzzle))
        end = time.perf_counter()
        time_taken = end - start
        print(f"Line {index}: {puzzle[2:]}, {path_length} moves found in {time_taken} seconds")


print_for_submission()