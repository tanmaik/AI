import math
inf = 100000000
ninf = -100000000
directions = [-11, -10, -9, -1, 1, 9, 10, 11]

def possible_moves(board, token):
    board = border(board, True)
    possibles = []
    if token == "o":
        opponent = "x"
    elif token == "x":
        opponent = "o"
    for index, char in enumerate(board):
        if char == token:
            for direction in directions:
                i = index
                if board[i + direction] != opponent:
                    continue
                while board[i+direction] == opponent:
                    i = i + direction
                if board[i + direction] == '.':
                    board = board[:i+direction] + "!" + board[i+direction+1:]
                else:
                    continue
    board = border(board, False)
    for index, char in enumerate(board):
        if char == "!":
            possibles.append(index)            
    return possibles

def make_move(board, token, index):
    new_board = board[:index] + "!" + board[index+1:]
    new_board = border(new_board, True)
    index = new_board.index("!")
    board = border(board, True)
    if token == "o":
        opponent = "x"
    elif token == "x":
        opponent = "o"
    board = board[:index] + token + board[index+1:]
    for direction in directions:
        i = index
        toFlip = []
        if board[i + direction] != opponent:
            continue
        while board[i + direction] == opponent:
            i = i + direction
            toFlip.append(i)
        if board[i + direction] == token:
            for flip in toFlip:
                board = board[:flip] + token + board[flip+1:]
        else:
            continue
    board = border(board, False)
    return board

def border(board, bord):
    if bord and "?" not in board:
        new_board = 10 * "?"
        for i in range(0, 8):
            new_board += ("?" + board[i*8: (i*8)+8] + "?")
        new_board += 10 * "?"
        return new_board
    else:
        new_board = ""
        for char in board:
            if char != "?":
                new_board += char
        return new_board

def print_board(board):
    N = int(math.sqrt(len(board)))
    s = ''
    for i in range(1, len(board) + 1):
        s += board[i - 1] + " "       
        if i % N == 0:
            s += "\n"
    print(s)

def find_next_move(board, player, depth):
    possible_indices = possible_moves(board, player)
    if player == 'x':
        scores = []
        for index in possible_indices:
            scores.append(min_step(make_move(board, player, index), depth, ninf, inf))
        return (possible_indices[scores.index(max(scores))])
    else:
        scores = []
        for index in possible_indices:
            scores.append(max_step(make_move(board, player, index), depth, ninf, inf))
        return (possible_indices[scores.index(min(scores))])

def score(board):
    corners_dict = {
        0: {1, 8, 9},
        7: {6, 14, 15},
        56: {57, 48, 49},
        63: {62, 54, 55}
    }
    score = (len(possible_moves(board, 'x')) - len(possible_moves(board, 'o'))) * 4000
    x_count = 0
    o_count = 0
    for piece in board:
        if piece == 'x':
            x_count += 1
        if piece == 'o':
            o_count += 1
    if len(possible_moves(board, 'o')) == 0 and len(possible_moves(board, 'x')) == 0:
        if x_count > o_count:
            return 1000000 + x_count - o_count
        if o_count < x_count:
            return -1000000 - o_count + x_count
        if x_count == o_count:
            return 0
    for corner in corners_dict:
        if board[corner] == 'x':
            score += 75000
        if board[corner] == 'o':
            score -= 75000
        for c in corners_dict[corner]:
            if board[c] == 'x' and board[corner] == '.':
                score -= 18000
            if board[c] == 'x' and board[corner] == 'x':
                score += 3000
            if board[c] == 'o' and board[corner] == 'o':
                score -= 3000
            if board[c] == 'o' and board[corner] == '.':
                score += 18000
    # if board.count('.') > 42:
    #     score -= int(x_count * 1.5)
    #     score += int(o_count * 1.5)
    # else:
    #     score += int(x_count * 1.5)
    #     score -= int(o_count * 1.5)
    return (score)

def possible_next_boards(board, token):
    boards = []
    for index in possible_moves(board, token):
        boards.append(make_move(board, token, index))
    return boards

def max_step(board, depth, alpha, beta):
    if depth == 1 or (len(possible_moves(board, 'x')) == 0 and len(possible_moves(board, 'o')) == 0):      
        return score(board)
    possible_nexts = possible_next_boards(board, 'x')
    if len(possible_nexts) == 0:
        return min_step(board, depth - 1, alpha, beta)           
    best = ninf
    for next_board in possible_nexts: 
        val = min_step(next_board, depth - 1, alpha, beta)
        best = max(best, val)
        alpha = max(alpha, best)

        if beta <= alpha:
            break
    return best
        

def min_step(board, depth, alpha, beta):
    if depth == 1 or (len(possible_moves(board, 'x')) == 0 and len(possible_moves(board, 'o')) == 0):      
        return score(board)
    possible_nexts = possible_next_boards(board, 'o')
    if len(possible_nexts) == 0:
        return max_step(board, depth - 1, alpha, beta)
    best = inf
    for next_board in possible_nexts:
        val = max_step(next_board, depth - 1, alpha, beta)
        best = min(best, val)
        beta = min(beta, best)

        if beta <= alpha:
            break
    return best

class Strategy():
    logging = True  # Optional
    def best_strategy(self, board, player, best_move, still_running):
        depth = 1
        for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all
            best_move.value = find_next_move(board, player, depth)
            print(f"Choosing {best_move.value} at depth {depth}.")
            depth += 1