import numpy as np
from random import randint
import random
import matplotlib.pyplot as plt

class Queens:

    def __init__(self, population):
        self.population = population
        self.boards = np.zeros((8, 8, self.population))
        self.fitnessCounts = np.empty(self.population)
        self.mutationCO = 0.01
        self.crossoverCO = 0.7

    def initialize(self):
        for p in range(self.population):
            for j in range(8):
                r = randint(0, 7)
                self.boards[p, j, r] = 1

    def checkRows(self, x, y, board):
        errorCount = 0
        for i in range(8):
            if x == i:
                continue
            if board[i, y] == 1:
                errorCount += 1
        return errorCount

    def checkColumns(self,x,y,board):
        errorCount = 0
        for i in range(8):
            if y == i:
                continue
            if board[x, i] == 1:
                errorCount += 1
        return errorCount

    def checkDiagonal(self, x, y, board):
        errorCount=0
        for i in range(8):
            if i==0:
                continue
            currentx = x + i
            currentyminus = y - i
            currentyplus = y + i
            if currentx<7 and currentyplus<7:
                if board[currentx,currentyplus]==1:
                    errorCount += 1
            if currentx<8 and currentyminus>-1:
                if board[currentx,currentyminus]==1:
                    errorCount +=1
        return errorCount
    def check(self,x,y, board):
        errorCount=0
        for i in range(8):
            #Check Diagonals
            if i != 0:
                currentx = x + i
                currentyminus = y - i
                currentyplus = y + i
                if currentx < 7 and currentyplus < 7:
                    if board[currentx, currentyplus] == 1:
                        errorCount += 1
                if currentx < 8 and currentyminus > -1:
                    if board[currentx, currentyminus] == 1:
                        errorCount += 1
            #Check Columns
            if y != i:
                if board[x, i] == 1:
                    errorCount += 1
            #Check Rows
            if x != i:
                if board[i, y] == 1:
                    errorCount += 1
        return errorCount

    def fitness(self):
        for p in range(self.population):
            errorCount = 0
            for i in range(8): #x
                for j in range(8): #y
                    if self.boards[p, i, j] == 1:
                        errorCount += self.check(i, j, self.boards[p, :, :])
                    else:
                        continue
            self.fitnessCounts[p] = errorCount



    def uniformCrossover(self):
        for p in range(self.population):
            max1 = np.argmax(self.fitnessCounts)
            max2 = np.argmin(self.fitnessCounts)


            for i in range(8):
                if random.uniform(0, 1) < self.crossoverCO:
                    for j in range(8):
                        temp = self.boards[max1, i, j]
                        self.boards[max1, i, j] = self.boards[max2, i, j]
                        self.boards[max2, i, j] = temp

    def mutation(self):
        for p in range(self.population):
            for i in range(8):
                if random.uniform(0, 1) < self.mutationCO:
                    r = randint(0, 7)
                    for j in range(8):
                        if j == r:
                            self.boards[p, i, j] = 1
                        else:
                            self.boards[p, i, j] = 0
                else:
                    continue

    def checkFitness(self):
        currentMinIndex = np.argmin(self.fitnessCounts)
        if self.fitnessCounts[currentMinIndex] == 0:
            print(self.boards[currentMinIndex, :, :])
            return False
        return True


    def run(self):
        Averagedata = []
        Fittest = []

        gen = 0
        self.initialize()
        self.fitness()
        while self.checkFitness():
            gen += 1
            self.uniformCrossover()
            self.mutation()
            self.fitness()
            if gen % 1000 == 0:
                print(gen)
                print(self.fitnessCounts)

                # Average
                Averagedata.append(sum(self.fitnessCounts) / len(self.fitnessCounts))
                Fittest.append(np.argmin(self.fitnessCounts))

        print(self.fitnessCounts)
        print('Final Generation: ' + str(gen))
        return Fittest, Averagedata

thing = Queens(8)
data = thing.run()

# used for average graph
plt.plot(data[0], label='Best')
plt.plot(data[1], label='Average')

plt.ylabel('Error Counts')
plt.xlabel('Generations (Thousands)')
plt.title('Error Count vs. Generation')
plt.show()
