import math
from collections import deque

def BFS(start_node):
    fringe = deque()
    count = 0
    visited = {start_node}
    fringe.append(start_node)
    while fringe:
        v = fringe.popleft()
        print(print_puzzle(v))
        count += 1
        if goal_test(v):
            return count
        for c in get_children(v):
            if c not in visited:
                fringe.append(c)
                visited.add(c)
    return count

# actual movemenet of the game
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
    if print_puzzle(puzzle) == find_goal(puzzle):
        return True
    else:
        return False

# def change_dimension(puzzle, coordinates):
    matrix_puzzle = []
    size = int(puzzle[0:1])
    puzzle = puzzle[2:]
    count = 0
    i = 1
    index = 0
    while count != size:
        if i == 1:
            matrix_puzzle.append([])
        matrix_puzzle[count].append(puzzle[index])
        if i == size:
            count += 1
            i = 1
            index += 1
            continue
        i += 1
        index += 1
    x, y = coordinates
    x -= 1
    y -= 1
    return matrix_puzzle[y][x]

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

file_name = "/Volumes/GoogleDrive-104048612014867030298/My Drive/11th Grade/AI/Unit 1/Sliding Puzzles 1/slide_puzzle_tests.txt"
line_list = use_file(file_name)
puzzle = line_list[1]


print(BFS(puzzle))
