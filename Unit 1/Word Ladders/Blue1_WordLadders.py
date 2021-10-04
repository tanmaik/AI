import sys
import time
from collections import deque 

def open_file(dict_file, puzzle_file):
    with open(dict_file) as f:
        line_list = {line.strip() for line in f}
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

dict_file_name = "/Volumes/GoogleDrive-104048612014867030298/My Drive/11th Grade/AI/Unit 1/Word Ladders/words_06_longer.txt"
puzzle_file_name = "/Volumes/GoogleDrive-104048612014867030298/My Drive/11th Grade/AI/Unit 1/Word Ladders/puzzles_longer.txt"
print_for_submission(dict_file_name, puzzle_file_name)
