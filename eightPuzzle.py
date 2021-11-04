from copy import deepcopy
import math

class Puzzle:
    def __init__ (self, start, next = None):
        self.startState = start
        self.gameState = start

        self.goalState = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
        self.g = 0
        self.h = 0
        self.f = 0

    def manhattan_dist_heuristic(matrix):
        dist = 0
        for i in range(len(random)):
            for j in range(len(random[i])):
                if random[i][j] != goal[i][j] and random[i][j] != 0:
                    goalPos = thisdict[str(random[i][j])]
                    #print(goalPos)
                    dist += (abs(i - goalPos[0]) + abs(j - goalPos[1]))
        print(dist)

    def misplaced_tile_heuristic(self, start, goal):
        count = 0
        for i in range(len(random)):
            for j in range(len(random[i])):
                if random[i][j] != goal[i][j]:
                    count += 1
        print(count)
        

    #def 
    # def manhattan_algorithm(self, )

    # def print_initial_state(self):


    def solution_check(self):
        return self.gameState == self.goalState



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

#algChoice = input('Choose (1)Uniform Cost ')


print('Matrix: ', matrix)
