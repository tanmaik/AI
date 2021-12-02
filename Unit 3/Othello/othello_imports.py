directions = [-11, -10, -9, -1, 1, 9, 10, 11]

def possible_moves(board, token):
    # assuming board has question marks
    if token == "o":
        opponent = "x"
    elif token == "x":
        opponent = "o"
    for char in board:
        

def border(board):
    toPut = True
    if '?' in board:
        toPut = False
    if toPut:
        new_board = 10 * "?"
        for i in range(0, 7):
            new_board += ("?" + board[i*8: (i*8)+8] + "?")
        new_board += 10 * "?"
        return new_board
    # return new_board

def print_board(board):
    boardQ = border(board)
    size = len(boardQ)**(1/2)
    final_board = ""
    for index, char in enumerate(boardQ):
        if index % 10 == 0 and index != 0:
            final_board += "\n"
        final_board += char + " "
    print(final_board)

print_board("...........................ox......xo...........................")