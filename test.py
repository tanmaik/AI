import sys

board = '.........'

def isEmpty(board):
    for space in board:
        if space != ".":
            return False
    return True

if isEmpty(board):
    ai_player = input("Should I be X or O? ")
    if ai_player == "O":
        player = "X"
    elif ai_player == "X":
        player = "O"
    else:
        print()
        print("Please choose a valid player.")
        exit()
else:
    x_count = 0
    o_count = 0
    for space in board:
        if space == "X":
            x_count += 1
        elif space == "O":
            o_count += 1
    if x_count <= o_count:
        ai_player = "X"
        player = "O"
    else:
        ai_player = "O"
        player = "X"

def find_current_player(board):
    x_count = 0
    o_count = 0
    for space in board:
        if space == "X":
            x_count += 1
        elif space == "O":
            o_count += 1
    if x_count <= o_count:
        return "X"
    else:
        return "O"

def print_board(board):
    i = 1
    toPrint = "\nCurrent board: \n"
    for index, space in enumerate(board):
        toPrint += space
        if i == 3:
            indices = f"{index - 2}{index - 1}{index}"
            toPrint += f'    {indices}\n'
            i = 0
        i += 1
    return toPrint

def game_over(board):
    win_spots = ["012", "345", "678", "036", "147", "258", "048", "246"]
    score = 0
    for elem in win_spots:
        if board[int(elem[0])] == board[int(elem[1])] and board[int(elem[1])] == board[int(elem[2])] and board[int(elem[0])] == board[int(elem[2])] and board[int(elem[0])] != "." and board[int(elem[1])] != "." and board[int(elem[2])] != ".":
            if board[int(elem[0])] == 'O':
                score = -1
            elif board[int(elem[0])] == 'X':
                score = 1
            return True, score
    if not '.' in board:
        return True, score
    return False, None

def ai_move(board):
    if ai_player == "X":
        possibilites = possible_next_boards(board, ai_player)
        moves = [(elem[0], min_step(elem[0]), elem[1]) for elem in possibilites]
        wins = []
        for move in moves:
            if move[1] == 1:
                print(f"Moving at {move[2]} results in a win.")
            elif move[1] == -1:
                print(f"Moving at {move[2]} results in a loss.")
            elif move[1] == 0:
                print(f"Moving at {move[2]} results in a tie.")
            wins.append((move[1], move[0], move[2]))
        print()
        choice = max(wins)
        print(f"I choose space {choice[2]}.")
        return choice[1]
    elif ai_player == "O":
        possibilites = possible_next_boards(board, ai_player)
        moves = [(elem[0], max_step(elem[0]), elem[1]) for elem in possibilites]
        wins = []
        for move in moves:
            if move[1] == -1:
                print(f"Moving at {move[2]} results in a win.")
            elif move[1] == 1:
                print(f"Moving at {move[2]} results in a loss.")
            elif move[1] == 0:
                print(f"Moving at {move[2]} results in a tie.")
            wins.append((move[1], move[0], move[2]))
        print()
        choice = min(wins)
        print(f"I choose space {choice[2]}.")
        return choice[1]
    return None

def max_step(board):
    if game_over(board)[0]:    
        return game_over(board)[1]                           
    results = list()
    for next_board in possible_next_boards(board, 'X'): 
        results.append(min_step(next_board[0]))
    return max(results)

def min_step(board):
    if game_over(board)[0]:
        return game_over(board)[1]
    results = list()
    for next_board in possible_next_boards(board, 'O'):
        results.append(max_step(next_board[0]))
    return min(results)

def possible_next_boards(board, current_player):
    possibilites = []
    blank_indices = []
    for index, space in enumerate(board):
        if space == ".":
            blank_indices.append(index)
    for index in blank_indices:
        temp_board = board[:index] + current_player + board[index + 1:]
        possibilites.append((temp_board, index))
    return possibilites
