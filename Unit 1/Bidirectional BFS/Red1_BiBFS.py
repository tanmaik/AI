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

def BiBFS(start_node):
    end_node = find_goal(start_node)
    start_fringe = deque()
    end_fringe = deque()
    start_checker = deque()
    end_checker = deque()
    count = 0
    start_visited = {start_node}
    end_visited = {end_node}
    start_fringe.append((start_node, count, None))
    end_fringe.append((end_node, count, None))
    start_checker.append(start_node)
    end_checker.append(end_node)
    while start_fringe and end_fringe:
        v = start_fringe.popleft()
        t = end_fringe.popleft()
        start_checker.popleft()
        end_checker.popleft()
        if v[0] == end_node:
            return [v, t]
        if t[0] == start_node:
            return [v, t]
        for c in get_children(v[0]):
            if c not in start_visited:
                start_fringe.append((c, count + 1, v))
                start_checker.append(c)
                start_visited.add(c)
                if start_checker[-1] in end_checker:
                    index = end_checker.index(start_checker[-1])
                    return [start_fringe[-1], end_fringe[index]]    
        for c in get_children(t[0]):
            if c not in end_visited:
                end_fringe.append((c, count + 1, t))
                end_visited.add(c)
                end_checker.append(c)
                if end_checker[-1] in start_checker:
                    index = start_checker.index(end_checker[-1])
                    return [start_fringe[index], end_fringe[-1]]
        # for start_elems in start_fringe:
        #     for end_elems in end_fringe:
        #         if start_elems[0] == end_elems[0]:
        #             return [start_elems, end_elems]
        count += 1
    return -1


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

def print_path_prime(v, t):
    print_order = []
    print_order.append(v[0])
    while v != None:
        v = v[2]
        if v != None:
            print_order.append(v[0])
    print_order = print_order[::-1]
    path = "\n"
    i = 0
    for elem in print_order:
        path += ("State %s: \n" % i) + (print_puzzle(elem))
        path += ("\n\n")
        i += 1
    old = print_order
    print_order = []
    while t != None:
        t = t[2]
        if t != None:
            if t[0] not in old:
                print_order.append(t[0])
    for elem in print_order:
        # if goal_test(elem) and elem in print_order:
        #     break
        path += ("State %s: \n" % i) + (print_puzzle(elem))
        path += ("\n\n")
        i += 1
    return (path, i)

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


file_name = '/Volumes/GoogleDrive-104048612014867030298/My Drive/11th Grade/AI/Unit 1/Bidirectional BFS/slide_puzzle_tests.txt'
line_list = use_file(file_name)
puzzle = line_list[8]
def print_for_submission():
    for index, puzzle in enumerate(line_list):
        start = time.perf_counter()
        solve = BiBFS(puzzle)
        path_length = print_path_prime(solve[0], solve[1])[1] - 1
        end = time.perf_counter()
        time_taken = end - start
        print(f"Line {index} with BiBFS: {puzzle[2:]}, {path_length} moves found in {time_taken} seconds")
        start = time.perf_counter()
        solve = BFS(puzzle)
        path_length = print_path(solve)[1]
        end = time.perf_counter()
        time_taken = end - start
        print(f"Line {index} with BFS: {puzzle[2:]}, {path_length} moves found in {time_taken} seconds")

print_for_submission()