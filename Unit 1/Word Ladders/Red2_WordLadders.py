import sys
import time
from collections import deque 

def BiBFS(start_node, end_node, word_list):
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
        for c in get_children(v[0], word_list):
            if c not in start_visited:
                start_fringe.append((c, count + 1, v))
                start_checker.append(c)
                start_visited.add(c)
                if start_checker[-1] in end_checker:
                    index = end_checker.index(start_checker[-1])
                    return [start_fringe[-1], end_fringe[index]]    
        for c in get_children(t[0], word_list):
            if c not in end_visited:
                end_fringe.append((c, count + 1, t))
                end_visited.add(c)
                end_checker.append(c)
                if end_checker[-1] in start_checker:
                    index = start_checker.index(end_checker[-1])
                    return [start_fringe[index], end_fringe[-1]]
        count += 1
    return -1

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
    time_taken = 0.0
    print(f"Time to create data structure was: {end - start} seconds")
    print(f"There are {len(word_list)} words in this dict.\n")
    for index, puzzle in enumerate(puzzle_list):
        start = puzzle[0]
        end = puzzle[1]
        start1 = time.perf_counter()
        solution = BiBFS(start, end, word_list)
        end1 = time.perf_counter()
        time_taken += (end1 - start1)
        print(f"Line: {index}")
        if solution == -1:
            print("No solution!")
        else:
            path = print_path_prime(solution[0], solution[1])
            print(f"Length is: {path[1]}")
            print(path[0])
    print(f"\nTime to solve all of these puzzles was: {time_taken} seconds")

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
        path += ((elem))
        path += ("\n")
        i += 1
    old = print_order
    print_order = []
    while t != None:
        t = t[2]
        if t != None:
            if t[0] not in old:
                print_order.append(t[0])
    for elem in print_order:
        path += ((elem))
        path += ("\n")
        i += 1
    return (path, i)

dict_file_name = sys.argv[1]
puzzle_file_name = sys.argv[2]
print_for_submission(dict_file_name, puzzle_file_name)

