from eightPuzzle import Puzzle, MoveDirection
from queue import Queue, PriorityQueue


def uniform_cost_algorithm(game):

    print('Entered Uniform cost alg')

    depth = 0
    q = Queue()
    q.put(game)
   
    while not q.empty():

        #depth += 1

        startGame = q.get()  #pops first node and stores it in startGame var.

        if startGame.goal_test(): #checks if curr_state = goal_state
            print('Solved using Uniform Cost!')
            return 

        #checks all possible direction moves
        try:
            newGame = Puzzle(startGame)
            newMove = newGame.direction_result(newGame.gameState, MoveDirection.Up)
            q.put(newMove)

        except:
            pass

        try:
            print('checking down')
            newGame = Puzzle(startGame)
            newMove = newGame.direction_result(newGame.gameState, MoveDirection.Down)
            q.put(newMove)

        except:
            pass

        try:
            print('checking left')
            newGame = Puzzle(startGame)
            newMove = newGame.direction_result(newGame.gameState, MoveDirection.Left)
            q.put(newMove)

        except:
            pass

        try:
            print('checking right')
            newGame = Puzzle(startGame)
            newMove = newGame.direction_result(newGame.gameState, MoveDirection.Right)
            q.put(newMove)

        except:
            pass
 


def misplaced_tile_algorithm(game):

    depth = 0
    q = PriorityQueue()
    q.put(game)

    while not q.empty():

        depth += 1

        startGame = q.get()  #pops first node and stores it in startGame var.

        if startGame.goal_test(): #checks if curr_state = goal_state
            print('Solved using Misplaced Tile!!')
            return

        #check all possible direction moves
        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Up)
            if newMove:
                newMove = Puzzle(newMove)
                print('up', newMove.startState)
                newMove.h = newMove.misplaced_tile_heuristic()
                newMove.f = depth + newMove.h
                print('h', newMove.h)
                print('f', newMove.f)
                q.put(newMove)

        except:
            pass

        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Down)
            if newMove:
                newMove = Puzzle(newMove)
                print('down', newMove.startState)
                newMove.h = newMove.misplaced_tile_heuristic()
                newMove.f = depth + newMove.h
                print('h', newMove.h)
                print('f', newMove.f)
                q.put(newMove)

        except:
            pass

        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Left)
            if newMove:
                newMove = Puzzle(newMove)
                print('left', newMove.startState)
                newMove.h = newMove.misplaced_tile_heuristic()
                newMove.f = depth + newMove.h
                print('h', newMove.h)
                print('f', newMove.f)
                q.put(newMove)

        except:
            pass

        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Right)
            if newMove:
                newMove = Puzzle(newMove)
                print('right', newMove.startState)
                newMove.h = newMove.misplaced_tile_heuristic()
                newMove.f = depth + newMove.h
                print('h', newMove.h)
                print('f', newMove.f)
                q.put(newMove)
        except:
            pass



        bestMove=''
        leastScore=100000000
    
        for move in q.queue:
            if move.f < leastScore:
                bestMove = move
                leastScore = move.f
        
        print('BestMove =>>', bestMove.gameState)
        q = PriorityQueue()
        q.put(bestMove)

    



def manhattan_distance_algorithm(game):
    
    depth = 0
    q = PriorityQueue()
    q.put(game)
    print(q.qsize())

    while not q.empty():

        depth += 1

        startGame = q.get()  #pops first node and stores it in startGame var.

        if startGame.goal_test(): #checks if curr_state = goal_state
            print('Solved using Manhattan Distance!!')
            return

        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Up)
            if newMove:
                newMove = Puzzle(newMove)
                print('up', newMove.startState)
                newMove.h = newMove.manhattan_dist_heuristic()
                newMove.f = depth + newMove.h
                print('h', newMove.h)
                print('f', newMove.f)
                q.put(newMove)

        except:
            pass

        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Down)
            if newMove:
                newMove = Puzzle(newMove)
                print('down', newMove.startState)
                newMove.h = newMove.manhattan_dist_heuristic()
                newMove.f = depth + newMove.h
                print('h', newMove.h)
                print('f', newMove.f)
                q.put(newMove)


        except:
            pass

        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Left)
            if newMove:
                newMove = Puzzle(newMove)
                print('left', newMove.startState)
                newMove.h = newMove.manhattan_dist_heuristic()
                newMove.f = depth + newMove.h
                print('h', newMove.h)
                print('f', newMove.f)
                q.put(newMove)

        except:
            pass

        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Right)
            if newMove:
                newMove = Puzzle(newMove)
                print('right', newMove.startState)
                newMove.h = newMove.manhattan_dist_heuristic()
                newMove.f = depth + newMove.h
                print('h', newMove.h)
                print('f', newMove.f)
                q.put(newMove)

        except:
            pass


        bestMove=''
        leastScore=100000000
    
        for move in q.queue:
            if move.f < leastScore:
                bestMove = move
                leastScore = move.f
        
        print('BestMove =>>', bestMove.gameState)
        q = PriorityQueue()
        q.put(bestMove)






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

    if algChoice == 1:
        uniform_cost_algorithm(game)

    if algChoice == 2:
        misplaced_tile_algorithm(game)

    if algChoice == 3:
        manhattan_distance_algorithm(game)





    #game.find_zero_index()

    #game.direction_result(matrix, MoveDirection.Up)    

    #game.misplaced_tile_heuristic()
    #game.manhattan_dist_heuristic()

    # game.print_initial_state()

    



    #depth: 3
    #game = Puzzle([['1', '2', '3'], ['0', '4', '6'], ['7', '5', '8']])

