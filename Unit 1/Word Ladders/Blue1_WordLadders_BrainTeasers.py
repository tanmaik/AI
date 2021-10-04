import sys
import time
from collections import deque

def open_file(dict_file, puzzle_file):
    with open(dict_file) as f:
        line_list = [line.strip() for line in f]
    with open(puzzle_file) as f:
        puzzle_list = [line.split() for line in f]
    return (line_list, puzzle_list)

def get_children(w, dict):
    children = []
    letters = ['a', 'b', 'c', 'd', 'e', "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for index, char in enumerate(w):
        for letter in letters:
            if letter != char:
                word = w[0:index] + letter + w[index+1:]
                if word in dict:
                    children.append(word)
    return children

def print_for_submission(dict_file, puzzle_file):
    start = time.perf_counter()
    word_list, puzzle_list = open_file(dict_file_name, puzzle_file_name)
    end = time.perf_counter()
    print(f"Time to create data structure was: {end - start} seconds")
    print(f"There are {len(word_list)} words in this dict.\n")
    time_taken = 0.0
    for index, puzzle in enumerate(puzzle_list):
        start = puzzle[0]
        end = puzzle[1]
        start1 = time.perf_counter()
        path = print_path(BFS(start, end, word_list))
        end1 = time.perf_counter()
        time_taken += (end1 - start1)
        print(f"Line: {index}")
        if path != "No solution!":
            print(f"Length is: {path[1]}")
            print(path[0])
        else:
            print(path)
    print(f"\nTime to solve all of these puzzles was: {time_taken} seconds")     

def print_path(solved):
    if solved == -1:
        return "No solution!"
    print_order = []
    print_order.append(solved[0])
    while solved != None:
        solved = solved[2]
        if solved != None:
            print_order.append(solved[0])
    path_length = len(print_order)
    print_order = print_order[::-1]
    path = ""
    for index, elem in enumerate(print_order):
        path += (elem)
        path += ("\n")
    return (path, path_length)

def BFS(start_node, goal_node, word_list):
    fringe = deque()
    count = 0
    visited = {start_node}
    fringe.append((start_node, count, None))
    while fringe:
        v = fringe.popleft()
        if v[0] == goal_node:
            return v
        for c in get_children(v[0], word_list):
            if c not in visited:
                fringe.append((c, count + 1, v))
                visited.add(c)
        count += 1
    return -1


def unlimitedBFS(start_node, word_list):
    fringe = deque()
    count = 0
    visited = {start_node}
    fringe.append((start_node, count, None))
    last_node = None
    while fringe:
        v = fringe.popleft()
        last_node = v
        for c in get_children(v[0], word_list):
            if c not in visited:
                fringe.append((c, count + 1, v))
                visited.add(c)
        count += 1
    return last_node


def unlimitedBFS1(start_node, word_list):
    fringe = deque()
    count = 0
    visited = {start_node}
    fringe.append((start_node, count, None))
    while fringe:
        v = fringe.popleft()
        if not fringe and count > 2:
            return v
        for c in get_children(v[0], word_list):
            if c not in visited:
                fringe.append((c, count + 1, v))
                visited.add(c)
        count += 1
    return visited

def hardestBFS(start_node, word_list):
    fringe = deque()
    count = 0
    visited = {start_node}
    fringe.append((start_node, count, None))
    while fringe:
        v = fringe.popleft()
        if not fringe and count != 0: 
            return v
        for c in get_children(v[0], word_list):
            if c not in visited:
                fringe.append((c, count + 1, v))
                visited.add(c)
        count += 1
    


def find_singletons(word_list):
    singletons = []
    for word in word_list:
        if len(get_children(word, word_list)) == 0:
            singletons.append(word)
    return len(singletons)

dict_file_name = '/Volumes/GoogleDrive-104048612014867030298/My Drive/11th Grade/AI/Unit 1/Word Ladders/words_06_letters.txt'
puzzle_file_name = '/Volumes/GoogleDrive-104048612014867030298/My Drive/11th Grade/AI/Unit 1/Word Ladders/puzzles_normal.txt'
word_list, puzzle_list = open_file(dict_file_name, puzzle_file_name)

# Brainteaser 1
# Brainteaser 1: 1568 words without any children]

# Brainteaser 2
# Brainteaser 2: 1625

# Brainteaser 3
# words = word_list
# num_clumps = 0
# while words:
#     fringe = deque()
#     count = 0
#     visited = {words[0]}
#     fringe.append((words[0], count, None))
#     while fringe:
#         v = fringe.popleft()
#         for c in get_children(v[0], words):
#             if c not in visited:
#                 fringe.append((c, count + 1, v))
#                 visited.add(c)
#         count += 1
#     for elem in visited:
#         words.remove(elem)
#     num_clumps += 1

# num_clumps -= 1568
# print(num_clumps)
# Brainteaser 3: 450 clumps

# Brainteaser 4

# start = unlimitedBFS1('willed', word_list)
start = ['drafty']
# start = ""
# for word in clump:
#     start = word
#     break

print(start)
print(print_path(unlimitedBFS(start[0], word_list))[0])