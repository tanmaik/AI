import sys
from math import sqrt

def open_file(filename):
    with open(filename) as f:
        line_list = [line.strip() for line in f]
    return line_list

def determine_variables(p):
    N = int(sqrt(len(p)))
    symbol_set = {x for x in p if x != "."}
    for i in range(int(sqrt(N))-1, 0):
        if n % i = 
    subblock_width = None

puzzles = open_file("/Volumes/GoogleDrive-104048612014867030298/My Drive/11th Grade/AI/Unit 2/Sudoku/puzzles_1_standard_easy.txt")
