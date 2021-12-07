from othello_imports import possible_moves, make_move
import sys
import random

board = sys.argv[1]
player = sys.argv[2]

corners_dict = {
    0: {1, 8, 9},
    7: {6, 14, 15},
    56: {57, 48, 49},
    63: {62, 54, 55}
}


def score(board):
    score = (len(possible_moves(board, 'x')) - len(possible_moves(board, 'o'))) * 100
    if len(possible_moves(board, 'o')) == 0 and len(possible_moves(board, 'x')) == 0:
        x_count = 0
        o_count = 0
        for piece in board:
            if piece == 'x':
                x_count += 1
            if piece == 'o':
                o_count += 1
        if x_count > o_count:
            return 1000000 + x_count - o_count
        if o_count < x_count:
            return -1000000 - o_count + x_count
        if x_count == o_count:
            return 0
    for corner in corners_dict:
        if board[corner] == 'x':
            score += 1000
        if board[corner] == 'o':
            score -= 1000
        for c in corners_dict[corner]:
            if board[c] == 'x':
                score -= 200
            if board[c] == 'o':
                score += 200
    score += x_count
    score -= o_count
    return score


print(random.choice(possible_moves(board, player)))