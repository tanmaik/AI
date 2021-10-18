# import sys
from collections import deque
board_size = 6


def get_num_cars(board):
    alphabet = "ABCDEFGHIJKX"
    count = 0
    for a in alphabet:
        if a in board:
            count += 1
    return count


def make2d(board):
    board_2d = []
    count = 0
    for i in range(6):
        temp = []
        for j in range(6):
            temp.append(board[count])
            count += 1
        board_2d.append(temp)
    return board_2d


def find2d(board2d, char):
    first = 0
    second = 0
    for arr in board2d:
        for elem in arr:
            if elem == char:
                return first, second
            second += 1
        second = 0
        first += 1
    return -1, -1


def find_cars(board):
    cars = dict()
    temp = board
    horizontal = False
    alphabet = "ABCDEFGHIJK"
    num_cars = get_num_cars(board)
    alphabet = alphabet[:num_cars-1] + 'X'
    for i in range(num_cars):
        car = alphabet[i]
        car_size = 0
        first_pos = 0
        car_xspots = dict()
        car_yspots = dict()
        while car in temp:
            car_size += 1
            pos = temp.index(car)
            temp = temp[0:pos] + "-" + temp[pos+1: len(temp)]
            x = pos % board_size
            y = pos // board_size
            if car_size == 1:
                first_pos = pos
                beg_x = x
                beg_y = y
                beginning_xy = str(x) + str(y)
            if x in car_xspots:
                car_yspots[y] = x
                horizontal = False
            elif y in car_yspots:
                car_xspots[x] = y
                horizontal = False
            else:
                car_xspots[x] = y
                horizontal = True

        cars[car] = (horizontal, car_size, first_pos)
    return cars


def get_children(board):
    children = []
    cars = find_cars(board)
    for i in cars:
        horizontal, size, first_pos = cars[i]
        if horizontal == False:
            beg_y = first_pos // board_size
            end = first_pos + ((size-1) * 6)
            end_y = end // board_size
            new_up = first_pos - 6
            new_downend = end + 6
            if (beg_y != 0) and (board[new_up] == "-"):  # move up one
                new_end = new_up + ((size-1) * 6)
                child = board[0:new_up] + i + board[new_up +
                                                    1: end] + "-" + board[end + 1: len(board)]
                children.append(child)
                if (beg_y - 1 != 0) and (board[new_up-6] == "-"):  # move up two
                    new_up = new_up - 6
                    #up_twoend = up_two -((size-1)*6)
                    child2 = child[0:new_up] + i + child[new_up +
                                                         1: new_end] + "-" + child[new_end + 1: len(board)]
                    # print(print_puzzle(child))
                    # print()
                    children.append(child2)
                    # move up three
                    if (beg_y - 2 != 0) and (board[new_up - 6] == "-"):
                        up_threeend = new_up + ((size-1)*6)
                        new_up = new_up - 6
                        #up_two = new_up - 6
                        child3 = child2[0:new_up] + i + child2[new_up +
                                                               1: up_threeend] + "-" + child2[up_threeend + 1: len(board)]
                        # print(print_puzzle(child))
                        # print()
                        children.append(child3)
##########################################################################################################################
                   # move down
            if (end_y < board_size-1):
                if (board[new_downend] == "-"):
                    new_down_y = first_pos + 1
                    child = board[0:first_pos] + "-" + board[first_pos +
                                                             1: new_downend] + i + board[new_downend + 1: len(board)]
                    children.append(child)
                    if (end_y + 1 < board_size - 1):  # move down two
                        if (board[new_downend + 6] == "-"):
                            down_two = new_downend - ((size-1) * 6)
                            down_twoend = new_downend + 6
                            child2 = child[0:down_two] + "-" + child[down_two +
                                                                     1: down_twoend] + i + child[down_twoend + 1: len(child)]
                            children.append(child2)
                            if (end_y + 2 < board_size - 1):
                                if (board[new_downend + 12] == "-"):  # move down three
                                    down_three = down_two + 6
                                    down_threeend = down_twoend + 6
                                    child3 = child2[0:down_three] + "-" + child2[down_three +
                                                                                 1: down_threeend] + i + child2[down_threeend + 1: len(child2)]
                                    children.append(child3)
               # horizontal cars (left and right moves)
        else:
            beg_x = first_pos % board_size
            end = first_pos + size - 1
            end_x = beg_x + size - 1
            new_left = first_pos-1
            new_rightend = end + 1
            if (beg_x > 0) and (board[new_left] == "-"):  # move Left
                new_leftend = end - 1
                child = board[0: new_left] + i + \
                    board[first_pos: end] + "-" + board[end + 1:len(board)]
                # print(print_puzzle(child))
                # print()
                children.append(child)
            # move Left two
            if (beg_x > 0) and (board[new_left] == "-") and (beg_x - 1 > 0) and (board[new_left-1] == "-"):
                left_two = first_pos - 2
                #left_twoend = left_two + size
                child = board[0:left_two] + i + board[first_pos: end] + \
                    "-" + "-" + board[end+1: len(board)]
                # print(print_puzzle(child))
                # print()
                children.append(child)
                # move Left two
                if (beg_x != 0) and (board[new_left] == "-") and (beg_x - 1 != 0) and (board[new_left-1] == "-") and (beg_x - 2 != 0) and (board[new_left - 2] == "-"):
                    left_two = first_pos - 2
                    left_three = left_two - 1
                    #left_twoend = left_two + size
                    child = board[0:left_three] + i + board[first_pos: end] + \
                        "-" + "-" + "-" + board[end+1: len(board)]
                    # print(print_puzzle(child))
                    # print()
                    children.append(child)
            if (end_x < board_size-1) and (new_rightend < len(board)):
                if (board[new_rightend] == "-"):  # move Right
                    new_right = first_pos + 1
                    child = board[0: first_pos] + "-" + board[new_right: new_rightend] + \
                        i + board[new_rightend + 1: len(board)]
                    # print(print_puzzle(child))
                    # print()
                    children.append(child)
            if (end_x < board_size-1) and (new_rightend < len(board)):
                if (board[new_rightend] == "-") and (end_x + 1 < board_size-1) and (new_rightend + 1 < len(board)):
                    if (board[new_rightend + 1] == "-"):  # move Right two
                        right_two = new_right + 1
                        right_twoend = right_two + size
                        child = board[0:first_pos] + "-" + "-" + \
                            board[first_pos: end] + i + \
                            board[right_twoend: len(board)]
                        # print(print_puzzle(child))
                        # print()
                        children.append(child)
            if (end_x < board_size-1) and (new_rightend < len(board)):
                if (board[new_rightend] == "-") and (end_x + 1 < board_size-1) and (new_rightend + 1 < len(board)):
                    if (board[new_rightend + 1] == "-") and (end_x + 2 < board_size - 1) and (new_rightend + 2 < len(board)):
                        if (board[new_rightend + 2] == "-"):  # move Right three
                            right_two = new_right + 1
                            right_twoend = right_two + size
                            right_three = right_two + 1
                            right_threeend = right_twoend + 1
                            child = board[0: first_pos] + "-" + "-" + "-" + \
                                board[first_pos: end] + i + \
                                board[right_threeend: len(board)]
                            # print(print_puzzle(child))
                            # print()
                            children.append(child)
    return children


def goal_test(board):
    if make2d(board)[2][5] == 'X':
        return True
    else:
        return False


def print_puzzle(puzzle):
    size = 6
    final_puzzle = ""
    for index, char in enumerate(puzzle):
        final_puzzle += char
        if (((index + 1) % size) == 0) and index != ((size**2)-1):
            final_puzzle += "\n"
        else:
            final_puzzle += " "
    return final_puzzle


def BFS(start_node):
    fringe = deque()
    visited = {start_node}
    fringe.append((start_node, 0, None))
    while fringe:
        v = fringe.popleft()
        if goal_test(v[0]):
            return v
        for c in get_children(v[0]):
            if c not in visited:
                fringe.append((c, v[1] + 1, v))
                visited.add(c)
    return None


# example_start = "AA---BC--D-BCXXD-BC--D--E---FFE-GGG-"
example_start = "---A-----ABBXX-D--E-FDGGE-FHHIE-F--I"


def print_path(v):
    print_order = []
    print_order.append(v[0])
    while v != None:
        v = v[2]
        if v != None:
            print_order.append(v[0])
    path_length = len(print_order) - 1
    print_order = print_order[::-1]
    path = "\n"
    for index, elem in enumerate(print_order):
        path += ("State %s: \n" % index) + (print_puzzle(elem))
        path += ("\n\n")
    return (path, path_length)


print(print_path(BFS(example_start))[0])
