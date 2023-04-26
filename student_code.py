import copy
import time

global coords
coords = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

def get_manhattan_dist(current_board):
    # take every value in my current board (except 0) and find the distance
    # between where it currently is and where its goal is
    dist = 0
    for i in range(1, 9):
        dist += abs(current_board[i][0] - coords[i - 1][0]) + abs(current_board[i][1] - coords[i - 1][1])
    return dist

def tiebreak(board1, board2):
    ind1 = -1
    ind2 = -1
    for ind in coords:
        for i in range(9):
            if board1[i] == ind:
                ind1 = i
            if board2[i] == ind:
                ind2 = i
        if ind1 > ind2:
            return False
        elif ind2 > ind1:
            return True

def add_node(parent, direction):
    # child = parent
    # get the current coordinate of 0
    zero_coord = parent[0][0]
    # if direction is 0 move the 0 space up
    if direction == 0:
        new_board = parent[0][:]
        goal_coord = [zero_coord[0] - 1, zero_coord[1]]
        # look through the board for the value currently at the goal coord
        for i in range(9):
            # once found update the new board
            if new_board[i] == goal_coord:
                new_board[i] = zero_coord
                new_board[0] = goal_coord
                break
        man_dist = get_manhattan_dist(new_board)
        new_depth = parent[1] + 1
        new_moves = parent[4][:]
        new_moves.append(direction)
        return [new_board, new_depth, man_dist, new_depth + man_dist, new_moves]
    # if direction is 1 move the 0 space right
    elif direction == 1:
        new_board = parent[0][:]
        goal_coord = [zero_coord[0], zero_coord[1] + 1]
        # look through the board for the value currently at the goal coord
        for i in range(9):
            # once found update the new board
            if new_board[i] == goal_coord:
                new_board[i] = zero_coord
                new_board[0] = goal_coord
                break
        man_dist = get_manhattan_dist(new_board)
        new_depth = parent[1] + 1
        new_moves = parent[4][:]
        new_moves.append(direction)
        return [new_board, new_depth, man_dist, new_depth + man_dist, new_moves]
    # if direction is 2 move the 0 space down
    elif direction == 2:
        new_board = parent[0][:]
        goal_coord = [zero_coord[0] + 1, zero_coord[1]]
        # look through the board for the value currently at the goal coord
        for i in range(9):
            # once found update the new board
            if new_board[i] == goal_coord:
                new_board[i] = zero_coord
                new_board[0] = goal_coord
                break
        man_dist = get_manhattan_dist(new_board)
        new_depth = parent[1] + 1
        new_moves = parent[4][:]
        new_moves.append(direction)
        return [new_board, new_depth, man_dist, new_depth + man_dist, new_moves]
    # if direction is 3 move the 0 space left
    if direction == 3:
        new_board = parent[0][:]
        goal_coord = [zero_coord[0], zero_coord[1] - 1]
        # look through the board for the value currently at the goal coord
        for i in range(9):
            # once found update the new board
            if new_board[i] == goal_coord:
                new_board[i] = zero_coord
                new_board[0] = goal_coord
                break
        man_dist = get_manhattan_dist(new_board)
        new_depth = parent[1] + 1
        new_moves = parent[4][:]
        new_moves.append(direction)
        return [new_board, new_depth, man_dist, new_depth + man_dist, new_moves]
    # return child

# astar search
def astar(board):
    start_time = time.time()
    # initialize goal state, depth, steps, and path vars
    explored = []
    frontier = []
    steps = 0
    # find the loaction of all my values in the board
    start_board = []
    # go from 0-8
    for i in range(9):
        # go through the board and record the location of each number
        for j in range(len(board)):
            if board[j] == (i):
                start_board.append(coords[j])

    # create the first node ([board, depth, man_dist, f(n), path])
    dist = get_manhattan_dist(start_board)
    frontier.append([start_board, 0, dist, dist, []])

    while len(frontier) > 0:
        # increment steps
        steps += 1
        # go through each node in fronteir and look for the one with the lowest f(n)
        best_node_ind = 0
        for i in range(1, len(frontier)):
            # if its the same then tiebreak
            if frontier[i][3] < frontier[best_node_ind][3]:
                best_node_ind = i
            # if it is less than the current best_node_ind save the index
            elif frontier[i][3] == frontier[best_node_ind][3]:
                if tiebreak(frontier[best_node_ind][0], frontier[i][0]) == True:
                    best_node_ind = i
        # check if this node is the goal state, if it is return the info
        best_node = frontier[best_node_ind]
        if get_manhattan_dist(best_node[0]) == 0:
            depth = best_node[1]
            path = best_node[4]
            break
        else:
            # check if this node had already been expanded
            found = False
            for node in explored:
                if node[0] == best_node[0]:
                    # del frontier[best_node_ind]
                    found = True
                    steps -= 1
            # if the node was not found in explored then get its children and add them
            if found == False:
                # create variables to make it readable
                x = best_node[0][0][1]
                y = best_node[0][0][0]
                if y > 0:
                    check = False
                    new_node = add_node(best_node, 0)
                    for node in explored:
                        if node[0] == new_node[0]:
                            check = True
                    if check == False:
                        frontier.append(new_node)
                if x < 2:
                    check = False
                    new_node = add_node(best_node, 1)
                    for node in explored:
                        if node[0] == new_node[0]:
                            check = True
                    if check == False:
                        frontier.append(new_node)
                if y < 2:
                    check = False
                    new_node = add_node(best_node, 2)
                    for node in explored:
                        if node[0] == new_node[0]:
                            check = True
                    if check == False:
                        frontier.append(new_node)
                if x > 0:
                    check = False
                    new_node = add_node(best_node, 3)
                    for node in explored:
                        if node[0] == new_node[0]:
                            check = True
                    if check == False:
                        frontier.append(new_node)
            # append this board to explored
            explored.append(best_node)
            # delete the current node and all other nodes that have the same board
            board_to_delete = best_node[0][:]
            del frontier[best_node_ind]
            for i in range(len(frontier) - 1, 0, -1):
                if frontier[i][0] == board_to_delete:
                    del frontier[i]

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
    return depth, steps, path


#graphic print of board, feel free to use, or not
def print_board(board):
    print("\n")
    print("------------")
    print(
        "{:02d}".format(board[0]),
        "|",
        "{:02d}".format(board[1]),
        "|",
        "{:02d}".format(board[2]),
    )
    print("------------")

    print(
        "{:02d}".format(board[3]),
        "|",
        "{:02d}".format(board[4]),
        "|",
        "{:02d}".format(board[5]),
    )
    print("------------")

    print(
        "{:02d}".format(board[6]),
        "|",
        "{:02d}".format(board[7]),
        "|",
        "{:02d}".format(board[8]),
    )
    print("------------")



