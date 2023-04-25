import copy

global coords 
coords = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

def get_manhattan_dist(current_board):
    # take every value in my current board (except 0) and find the distance
    # between where it currently is and where its goal is
    dist = 0
    for i in range(1, 9):
        dist += abs(current_board[i][0] - coords[i - 1][0]) + abs(current_board[i][1] - coords[i - 1][1])
    print("manhattan dist: ", dist)
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
        print("ind1 ", ind1)
        print("ind2 ", ind2)
        if ind1 > ind2:
            return False
        elif ind2 > ind1:
            return True



# astar search
def astar(board):
    # initialize goal state, depth, steps, and path vars
    goal_board = [[2,2],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1]]
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
    print("initialize")
    dist = get_manhattan_dist(start_board)
    # test_board = [[2,2],[2,1],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[0,0]]
    frontier.append([start_board, 0, dist, dist, []])
    # frontier.append([test_board, 0, dist, dist, []])
    print('frontier: ', frontier)

    cap = 0
    print("enter loop")
    while len(frontier) > 0 and cap < 1:
        # increment steps
        steps += 1
        print(steps)
        # go through each node in fronteir and look for the one with the lowest f(n)
        best_node_ind = 0
        for i in range(1, len(frontier)):
            # if its the same then tiebreak
            if frontier[i][3] == frontier[best_node_ind][3]:
                if tiebreak(frontier[best_node_ind][0], frontier[i][0]) == True:
                    best_node_ind = i
            # if it is less than the current best_node_ind save the index
            elif frontier[i][3] < frontier[best_node_ind][3]:
                best_node_ind = i
        # check if this node is the goal state, if it is return the info
        if get_manhattan_dist(frontier[best_node_ind][0]) == 0:
            depth = frontier[best_node_ind][1]
            path = frontier[best_node_ind][4]
            break
        else:
            print("yay it knows not to end")
        # if it isn't the goal state then expand the node into children
        cap +=1

        
    # # if the board is in its goal state
    # while current_board != goal_board:
    #     print("yay")
    #     current_board = goal_board

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



