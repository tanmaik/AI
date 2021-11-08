import sys
from math import sqrt
from copy import copy

def open_file(filename):
    with open(filename) as f:
        line_list = [line.strip() for line in f]
    return line_list

def determine_variables(p):
    N = int(sqrt(len(p)))
    symbol_set = {x for x in p if x != "."}
    if '.0' in str(sqrt(N)):
        return int(N), symbol_set, int(sqrt(N)), int(sqrt(N))
    subblock_width = 0
    subblock_height = 0
    for i in range(int(sqrt(N)), 0, -1):
        if N % i == 0:
            subblock_height = i
            break
    for i in range(int(sqrt(N))+1, N):
        if N % i == 0:
            subblock_width = i
            break
    return N, symbol_set, subblock_width, subblock_height

def print_puzzle(puzzle):
    size = int(sqrt(len(puzzle)))
    s = ''
    for i in range(1, len(puzzle) + 1):
        s += puzzle[i - 1] + " "       
        if i % size == 0:
            s += "\n"
    return s

def generate_constraint_sets(puzzle, s_w, s_h):
    size = int(sqrt(len(puzzle)))
    constraint_sets = []
    for n in range(size):
        constraint_sets.append({x + n*size for x in range(size)})
    for n in range(size):
        constraint_sets.append({n + x*size for x in range(size)})
    for y in range(0, size, s_h):    
        for x in range(0, size, s_w):
            toAdd = set()
            for i in range(0+x, s_w+x):
                for j in range(0+y, s_h+y):
                    toAdd.add(i + j)
            constraint_sets.append(toAdd)

        # for y in range(s_h):
        #     toAdd = set()
        #     for i in range():
        #         for
    return constraint_sets

def find_neighbors(constraint_sets, symbol_set, N):
    neighbors = dict()
    for n in range(N^2):
        neighbors[n] = set()
        for s in constraint_sets:
            if n in s:
                temp = copy(s)
                temp.remove(n)
                for elem in temp:
                    neighbors[n].add(elem)
    return neighbors
puzzles = open_file("/Volumes/GoogleDrive-104048612014867030298/My Drive/11th Grade/AI/Unit 2/Sudoku/puzzles_1_standard_easy.txt")
puzzle = puzzles[0]
N, symbol_set, subblock_width, subblock_height = determine_variables(puzzle)
print(print_puzzle(puzzle))
print(find_neighbors(generate_constraint_sets(puzzle, subblock_width, subblock_height), symbol_set, N))