import sys
import random
import math
import pickle

POPULATION_SIZE = 200
NUM_CLONES = 50
TRIALS = 5
TOURNAMENT_SIZE = 20
TOURNAMENT_WIN_PROBABILITY = .83
MUTATION_RATE = .1
STRATEGY_LENGTH = 5

pieces = [ # fix to make each orientation in its own group
    [{0: (0, 1), 1: (0, 1), 2: (0, 1), 3: (0, 1)},
    {0: (0, 4)}],
    [{0: (0, 2), 1: (0, 2)}],
    [{0: (0, 1), 1: (0, 2), 2: (0, 1)},
    {0: (0, 3), 1: (-1, 1)},
    {0: (-1, 1), 1: (0, 2), 2: (-1, 1)},
    {0: (-1, 1), 1: (0, 3)}],
    [{0: (0, 1), 1: (0, 2), 2: (-1, 1)},
    {0: (-1, 2), 1: (0, 2)}],
    [{0: (-1, 1), 1: (0, 2), 2: (0, 1)},
    {0: (0, 2), 1: (-1, 2)}],
    [{0: (0, 2), 1: (0, 1), 2: (0, 1)},
    {0: (0, 3), 1: (-2, 1)},
    {0: (-1, 1), 1: (-1, 1), 2: (0, 2)},
    {0: (0, 1), 1: (0, 3)}], 
    [{0: (0, 1), 1: (0, 1), 2: (0, 2)},
    {0: (0, 3), 1: (0, 1)},
    {0: (0, 2), 1: (-1, 1), 2: (-1, 1)},
    {0: (-2, 1), 1: (0, 3)}]
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

def add_piece(piece, board, left_most_column, heights):
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
    toReturn = matrix_to_string(matrix)
    return check_eliminations(toReturn)

def find_heights(board): 
    matrix = string_to_matrix(board)
    heights = [0 for x in range(10)]
    for col in range(10):
        if matrix[0][col] == "#":
            heights[col] = 20
            continue
        for row in range(19):
            if matrix[row][col] != "#":
                # try: for testing
                if matrix[row + 1][col] == '#':
                        heights[col] = 20 - (row + 1)
                        break
                # except: 
                #     print_puzzle(board)
                #     print(matrix)
                #     print(row, col)
                #     sys.exit()
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
    return matrix_to_string(matrix), len(toPop)


def print_puzzle(board):
    print("=======================")
    for count in range(20):
        print(' '.join(list(("|" + board[count * 10: (count + 1) * 10] + "|"))), " ", count)
    print("=======================")
    print()
    print("  0 1 2 3 4 5 6 7 8 9  ")
    print()



def heuristic(board, strategy, lines_removed):
    a, b, c, d, e = strategy
    value = 0
    heights = find_heights(board)
    value += a * sum(heights)
    value += b * min(heights)
    value += c * max(heights)
    value += d * (lines_removed)
    value += e * (board.count("#"))
    return value


def play_game(strategy, print_game):
    board = ' '*200
    points = 0
    while True:
        heights = find_heights(board)
        piece = random.choice(pieces)
        boards = []
        scores = []
        clearedLines = []
        for orientation in piece:
            for left_most in range(10):
                result = add_piece(orientation, board, left_most, heights)
                if result:
                    if result == "GAME OVER":
                        boards.append("")   
                        scores.append(-1000000000)
                        clearedLines.append(0)
                    else:
                        poss_board, lines_removed = result
                        boards.append(poss_board)
                        scores.append(heuristic(poss_board, strategy, lines_removed))
                        clearedLines.append(lines_removed)
        board = boards[scores.index(max(scores))]
        if board == "":
            return points
        if print_game:
            print_puzzle(board)
        lines_cleared = clearedLines[boards.index(board)]
        if lines_cleared == 1:
            points += 40
        elif lines_cleared == 2:
            points += 100
        elif lines_cleared == 3:
            points += 300
        elif lines_cleared >= 4:
            points += 1200
    return points


def fitness_function(strategy):
    game_scores = []
    for count in range(TRIALS):
        game_scores.append(play_game(strategy, False))
    return (sum(game_scores)/len(game_scores))

def generate_random_strategy():
    strat = []
    for i in range(STRATEGY_LENGTH):
        multiplier = 1
        if random.random() < 0.5: 
            multiplier = -1
        strat.append(random.random() * multiplier)
    return strat

def add_child(population):
    full_tourney = []
    while len(full_tourney) < (TOURNAMENT_SIZE * 2):
        toAdd = random.choice(population)
        if toAdd not in full_tourney:
            full_tourney.append(toAdd)
    tourney1 = full_tourney[:TOURNAMENT_SIZE]
    tourney2 = full_tourney[TOURNAMENT_SIZE:]
    tourney1.sort(key=lambda x:x[0])
    tourney2.sort(key=lambda x:x[0])
    tourney1 = tourney1[::-1]
    tourney2 = tourney2[::-1]
    parent1 = 0
    parent2 = 0
    for element in tourney1:
        if random.random() <= TOURNAMENT_WIN_PROBABILITY:
            parent1 = element[1]
            break
    for element in tourney2:
        if random.random() <= TOURNAMENT_WIN_PROBABILITY:
            parent2 = element[1]
            break
    if parent1 == 0:
        parent1 = tourney1[0][1]
    if parent2 == 0:
        parent2 = tourney2[0][1]
    child = create_child(parent1, parent2)
    return child

def create_child(mom, dad):
    like_mom = random.randrange(1, len(mom))
    what_from_mom = []
    child = []
    while len(what_from_mom) < like_mom:
        toAdd = random.randrange(0, len(mom))
        if toAdd not in what_from_mom:
            what_from_mom.append(toAdd)
    for n in range(len(mom)):
        if n in what_from_mom:
            child.append(mom[n])
        else:
            child.append(dad[n])
    if random.random() < MUTATION_RATE:
        multiplier = 1
        if random.random() < 0.5: 
            multiplier = -1
        child[random.randrange(0, len(child))] = (multiplier * random.random())
    return child

def create_initial_generation():
    g0 = []
    while len(g0) < POPULATION_SIZE:
        stratToAdd = generate_random_strategy()
        if stratToAdd not in g0:
            g0.append(stratToAdd)
    return g0

def rank_population(population):
    strat_and_fitness = []
    for index, strategy in enumerate(population):
        if len(strategy) != 2:
            fitness_score = fitness_function(strategy)
            print(f"Evaluating strategy number {index} --> {fitness_score}")
            strat_and_fitness.append((fitness_score, strategy))
        else:
            print(f"Evaluating strategy number {index} --> {strategy[0]}")
            strat_and_fitness.append(strategy)
    ranked = sorted(strat_and_fitness)
    return ranked[::-1]

gen_num = 0
going = True
starting = input("(N)ew process, or (L)oad saved progress? ")
if not (starting == "N" or starting == "L"):
    print("Please pick restart the process and pick a valid option.")
    going = False
    exit()
while going:
    if starting == "N":
        g0 = create_initial_generation()
        ranked_g0 = rank_population(g0)
        adding = 0
        for x in ranked_g0:
            adding += x[0]
        print(f"Average: {adding/POPULATION_SIZE}")
        print(f"Generation: {gen_num}")
        gen_num += 1
        print(f"Best strategy so far: {ranked_g0[0][1]} with score: {ranked_g0[0][0]}")
        starting = input("(P)lay a game with current best strategy, (S)ave current process, or (C)ontinue? ")
        ranked_gnew = ranked_g0
    elif starting == "L":
        file_name = input("What filename? ")
        pickle_in = open(file_name, "rb")
        ranked_gnew = pickle.load(pickle_in)
        print(f"Best strategy so far: {ranked_gnew[0][1]} with score: {ranked_gnew[0][0]}")
        starting = input("(P)lay a game with current best strategy, (S)ave current process, or (C)ontinue? ")
    elif starting == "S":
        file_name = input("What filename? ")
        pickle_out = open(file_name, "wb")
        pickle.dump(ranked_gnew, pickle_out)
        pickle_out.close()
        exit()
    elif starting == "P":
        x = play_game(ranked_gnew[0][1], True)
        print("This game had a score of", x)
        starting = input("(P)lay a game with current best strategy, (S)ave current process, or (C)ontinue? ")
    elif starting == "C":
        g_new = []
        for clone in range(NUM_CLONES):
            g_new.append(ranked_gnew[clone])
        while len(g_new) < POPULATION_SIZE:
            g_new.append(add_child(ranked_gnew))
        ranked_gnew = rank_population(g_new)
        for x in ranked_gnew:
            adding += x[0]
        print(f"Average: {adding/POPULATION_SIZE}")
        print(f"Generation: {gen_num}")
        gen_num += 1
        print(f"Best strategy so far: {ranked_gnew[0][1]} with score: {ranked_gnew[0][0]}")
        starting = input("(P)lay a game with current best strategy, (S)ave current process, or (C)ontinue? ")
