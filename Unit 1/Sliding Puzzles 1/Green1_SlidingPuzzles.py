# Coordinate-location to one-dimensional indices

def BFS():
    return

def get_children():
    return

def goal_test():
    return

def change_dimension(coordinates, dimension):
    return

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
    for char in puzzle:
        if char.isalpha():
            goal_puzzle += char
    return goal_puzzle

file_name = "/Volumes/GoogleDrive-104048612014867030298/My Drive/11th Grade/AI/Unit 1/Sliding Puzzles 1/slide_puzzle_tests.txt"

with open(file_name) as f: 
    line_list = [line.strip() for line in f]

# print(find_goal(print_puzzle(line_list[1])))
