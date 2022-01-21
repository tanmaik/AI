import sys
import math
import time


directions = [-11, -10, -9, -1, 1, 9, 10, 11]
def find_next_move(board, player, depth):
    if player == 'x':
        opponent = 'o'
    else:
        opponent = 'x'
    max = (0, float("-inf"))
    for board in possible_next_boards(board, player):
        board2, index = board
        value = -1 * negamax(board2, opponent, depth, float('-inf'), float('inf'))
        if value >= max[1]:
            max = (index, value)
    return max[0]

def convertBoard(board):
    # string = '??????????'
    # board = string + board
    board = ''.join(board)
    if '?' not in board:
        string = ""
        size = int(math.sqrt(len(board)))
        newBoard = ''
        for i in range(size):
            boardString = board[(i*size):(i+1)*size]
            boardString = '?' + boardString + '?'
            newBoard += boardString
        newBoard = '??????????' + newBoard + '??????????'
    else:
        newBoard = board.replace('?', '')
    return list(newBoard)

def convert(index):
    x = index//8
    y = index%8
    return ((x*10)+1+10)+y

def possible_moves(board, token):
    board = convertBoard(board)
    if token == 'x':
        opponent = 'o'
    else:
        opponent = 'x'
    moveList = set()
    for row in range(9):
        for column in range(9):
            questionIndex = (10 * row) + column 
            if (board[questionIndex] == "."):
                for direction in directions:
                    opponentIndex = questionIndex + direction
                    while board[opponentIndex] == opponent:
                        opponentIndex += direction
                        if (board[opponentIndex] == token):
                            moveList.add((8 * (row-1)) + (column-1))
                            break
    return sorted(moveList)

def make_move(board, token, index):
    index = convert(index)
    board = convertBoard(board)
    size = int(math.sqrt(len(board)))
    board = list(board)
    x = index
    if token == 'x':
        opponent = 'o'
    else:
        opponent = 'x'
    moves = []
    flag = True
    while board[x] != '?':
        moves.append(x)
        x+=1
        if board[x] == '.':
            #print('hi')
            flag = False
        if board[x] == token and flag:
            for i in moves:
                board[i] = token
            break
    x = index
    moves = []
    flag = True
    while board[x] != '?':
        moves.append(x)
        x-=1
        if board[x] == '.':
            flag = False
        if board[x] == token and flag:
            for i in moves:
                board[i] = token
            break
    x = index
    moves = []
    flag = True
    while board[x] != '?':
        moves.append(x)
        x+=size
        if board[x] == '.':
            flag = False
        if board[x] == token and flag:
            for i in moves:
                board[i] = token
            break
    x = index
    moves = []
    flag = True
    while board[x] != '?':
        moves.append(x)
        x-=size
        if board[x] == '.':
            flag = False
        if board[x] == token and flag:
            for i in moves:
                board[i] = token
            break
    x = index
    moves = []
    flag = True
    while board[x] != '?':
        moves.append(x)
        x+=size+1
        if board[x] == '.':
            flag = False
        if board[x] == token and flag:
            for i in moves:
                board[i] = token
            break
    x = index
    moves = []
    flag = True
    while board[x] != '?':
        moves.append(x)
        x-=(size+1)
        if board[x] == '.':
            flag = False
        if board[x] == token and flag:
            for i in moves:
                board[i] = token
            break
    x = index
    moves = []
    flag = True
    while board[x] != '?':
        moves.append(x)
        x-=size
        x+=1
        if board[x] == '.':
            flag = False
        if board[x] == token and flag:
            for i in moves:
                board[i] = token
            break
    x = index
    moves = []
    flag = True
    while board[x] != '?':
        moves.append(x)
        x+=(size-1)
        if board[x] == '.':
            flag = False
        if board[x] == token and flag:
            for i in moves:
                board[i] = token
            break
    return ''.join(convertBoard(board))

def scoring(board, player):
    # g = game_over(board, player)
    # if g[0]:
    #     return g[1]
    if player == 'x':
        opponent = 'o'
    else:
        opponent = 'x'
    score = 0
    if len(possible_moves(board, player)) == 0 and len(possible_moves(board, opponent)) == 0:
        playerCount = board.count(player)
        opponentCount = board.count(opponent)
        if playerCount > opponentCount:
            return 1000000000000
        elif opponentCount > playerCount:
            return -100000000000
    corners = {
        0: {1, 8, 9},
        7: {6, 14, 15},
        56: {57, 48, 49},
        63: {62, 54, 55}
    }
    # edges = [2, 3, 4, 5, 16, 24, 32, 40, 58, 59, 60, 61, 23, 31, 39, 47]
    if player == 'x':
        opponent = 'o'
    else:
        opponent = 'x'
    

    score += len(possible_moves(board, player)) * 150
    score -= len(possible_moves(board, opponent)) * 150

    for corner in corners:
        if board[corner] == player:
            score += 5000   
        if board[corner] == opponent:
            score -= 5000
        for next_corners in corners[corner]:
            if board[next_corners] != '.':
                for cornerIndex in corners:
                    # if next_corners in corners[cornerIndex]:
                        if board[cornerIndex] == '.':
                            if board[next_corners] == player:
                                score -= 100

                            if board[next_corners] == opponent:
                                score += 100
                        # else:
                        #     if board[cornerIndex] == player:
                        #         if board[next_corners] == player:
                        #             score += 100
                        #     if board[cornerIndex] == opponent:
                        #         if board[next_corners] == opponent:
                        #             score -= 100
    # for edge in edges:
    #     if board[edge] == player:
    #         score += 2500
    #     if board[edge] == opponent:
    #         score -= 2500

    return -1*score

def game_over(board, player):
    if player == 'x':
        opponent = 'o'
    else:
        opponent = 'x'
    
    score = scoring(board, player)

    if len(possible_moves(board, player)) == 0 and len(possible_moves(board, opponent)) == 0:
        return [True, score]
    return [False, score]

def possible_next_boards(board, player):
    boards = []
    for move in possible_moves(board, player):
        boards.append((make_move(board, player, move), move))
    return boards

def negamax(board, player, depth, a, b):
    if player == "x":
        opponent = 'o'
    else:
        opponent = 'x'
    g = game_over(board, player)
    if g[0] or (depth == 0):
        return g[1]
    # if len(possible_moves(board, player)) == 0 or depth == 0:
    #     return scoring(board, player)
    value = float('-inf')
    for board in possible_next_boards(board, player):
        board2 = board[0]
        value = max(value, -1*negamax(board2, opponent, depth-1, -b, -a)) #alpha beta pruning here
        a = max(a, value) #alpha beta pruning here
        if a >= b: #alpha beta pruning here
            break #alpha beta pruning here
    return value

# class Strategy():

#    logging = True  # Optional

#    def best_strategy(self, board, player, best_move, still_running):

#        depth = 1

#        for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all

#            best_move.value = find_next_move(board, player, depth)
#            print(depth)

#            depth += 1

board = sys.argv[1]

player = sys.argv[2]

depth = 1

for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all
   print(find_next_move(board, player, depth))
   depth += 1

# results = []
# with open("boards_timing.txt") as f:
#     for line in f:
#         board, token = line.strip().split()
#         temp_list = [board, token]
#         print(temp_list)
#         for count in range(1, 7):
#             print("depth", count)
#             start = time.perf_counter()
#             find_next_move(board, token, count)
#             end = time.perf_counter()
#             temp_list.append(str(end - start))
#         print(temp_list)
#     print()
#     results.append(temp_list)
# with open("boards_timing_my_results.csv", "w") as g:
#     for l in results:
#         g.write(", ".join(l) + "\n")
