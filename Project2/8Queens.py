import numpy as np
from random import randint

population = 10
boards = np.zeros((8, 8, population))
fitnessCounts = np.empty(population)

def initialize():
    for i in range(population):
        for j in range(8):
            r =randint(0,7)
            boards[i,j,r] = 1

def checkRows(x,y,board):
    errorCount=0
    for i in range(8):
        if x ==i:
            continue
        if board[i,y]==1:
            errorCount +=1
    return errorCount

def checkColumns(x,y,board):
    errorCount=0
    for i in range(8):
        if y ==i:
            continue
        if board[x,i]==1:
            errorCount +=1
    return errorCount

def checkDiagonal(x,y,board):
    errorCount=0
    for i in range(7):
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
def check(x,y, board):
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
        if x !=i:
            if board[i,y]==1:
                errorCount +=1
    return errorCount

def fitness():
    for k in range(population):
        errorCount = 0
        for i in range(8): #x
            for j in range(8): #y
                if boards[i,j,k]==1:
                    errorCount+=check(i,j,boards[:,:,k])
                else:
                    continue
        fitnessCounts[k]=errorCount


def crossover():

def mutation():


def run():
    initialize()
    while(check()):
        fit
