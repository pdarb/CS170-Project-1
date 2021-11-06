from eightPuzzle import Puzzle
from eightPuzzle import MoveDirection


# def uniform_cost_algorithm():



# def misplaced_tile_algorithm():



# def manhattan_distance_algorithm():







if __name__== '__main__':


    matrix = []

    input_string = input('Enter first row: ')
    user_list = input_string.split()

    for i in range(len(user_list)):
        # convert each item to int type
        user_list[i] = int(user_list[i])

    matrix.append(user_list)

    input_string = input('Enter second row: ')
    user_list = input_string.split()

    for i in range(len(user_list)):
        # convert each item to int type
        user_list[i] = int(user_list[i])

    matrix.append(user_list)

    input_string = input('Enter third row: ')
    user_list = input_string.split()

    for i in range(len(user_list)):
        # convert each item to int type
        user_list[i] = int(user_list[i])

    matrix.append(user_list)

    for i in matrix:
        for j in i:
            print(j, end=' ')
        print(' ')

    for i in range(len(user_list)):
        if user_list[i] == 0:
            print(int(user_list[i]))
    #else

    algChoice = int(input('Choose: \n(1) Uniform Cost \n(2) Misplaced Tiles \n(3) Manhattan Distance\n'))

    game = Puzzle(matrix)
    #d = MoveDirection()

    if algChoice == 2:
        game.misplaced_tile_heuristic()

    if algChoice == 3:
        game.manhattan_dist_heuristic()

    game.find_zero_index()

    game.direction_result(matrix, MoveDirection.Up)    

   # game.find_zero_index()

    game.print_initial_state()

    



    #depth: 3
    #game = Puzzle([['1', '2', '3'], ['0', '4', '6'], ['7', '5', '8']])

