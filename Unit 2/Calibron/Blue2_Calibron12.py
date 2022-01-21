from gzip import READ
import sys
from copy import copy
# You are given code to read in a puzzle from the command line.  The puzzle should be a single input argument IN QUOTES.
# A puzzle looks like this: "56 56 28x14 32x11 32x10 21x18 21x18 21x14 21x14 17x14 28x7 28x6 10x7 14x4"
# The code below breaks it down:
puzzle = sys.argv[1].split()
puzzle_height = int(puzzle[0])
puzzle_width = int(puzzle[1])
rectangles = [(int(temp.split("x")[0]), int(temp.split("x")[1])) for temp in puzzle[2:]]
# puzzle_height is the height (number of rows) of the puzzle
# puzzle_width is the width (number of columns) of the puzzle
# rectangles is a list of tuples of rectangle dimensions

# INSTRUCTIONS:

# First check to see if the sum of the areas of the little rectangles equals the big area.
# If not, output precisely this - "Containing rectangle incorrectly sized."

# Then try to solve the puzzle.
# If the puzzle is unsolvable, output precisely this - "No solution."

# If the puzzle is solved, output ONE line for EACH rectangle in the following format:
# row column height width
# where "row" and "column" refer to the rectangle's top left corner.

# For example, a line that says:
# 3 4 2 1
# would be a rectangle whose top left corner is in row 3, column 4, with a height of 2 and a width of 1.
# Note that this is NOT the same as 3 4 1 2 would be.  The orientation of the rectangle is important.

# Your code should output exactly one line (one print statement) per rectangle and NOTHING ELSE.
# If you don't follow this convention exactly, my grader will fail.

sum_area = 0
for rectangle in rectangles:
    sum_area += (rectangle[0] * rectangle[1])

if sum_area != (puzzle_height * puzzle_width):
    print("Containing rectangle incorrectly sized.")
    exit()

board_state = []
for x in range(puzzle_height):
    toAdd = []
    for x in range(puzzle_width):
        toAdd.append("")
    board_state.append(toAdd)


alphabet = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
rectangles_dict = dict()
for x in range(len(rectangles)):
    rectangles_dict[(rectangles[x][0], rectangles[x][1])] = alphabet[x]
    rectangles_dict[(rectangles[x][1], rectangles[x][0])] = alphabet[x]

# Pass in a tuple (length, width), 2D array, top-left x-coordinate, and top-left y-coordinate
def add_rect(rectangle, board, x, y):
    height = rectangle[0]
    width = rectangle[1]
    designated_letter = rectangles_dict[(height, width)]
    for y_coord in range(y, y + height):
        for x_coord in range(x, x + width):
            # First check if the index will be out of bounds
            try:
                val = board[y_coord][x_coord]
            except:
                return False
            # Check if space is empty space
            if board[y_coord][x_coord] == "":
                board[y_coord][x_coord] = designated_letter
            else:
                # Rectangle cannot be placed there so return False
                return False
    return board
   
def test_rect(rectangle, board, x, y):
    alphabet = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    height = rectangle[0]
    width = rectangle[1]
    designated_letter = rectangles_dict[(height, width)]
    for y_coord in range(y, y + height):
        for x_coord in range(x, x + width):
            # First check if the index will be out of bounds
            try:
                val = board[y_coord][x_coord]
            except:
                return False
            # Check if space is empty space
            if board[y_coord][x_coord] == "":
                pass
            else:
                # Rectangle cannot be placed there so return False
                return False
    return True

def get_next_unassigned_var(board):
    for y in range(puzzle_height):
        for x in range(puzzle_width):
            if board[y][x] == "":
                return (y, x)

def get_sorted_values(state, var):
    values = []
    y, x = var
    for rect in rectangles:
        r1 = rect[0]
        r2 = rect[1]
        letter = rectangles_dict[(r1, r2)]
        for row in state:
            for elem in row:
                if elem == letter:
                    continue
        if test_rect((r1, r2), state, x, y):
            values.append((r1, r2))
        if test_rect((r2, r1), state, x, y):
            values.append((r2, r1))
    return values

def test_solution(state):
    for row in state:
        for elem in row:
            if elem == "":
                return False
    return True

def csp_backtracking(state):
    print('hi')
    if None not in state:
        if test_solution(state):
            return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var):
        new_state = copy(state)
        r1, r2 = val
        print(r1, " ", r2, " rect being placed")
        y, x = var
        new_state = add_rect((r1, r2), new_state, x, y)
        for row in new_state:
            r = ""
            for elem in row:
                r += elem + " "
            print(r)
        result = csp_backtracking(new_state)
        if result: return result
    return None

print(rectangles_dict)

finished_board = csp_backtracking(board_state)
if finished_board == None:
    print("No solution.")

for row in finished_board:
    r = ""
    for elem in row:
        r += elem + " "
    print(r)
# print(finished_board)