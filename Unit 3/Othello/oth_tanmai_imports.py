from othello_imports import possible_moves, make_move
import sys

board = sys.argv[1]
player = sys.argv[2]

def score(board):
    corners_dict = {
        0: {1, 8, 9},
        7: {6, 14, 15},
        56: {57, 48, 49},
        63: {62, 54, 55}
    }

    score = (len(possible_moves(board, 'x')) - len(possible_moves(board, 'o'))) * 1000
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
            score += 50000
        if board[corner] == 'o':
            score -= 50000
        for c in corners_dict[corner]:
            if board[c] == 'x':
                score -= 2000
            if board[c] == 'o':
                score += 2000
    score += int(x_count * 1.5)
    score -= int(o_count * 1.5)
    return score


def possible_next_boards(board, token):
    boards = []
    for index in possible_moves(board, token):
        boards.append(make_move(board, token, index))
    return boards

def max_step(board, depth):
    if depth == 0 or (possible_moves(board, 'x') == 0 and possible_moves(board, 'o') == 0):      
        return score(board)
    possible_nexts = possible_next_boards(board, 'x')
    if len(possible_nexts) == 0:
        return min_step(board, depth - 1)           
    results = list()
    for next_board in possible_nexts: 
        results.append(min_step(next_board, depth - 1))
    return max(results)

def min_step(board, depth):
    if depth == 0 or (possible_moves(board, 'x') == 0 and possible_moves(board, 'o') == 0):      
        return score(board)
    possible_nexts = possible_next_boards(board, 'o')
    if len(possible_nexts) == 0:
        return max_step(board, depth - 1)
    results = list()
    for next_board in possible_nexts:
        results.append(max_step(next_board, depth - 1))
    return min(results)


for depth in range(1, 100000):
    possible_indices = possible_moves(board, player)
    if player == 'x':
        scores = []
        for index in possible_indices:
            scores.append(min_step(make_move(board, player, index), depth))
        print(possible_indices[scores.index(max(scores))])
    else:
        scores = []
        for index in possible_indices:
            scores.append(max_step(make_move(board, player, index), depth))
        print(possible_indices[scores.index(min(scores))])

