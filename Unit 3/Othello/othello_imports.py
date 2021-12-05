from math import sqrt
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
    N = int(sqrt(len(board)))
    s = ''
    for i in range(1, len(board) + 1):
        s += board[i - 1] + " "       
        if i % N == 0:
            s += "\n"
    print(s)

