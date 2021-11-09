import time
from eightPuzzle import Puzzle, MoveDirection
from queue import Queue, PriorityQueue
from dataclasses import dataclass, field
from typing import Any


maxTimeout = 30

## From StackOverflow 
@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)


def uniform_cost_algorithm(game):

    startTime = time.time()

    q = Queue()
    q.put(game)
    max_queue = 1
    nodeExpand = 1

    while not q.empty():
        
        queue_size = max(max_queue, q.qsize())

        startGame = q.get()
        print('depth:', startGame.g)

        nodeExpand += 1



        # Prints gameState in matrix format
        print('Current State:')
        for i in startGame.gameState:
            for j in i:
                print(j, end=' ')
            print(' ')

        
        print('g(n)', startGame.g)

        # Checks if curr_state = goal_state
        if startGame.goal_test():
            print('Solved using Uniform Cost!')
            print('Final Solution:')
            for i in startGame.gameState:
                for j in i:
                    print(j, end=' ')
                print(' ')

            print('Reached solution at a depth of ', startGame.g)
            endTime = time.time()
            print('Completion Time:', round(endTime - startTime, 3))
            print('# of nodes expanded:', nodeExpand)
            print('Max Queue Size:', queue_size)
            

            return 


        # Checks all possible direction moves
        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Up)
            if newMove:
                newMove = Puzzle(newMove)
                #print('up', newMove.startState)
                newMove.g = 1 + startGame.g
                q.put(newMove)

        except:
            pass

        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Down)
            if newMove:
                newMove = Puzzle(newMove)
                #print('down', newMove.startState)
                newMove.g = 1 + startGame.g
                q.put(newMove)

        except:
            pass

        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Left)
            if newMove:
                newMove = Puzzle(newMove)
                #print('left', newMove.startState)
                newMove.g = 1 + startGame.g
                q.put(newMove)

        except:
            pass

        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Right)
            if newMove:
                newMove = Puzzle(newMove)
                #print('right', newMove.startState)
                newMove.g = 1 + startGame.g
                q.put(newMove)

        except:
            pass


        currentTime = time.time()
        # print(currentTime - startTime)

        if (currentTime - startTime) > maxTimeout:
            print('Code has timed out in ', maxTimeout, ' secs')
            quit()



def misplaced_tile_algorithm(game):

    startTime = time.time()

    #Uses PrioritzedItem class to order matrices from lowest heuristic (high priority) to hishest
    q = PriorityQueue()
    q.put(PrioritizedItem(game.misplaced_tile_heuristic(), game))
    game.h = game.misplaced_tile_heuristic()
    game.f = 0 + game.h

    max_queue = 1
    nodeExpand = 1

    while not q.empty():

        queue_size = max(max_queue, q.qsize())

        startGame = q.get().item  #pops first node and stores it in startGame var.
        print('depth:', startGame.g)

        nodeExpand += 1

        # Prints gameState in matrix format
        print('Current State:')
        for i in startGame.gameState:
            for j in i:
                print(j, end=' ')
            print(' ')

        print('h(n)', startGame.h)
        print('f(n)', startGame.f)
    

        # Checks if curr_state = goal_state
        if startGame.goal_test():
            print('Solved using Misplaced Tile!!')

            print('Final Solution:')
            for i in startGame.gameState:
                for j in i:
                    print(j, end=' ')
                print(' ')

            print('Reached solution at a depth of ', startGame.g)
            endTime = time.time()
            print('Completion Time:', round(endTime - startTime, 3))
            print('# of nodes expanded:', nodeExpand)
            print('Max Queue Size:', queue_size)
            

            return

        # Checks all possible direction moves
        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Up)
            if newMove:
                newMove = Puzzle(newMove)
                #print('up', newMove.startState)
                newMove.h = newMove.misplaced_tile_heuristic()
                newMove.g = 1 + startGame.g
                newMove.f = newMove.g + newMove.h
                # print('h(n)', newMove.h)
                # print('f(n)', newMove.f)
                q.put(PrioritizedItem(newMove.f, newMove))

        except:
            pass

        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Down)
            if newMove:
                newMove = Puzzle(newMove)
                #print('down', newMove.startState)
                newMove.h = newMove.misplaced_tile_heuristic()
                newMove.g = 1 + startGame.g
                newMove.f = newMove.g + newMove.h
                # print('h(n)', newMove.h)
                # print('f(n)', newMove.f)
                q.put(PrioritizedItem(newMove.f, newMove))

        except:
            pass

        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Left)
            if newMove:
                newMove = Puzzle(newMove)
                #print('left', newMove.startState)
                newMove.h = newMove.misplaced_tile_heuristic()
                newMove.g = 1 + startGame.g
                newMove.f = newMove.g + newMove.h
                # print('h(n)', newMove.h)
                # print('f(n)', newMove.f)
                q.put(PrioritizedItem(newMove.f, newMove))

        except:
            pass

        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Right)
            if newMove:
                newMove = Puzzle(newMove)
                #print('right', newMove.startState)
                newMove.h = newMove.misplaced_tile_heuristic()
                newMove.g = 1 + startGame.g
                newMove.f = newMove.g + newMove.h
                # print('h(n)', newMove.h)
                # print('f(n)', newMove.f)
                q.put(PrioritizedItem(newMove.f, newMove))

        except:
            pass


        currentTime = time.time()
        # print(currentTime - startTime)

        if (currentTime - startTime) > maxTimeout:
            print('Code has timed out in ', maxTimeout, ' secs')
            quit()


def manhattan_distance_algorithm(game):
    
    startTime = time.time()

    #Uses PrioritzedItem class to order matrices from lowest heuristic (high priority) to hishest
    q = PriorityQueue()
    q.put(PrioritizedItem(game.manhattan_dist_heuristic(), game)) 
    game.h = game.manhattan_dist_heuristic()
    game.f = 0 + game.h

    max_queue = 1
    nodeExpand = 1

    while not q.empty():

        queue_size = max(max_queue, q.qsize())

        # Pops first node and stores it in startGame var.
        startGame = q.get().item  
        print('depth:', startGame.g)

        nodeExpand += 1
        

        # Prints gameState in matrix format
        print('Current State:')
        for i in startGame.gameState:
            for j in i:
                print(j, end=' ')
            print(' ')

        print('h(n)', startGame.h)
        print('f(n)', startGame.f)
    

        # Checks if curr_state = goal_state
        if startGame.goal_test(): 
            print('Solved using Manhattan Distance!!')

            print('Final Solution:')
            for i in startGame.gameState:
                for j in i:
                    print(j, end=' ')
                print(' ')

            print('Reached solution at a depth of ', startGame.g)
            endTime = time.time()
            print('Completion Time:', round(endTime - startTime, 3))
            print('# of nodes expanded:', nodeExpand)
            print('Max Queue Size:', queue_size)

            return

        # Checks all possible direction moves
        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Up)
            if newMove:
                newMove = Puzzle(newMove)
                #print('up', newMove.startState)
                newMove.h = newMove.manhattan_dist_heuristic()
                newMove.g = 1 + startGame.g
                newMove.f = newMove.g + newMove.h
                # print('h(n)', newMove.h)
                # print('f(n)', newMove.f)
                q.put(PrioritizedItem(newMove.f, newMove))

        except:
            pass

        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Down)
            if newMove:
                newMove = Puzzle(newMove)
                #print('down', newMove.startState)
                newMove.h = newMove.manhattan_dist_heuristic()
                newMove.g = 1 + startGame.g
                newMove.f = newMove.g + newMove.h
                # print('h(n)', newMove.h)
                # print('f(n)', newMove.f)
                q.put(PrioritizedItem(newMove.f, newMove))

        except:
            pass

        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Left)
            if newMove:
                newMove = Puzzle(newMove)
                #print('left', newMove.startState)
                newMove.h = newMove.manhattan_dist_heuristic()
                newMove.g = 1 + startGame.g
                newMove.f = newMove.g + newMove.h
                # print('h(n)', newMove.h)
                # print('f(n)', newMove.f)
                q.put(PrioritizedItem(newMove.f, newMove))

        except:
            pass

        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Right)
            if newMove:
                newMove = Puzzle(newMove)
                #print('right', newMove.startState)
                newMove.h = newMove.manhattan_dist_heuristic()
                newMove.g = 1 + startGame.g
                newMove.f = newMove.g + newMove.h
                # print('h(n)', newMove.h)
                # print('f(n)', newMove.f)
                q.put(PrioritizedItem(newMove.f, newMove))

        except:
            pass


        currentTime = time.time()
        # print(currentTime - startTime)

        if (currentTime - startTime) > maxTimeout:
            print('Code has timed out in ', maxTimeout, ' secs')
            quit()


if __name__== '__main__':


    matrix = []

    print('\nWelcome to my 8-puzzle solver! Enter a solvable 8-Puzzle.\n')
    print('Enter numbers for each row, separating each number using a space. Press ENTER when done\n')

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




    algChoice = int(input('Choose: \n(1) Uniform Cost \n(2) Misplaced Tiles \n(3) Manhattan Distance\n'))

    game = Puzzle(matrix)


    if algChoice == 1:
        uniform_cost_algorithm(game)

    if algChoice == 2:
        misplaced_tile_algorithm(game)

    if algChoice == 3:
        manhattan_distance_algorithm(game)
