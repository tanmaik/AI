import math

def putqMarks(board):
    SFboard = list(board)
    qMark = [None] * 100
    for x in range(10):
        qMark[x] = "?"
        qMark[-x] = "?"
        qMark[(x * 10)] = "?"
        qMark[9 + (x * 10)] = "?"
    for y in range(len(qMark)):
        if qMark[y] == None:
            qMark[y] = SFboard[0]
            del SFboard[0]
    return "".join(qMark)


def possible_moves(board, token):
    currentspots = []
    availablespots = []
    opponent = ""
    if (token == "x"):
        opponent = "o"
    else:
        opponent = "x"
    tenboard = putqMarks(board)
    eightboard = []
    currentspots = [i for i, ltr in enumerate(tenboard) if ltr == token]
    for y in currentspots:
        if tenboard[y - 10] == opponent:  # Up
            for x in range(11):
                if x != 0:
                    if (tenboard[y - (x * 10)]) == ".":
                        availablespots.append(y - (x * 10))
                        break
                    elif (tenboard[y - (x * 10)]) == "?" or (tenboard[y - (x * 10)]) == token:
                        break
        if tenboard[y + 10] == opponent:  # Down
            for x in range(11):
                if x != 0:
                    if (tenboard[y + (x * 10)]) == ".":
                        availablespots.append(y + (x * 10))
                        break
                    elif (tenboard[y + (x * 10)]) == "?" or (tenboard[y + (x * 10)]) == token:
                        break
        if tenboard[y + 1] == opponent:  # Right
            for x in range(11):
                if x != 0:
                    if (tenboard[y + (x + 1)]) == ".":
                        availablespots.append(y + (x + 1))
                        break
                    elif (tenboard[y + (x + 1)]) == "?" or (tenboard[y + (x + 1)]) == token:
                        break
        if tenboard[y - 1] == opponent:  # Left
            for x in range(11):
                if x != 0:
                    if (tenboard[y - (x + 1)]) == ".":
                        availablespots.append(y - (x + 1))
                        break
                    elif (tenboard[y - (x + 1)]) == "?" or (tenboard[y - (x + 1)]) == token:
                        break
        if tenboard[y + 9] == opponent:  # RDdown
            for x in range(11):
                if x != 0:
                    if (tenboard[y + (x * 9)]) == ".":
                        availablespots.append(y + (x * 9))
                        break
                    elif (tenboard[y + (x * 9)]) == "?" or (tenboard[y + (x * 9)]) == token:
                        break
        if tenboard[y - 9] == opponent:  # RDUp
            for x in range(11):
                if x != 0:
                    if (tenboard[y - (x * 9)]) == ".":
                        availablespots.append(y - (x * 9))
                        break
                    elif (tenboard[y - (x * 9)]) == "?" or (tenboard[y - (x * 9)]) == token:
                        break
        if tenboard[y + 11] == opponent:  # LDdown
            for x in range(11):
                if x != 0:
                    if (tenboard[y + (x * 11)]) == ".":
                        availablespots.append(y + (x * 11))
                        break
                    elif (tenboard[y + (x * 11)]) == "?" or (tenboard[y + (x * 11)]) == token:
                        break
        if tenboard[y - 11] == opponent:  # LDup
            for x in range(11):
                if x != 0:
                    if (tenboard[y - (x * 11)]) == ".":
                        availablespots.append(y - (x * 11))
                        break
                    elif (tenboard[y - (x * 11)]) == "?" or (tenboard[y - (x * 11)]) == token:
                        break
    availablespots = list(set(availablespots))
    for x in availablespots:
        leftover = int(x / 10)
        toremove = 9 + (2 * leftover)
        actualnum = x - toremove
        eightboard.append(actualnum)
    return eightboard


def make_move(board, token, index):
    tenboardindex = int(index)
    if (token == "x"):
        opponent = "o"
    else:
        opponent = "x"
    copyof = board
    toflip = []
    eightSpots = []
    tempspots = []
    copyoflist = list(copyof)
    copyoflist[index] = token
    copyof = "".join(copyoflist)
    tenboard = putqMarks(copyof)
    leftover = int(index / 8)
    index = index + (11 + (2 * leftover))
    if tenboard[index - 10] == opponent:  # Up
        tempspots.append(index - 10)
        for x in range(11):
            if x != 0:
                if (tenboard[index - (x * 10)]) == opponent:
                    tempspots.append(index - (x * 10))
                elif (tenboard[index - (x * 10)]) == "?" or (tenboard[index - (x * 10)]) == '.':
                    tempspots = []
                    break
                else:
                    toflip += tempspots
                    tempspots = []
                    break
    if tenboard[index + 10] == opponent:  # Down
        tempspots.append(index + 10)
        for x in range(11):
            if x != 0:
                if (tenboard[index + (x * 10)]) == opponent:
                    tempspots.append(index + (x * 10))
                elif (tenboard[index + (x * 10)]) == "?" or (tenboard[index + (x * 10)]) == '.':
                    tempspots = []
                    break
                else:
                    toflip += tempspots
                    tempspots = []
                    break
    if tenboard[index + 1] == opponent:  # Right
        tempspots.append(index + 1)
        for x in range(11):
            if x != 0:
                if (tenboard[index + (x + 1)]) == opponent:
                    tempspots.append(index + (x + 1))
                elif (tenboard[index + (x + 1)]) == "?" or (tenboard[index + (x + 1)]) == '.':
                    tempspots = []
                    break
                else:
                    toflip += tempspots
                    tempspots = []
                    break
    if tenboard[index - 1] == opponent:  # Left
        tempspots.append(index - 1)
        for x in range(11):
            if x != 0:
                if (tenboard[index - (x + 1)]) == opponent:
                    tempspots.append(index - (x + 1))
                elif (tenboard[index - (x + 1)]) == "?" or (tenboard[index - (x + 1)]) == '.':
                    tempspots = []
                    break
                else:
                    toflip += tempspots
                    tempspots = []
                    break
    if tenboard[index + 9] == opponent:  # RDdown
        tempspots.append(index + 9)
        for x in range(11):
            if x != 0:
                if (tenboard[index + (x * 9)]) == opponent:
                    tempspots.append(index + (x * 9))
                elif (tenboard[index + (x * 9)]) == "?" or (tenboard[index + (x * 9)]) == '.':
                    tempspots = []
                    break
                else:
                    toflip += tempspots
                    tempspots = []
                    break
    if tenboard[index - 9] == opponent:  # RDUP
        tempspots.append(index - 9)
        for x in range(11):
            if x != 0:
                if (tenboard[index - (x * 9)]) == opponent:
                    tempspots.append(index - (x * 9))
                elif (tenboard[index - (x * 9)]) == "?" or (tenboard[index - (x * 9)]) == '.':
                    tempspots = []
                    break
                else:
                    toflip += tempspots
                    tempspots = []
                    break
    if tenboard[index + 11] == opponent:  # LDdown
        tempspots.append(index + 11)
        for x in range(11):
            if x != 0:
                if (tenboard[index + (x * 11)]) == opponent:
                    tempspots.append(index + (x * 11))
                elif (tenboard[index + (x * 11)]) == "?" or (tenboard[index + (x * 11)]) == '.':
                    tempspots = []
                    break
                else:
                    toflip += tempspots
                    tempspots = []
                    break
    if tenboard[index - 11] == opponent:  # LDUp
        tempspots.append(index - 11)
        for x in range(11):
            if x != 0:
                if (tenboard[index - (x * 11)]) == opponent:
                    tempspots.append(index - (x * 11))
                elif (tenboard[index - (x * 11)]) == "?" or (tenboard[index - (x * 11)]) == '.':
                    tempspots = []
                    break
                else:
                    toflip += tempspots
                    tempspots = []
                    break
    for x in toflip:
        leftover = int(x / 10)
        toremove = 9 + (2 * leftover)
        actualnum = x - toremove
        eightSpots.append(actualnum)
    for y in eightSpots:
        copyoflist[y] = token
        copyof = "".join(copyoflist)
    return copyof
# *********************This is the code for the assignment2. Code above this is for Assignment1
import sys
board = sys.argv[1]
player = sys.argv[2]
depth = 1

static_weights = [
    120, -20, 20, 5, 5, 20, -20, 120,                   # 0    1  2  3  4  5  6  7
    -20, -40, -5, -5, -5, -5, -40, -20,                 # 8    9  10 11 12 13 14 15
    20, -5, 15, 3, 3, 15, -5, 20,                       # 16   17 18 19 20 21 22 23
    5, -5, 3, 3, 3, 3, -5, 5,                           # 24   25 26 27 28 29 30 31
    5, -5, 3, 3, 3, 3, -5, 5,                           # 32   33 34 35 36 37 38 39
    20, -5, 15, 3, 3, 15, -5, 20,                       # 40   41 42 43 44 45 46 47
    -20, -40, -5, -5, -5, -5, -40, -20,                 # 48   49 50 51 52 53 54 55
    120, -20, 20, 5, 5, 20, -20, 120 ]                  # 56   57 58 59 60 61 62 63

corners_dict = {
    0: {1, 8, 9},
    7: {6, 14, 15},
    56: {57, 48, 49},
    63: {62, 54, 55}
}

def take_corners(board, pos):
    if pos in corners_dict:
        return pos
    return -1

def mobility_score(board):
    return len(possible_moves(board, 'x')) - len(possible_moves(board, 'o'))


def game_score(board, player):
    x_weighted = 0
    o_weighted = 0
    for i in range(len(board)):
        if board[i] == player:
            x_weighted += static_weights[i]
        else:
            o_weighted += static_weights[i]

    return x_weighted - o_weighted

# structure for debugging
tree_struct = []

# We are going to call min_max by passing the board for current player
# so for example when I am playing x, this function would be called
# with player = "x", a board that has already has "x"'s moved
# once inside this function, we are going to play first as "o"
# followed by "x" and so on
mobility_factor1 = 20
mobility_factor2 = 5
pos_factor = 10

def min_max(board, depth, maximizing_player, move):
    if maximizing_player:
        player = "x"
        opp = "o"
    else:
        player = "o"
        opp = "x"

    if depth == 0 or board.count(".") == 0:
        temp_mob = 0
        mob_score = mobility_score(board)
        leaf_score = game_score(board, player)  + (mobility_factor1 * mob_score)

        return leaf_score

    moves = possible_moves(board, player)
    if maximizing_player:
        max_val = -math.inf
        for possible in moves:
            copyOf = make_move(board, player, possible)
            max_val = max(max_val, min_max(copyOf, depth - 1, False, possible))
        return max_val
    else:
        min_val = math.inf
        for possible in moves:
            copyOf = make_move(board, player, possible)
            min_val = min(min_val, min_max(copyOf, depth - 1, True, possible))
        return min_val

def find_next_move(board, player, depth):
    best = None
    moves = possible_moves(board, player)

    for move in moves:
        board_pos = take_corners(board, move)
        if board_pos != -1:
            print(board_pos)
            return  (10000, board_pos)

    maximizing = True if player == "x" else False
    for move in moves:
        board_state = make_move(board, player, move)
        val = min_max(board_state, depth, not maximizing, move)
        if best is None or val > best[0]:
            best = (val, move)
    return best

def chooseMove(board, player):
    for move in possible_moves(board, player):
        board_pos = take_corners(board, move)
        if board_pos != -1:
            print(board_pos)
    for i in range(2, 10):
        score = find_next_move(board, player, i)
        print(score[1])

chooseMove(board, player)