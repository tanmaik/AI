import sys
from copy import copy

board = sys.argv[1]
default = copy(board)
heights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if len(board) != 200:
    print("Board is not correct length.")
    exit()

score = 0

pieces = [
    {0: (0, 1), 1: (0, 1), 2: (0, 1), 3: (0, 1)},
    {0: (0, 4)},
    {0: (0, 2), 1: (0, 2)},
    {0: (0, 1), 1: (0, 2), 2: (0, 1)},
    {0: (0, 3), 1: (-1, 1)},
    {0: (-1, 1), 1: (0, 2), 2: (-1, 1)},
    {0: (-1, 1), 1: (0, 3)},
    {0: (0, 1), 1: (0, 2), 2: (-1, 1)},
    {0: (-1, 2), 1: (0, 2)},
    {0: (-1, 1), 1: (0, 2), 2: (0, 1)},
    {0: (0, 2), 1: (-1, 2)},
    {0: (0, 2), 1: (0, 1), 2: (0, 1)},
    {0: (0, 3), 1: (-2, 1)},
    {0: (-1, 1), 1: (-1, 1), 2: (0, 2)},
    {0: (0, 1), 1: (0, 3)}, 
    {0: (0, 1), 1: (0, 1), 2: (0, 2)},
    {0: (0, 3), 1: (0, 1)},
    {0: (0, 2), 1: (-1, 1), 2: (-1, 1)},
    {0: (-2, 1), 1: (0, 3)}
]

def string_to_matrix(board):
    matrix = []
    toAdd = []
    for index, char in enumerate(board):
        toAdd.append(char)
        if len(toAdd) == 10:
            matrix.append(toAdd)
            toAdd = []
    return matrix
            
def matrix_to_string(matrix):
    toReturn = ""
    for row in matrix:
        for char in row:
            toReturn += char
    return toReturn

def add_puzzle(piece, board, left_most_column):
    matrix = string_to_matrix(board)
    num_cols = len(piece)
    sums = [-100 for x in range(num_cols)]
    if (left_most_column + num_cols - 1) > 9:
        return False
    for current_col in range(left_most_column, left_most_column + num_cols):
            sums[current_col - left_most_column] = heights[current_col] + piece[current_col - left_most_column][0]  
    row_to_place = 19 - max(sums)
    if row_to_place < 0:
        return "GAME OVER"
    for col in piece: 
        for row in range(row_to_place + piece[col][0] - piece[col][1] + 1, row_to_place + piece[col][0] + 1):
            if row < 0: 
                return "GAME OVER"
            matrix[row][left_most_column + col] = "#"
    return matrix_to_string(matrix)

def find_heights(board): 
    matrix = string_to_matrix(board)
    heights = [0 for x in range(10)]
    for col in range(10):
        if matrix[0][col] == "#":
            heights[col] = 20
            continue
        for row in range(20):
            if matrix[row][col] != "#":
                if matrix[row + 1][col] == '#':
                        heights[col] = 20 - (row + 1)
                        break
    return heights

def check_eliminations(board):
    matrix = string_to_matrix(board)
    toPop = []
    for index, row in enumerate(matrix):
        if " " not in row:
            toPop.append(index)
    for x in range(len(toPop)):
        matrix.remove(["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])
    for x in range(len(toPop)):
        matrix = [[" "," "," "," "," "," "," "," "," "," "]] + matrix
    return matrix_to_string(matrix)


def print_puzzle(board):
    for count in range(20):
        print(' '.join(list(("|" + board[count * 10: (count + 1) * 10] + "|"))), " ", count)

f = open("tetrisout.txt", 'w')

for piece in pieces:
    heights = find_heights(board)
    for left_most in range(10):
        temp = add_puzzle(piece, board, left_most)
        if (temp):
            if "GAME OVER" not in temp:
                board = temp
                board = check_eliminations(board)
                # print(board)
                f.write(board + "\n")
            else:
                # print("GAME OVER")
                f.write("GAME OVER\n")
        board = copy(default)
f.close()