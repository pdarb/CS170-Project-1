import time
from eightPuzzle import Puzzle, MoveDirection
from queue import Queue, PriorityQueue
from dataclasses import dataclass, field
from typing import Any


maxTimeout = 10

## From StackOverflow 
@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)


def uniform_cost_algorithm(game):

    startTime = time.time()

    q = Queue()
    q.put(game)

    while not q.empty():
        
        startGame = q.get()
        print('depth:', startGame.g)

        print('Current State:')
        for i in startGame.gameState:
            for j in i:
                print(j, end=' ')
            print(' ')
    

        if startGame.goal_test():
            print('Solved using Uniform Cost!')
            print('Final Solution:', startGame.gameState)

            endTime = time.time()
            print('Completion Time:', endTime - startTime)

            return 


        #checks all possible direction moves
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

    q = PriorityQueue()
    q.put(PrioritizedItem(game.misplaced_tile_heuristic(), game))

    while not q.empty():


        startGame = q.get().item  #pops first node and stores it in startGame var.
        print('depth:', startGame.g)

        print('Current State:')
        for i in startGame.gameState:
            for j in i:
                print(j, end=' ')
            print(' ')
    

        if startGame.goal_test(): #checks if curr_state = goal_state
            print('Solved using Misplaced Tile!!')
            return

        #checks all possible direction moves
        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Up)
            if newMove:
                newMove = Puzzle(newMove)
                #sprint('up', newMove.startState)
                newMove.h = newMove.misplaced_tile_heuristic()
                newMove.g = 1 + startGame.g
                newMove.f = newMove.g + newMove.h
                # print('h', newMove.h)
                # print('f', newMove.f)
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
                # print('h', newMove.h)
                # print('f', newMove.f)
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
                # print('h', newMove.h)
                # print('f', newMove.f)
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
                # print('h', newMove.h)
                # print('f', newMove.f)
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

    q = PriorityQueue()
    q.put(PrioritizedItem(game.manhattan_dist_heuristic(), game))

    while not q.empty():


        startGame = q.get().item  #pops first node and stores it in startGame var.
        print('depth:', startGame.g)
        
        print('Current State:')
        for i in startGame.gameState:
            for j in i:
                print(j, end=' ')
            print(' ')
    

        if startGame.goal_test(): #checks if curr_state = goal_state
            print('Solved using Manhattan Distance!!')
            return

        #checks all possible direction moves
        try:
            newMove = startGame.direction_result(startGame.startState, MoveDirection.Up)
            if newMove:
                newMove = Puzzle(newMove)
                #print('up', newMove.startState)
                newMove.h = newMove.manhattan_dist_heuristic()
                newMove.g = 1 + startGame.g
                newMove.f = newMove.g + newMove.h
                # print('h', newMove.h)
                # print('f', newMove.f)
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
                # print('h', newMove.h)
                # print('f', newMove.f)
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
                # print('h', newMove.h)
                # print('f', newMove.f)
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
                # print('h', newMove.h)
                # print('f', newMove.f)
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
