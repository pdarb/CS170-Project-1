from copy import deepcopy
from queue import Queue
from enum import Enum
import numpy as np
import math

class MoveDirection(Enum):
    Up = (-1, 0)
    Down = (1, 0)
    Right = (0, 1)
    Left = (0, -1)


class Puzzle:
    def __init__ (self, start):
        self.startState = start
        self.gameState = start

        self.goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.g = 0
        #self.h = 0
        self.f = 0
        self.zero_index = []


    # Calculate the # of misplaced tiles of current state 
    def misplaced_tile_heuristic(self): 
        count = 0
        for i in range(len(self.gameState)):
            for j in range(len(self.gameState[i])):
                if self.startState[i][j] != self.goalState[i][j] and self.gameState[i][j] != 0:
                    count += 1
        print(count)
        return count
    

    # Calculate manhattan distance of current state
    def manhattan_dist_heuristic(self): 
        thisdict = {
            "1": [0,0],
            "2": [0,1],
            "3": [0,2],
            "4": [1,0],
            "5": [1,1],
            "6": [1,2],
            "7": [2,0],
            "8": [2,1],
            "0": [2,2]
        }
        
        dist = 0
        for i in range(len(self.gameState)):
            for j in range(len(self.gameState[i])):
                if self.gameState[i][j] != self.goalState[i][j] and self.gameState[i][j] != 0:
                    goalPos = thisdict[str(self.gameState[i][j])]
                    print(goalPos)
                    dist += (abs(i - goalPos[0]) + abs(j - goalPos[1]))
        print(dist)
        return dist


    def find_zero_index(self):
        for i in range(len(self.gameState)):
            for j in range(len(self.gameState[i])):
                if self.gameState[i][j] == 0:
                    self.zero_index = [i, j]
                    print(self.zero_index)
        return self.zero_index
        


    def direction_result(self, state, move):
        
        state = self.copy_matrix(state)

        # Add conditions to check edge cases, check for valid moves
        
        self.find_zero_index() # Finds position of 0 before moving
        #if (self.zero_index[0] < 0)

        swapPos = [sum(x) for x in zip(self.zero_index, move.value)]

        if swapPos[0] >= 0 and swapPos[0] <= 2 and swapPos[1] >=0 and swapPos[1] <=2:
            temp = state[swapPos[0]][swapPos[1]]
            state[self.zero_index[0]][self.zero_index[1]] = temp
            state[swapPos[0]][swapPos[1]] = 0
            return state
        else:
            return ''


        # a = self.gameState[self.zero_index[0]][self.zero_index[1]]
        # b = self.gameState[val[0]][val[1]]

        #a, b = b, a
        # self.gameState[self.zero_index[0]][self.zero_index[1]], self.gameState[val[0]][val[1]] = self.gameState[val[0]][val[1]], self.gameState[self.zero_index[0]][self.zero_index[1]]
        # return self.gameState


    def copy_matrix(self): #makes a copy of current matrix
        return deepcopy(self.gameState)
        

    def print_initial_state(self):
        print('Matrix: ', self.gameState)


    def goal_test(self):
        #print('Reached goal test')
        isEqual = np.array_equal(self.gameState, self.goalState) 
        #print('Is equal:', isEqual)
        return isEqual

        


