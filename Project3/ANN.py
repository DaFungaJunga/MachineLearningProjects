import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm


# from PIL import Image


class DigitBitmap:
    def __init__(self):
        self.bitmap = np.empty([9, 5])

    def initialize(self,num):
        if num == 1:
            arr = np.array([[0, 0, 1, 0, 0],
                            [0, 1, 1, 0, 0],
                            [1, 0, 1, 0, 0],
                            [0, 0, 1, 0, 0],
                            [0, 0, 1, 0, 0],
                            [0, 0, 1, 0, 0],
                            [0, 0, 1, 0, 0],
                            [0, 0, 1, 0, 0],
                            [0, 0, 1, 0, 0]])
            self.bitmap = arr
        if num == 2:
            arr = np.array([[0, 1, 1, 1, 0],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [0, 0, 0, 0, 1],
                            [0, 0, 0, 1, 0],
                            [0, 0, 1, 0, 0],
                            [0, 1, 0, 0, 0],
                            [1, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1]])
            self.bitmap = arr
        if num == 3:
            arr = np.array([[0, 1, 1, 1, 0],
                            [1, 0, 0, 0, 1],
                            [0, 0, 0, 0, 1],
                            [0, 0, 0, 0, 1],
                            [0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 1],
                            [0, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [0, 1, 1, 1, 0]])
            self.bitmap = arr
        if num == 4:
            arr = np.array([[0, 0, 0, 1, 0],
                            [0, 0, 1, 1, 0],
                            [0, 0, 1, 1, 0],
                            [0, 1, 0, 1, 0],
                            [0, 1, 0, 1, 0],
                            [1, 0, 0, 1, 0],
                            [1, 1, 1, 1, 1],
                            [0, 0, 0, 1, 0],
                            [0, 0, 0, 1, 0]])
            self.bitmap = arr
        if num == 5:
            arr = np.array([[1, 1, 1, 1, 1],
                            [1, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0],
                            [1, 1, 1, 1, 0],
                            [1, 0, 0, 0, 1],
                            [0, 0, 0, 0, 1],
                            [0, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [0, 1, 1, 1, 0]])
            self.bitmap = arr
        if num == 6:
            arr = np.array([[0, 1, 1, 1, 0],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0],
                            [1, 1, 1, 1, 0],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [0, 1, 1, 1, 0]])
            self.bitmap = arr
        if num == 7:
            arr = np.array([[1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 1],
                            [0, 0, 0, 1, 0],
                            [0, 0, 0, 1, 0],
                            [0, 0, 1, 0, 0],
                            [0, 0, 1, 0, 0],
                            [0, 1, 0, 0, 0],
                            [0, 1, 0, 0, 0],
                            [0, 1, 0, 0, 0]])
            self.bitmap = arr
        if num == 8:
            arr = np.array([[0, 1, 1, 1, 0],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [0, 1, 1, 1, 0],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [0, 1, 1, 1, 0]])
            self.bitmap = arr
        if num == 9:
            arr = np.array([[0, 1, 1, 1, 0],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [0, 1, 1, 1, 1],
                            [0, 0, 0, 0, 1],
                            [0, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [0, 1, 1, 1, 0]])
            self.bitmap = arr
        if num == 0:
            arr = np.array([[0, 1, 1, 1, 0],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 0],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [0, 1, 1, 1, 0]])
            self.bitmap = arr


class Perceptron:
    def __init__(self):
        self.weight = np.empty([9, 5])

    def initializeWeights(self):
        for i in range(9):
            for j in range(5):
                #self.weight[i][j] = random.uniform(-2.4/(9*5), 2.4/(9*5))
                self.weight[i][j] = random.uniform(-0.5, 0.5)

    def updateWeight(self, i, j, inp, error, learningRate):
        self.weight[i][j] += learningRate * inp * error


class ANN:

    def __init__(self, epochs):
        self.output = np.empty(10)
        self.workingOutput = np.empty(10)
        self.desiredOutput = np.empty(10)
        self.epochs = epochs
        self.sumSquareError = np.empty(epochs)
        self.threshold = 0.2
        self.learningRate = 0.1
        self.perceptronNum = 10
        self.hiddenPerceptrons = [Perceptron() for i in range(10)]
        self.workingBitmap = DigitBitmap()

    def initialization(self):
        for p in range(self.perceptronNum):
            self.hiddenPerceptrons[p].initializeWeights()

    def currentDesiredOutput(self, num):
        self.workingBitmap.initialize(num)

        if num == 0:
            self.desiredOutput = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if num == 1:
            self.desiredOutput = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        if num == 2:
            self.desiredOutput = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        if num == 3:
            self.desiredOutput = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        if num == 4:
            self.desiredOutput = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        if num == 5:
            self.desiredOutput = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        if num == 6:
            self.desiredOutput = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        if num == 7:
            self.desiredOutput = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        if num == 8:
            self.desiredOutput = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        if num == 9:
            self.desiredOutput = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

    def run(self):
        for o in range(10):
            count = 0
            self.currentDesiredOutput(o)

            while count < self.epochs:

                for p in range(self.perceptronNum):
                    self.output[p] = 0
                    self.workingOutput[p] = 0
                    for i in range(9):
                        for j in range(5):
                            self.workingOutput[p] += self.workingBitmap.bitmap[i][j] * self.hiddenPerceptrons[p].weight[i][j]

                    # adjust threshold value when testing for better results
                    #print(str(self.output[p]))
                    self.workingOutput[p] -= self.threshold
                    #print(str(self.workingOutput[p]))
                    if self.workingOutput[p] >= 0:
                        self.output[p] = 1
                    else:
                        self.output[p] = 0

                mean = 0

                for p in range(self.perceptronNum):
                    mean += self.desiredOutput[p] - self.output[p]
                    for i in range(9):
                        for j in range(5):
                            self.hiddenPerceptrons[p].updateWeight(i, j, self.workingBitmap.bitmap[i][j],
                                                                   (self.desiredOutput[p] - self.output[p]),
                                                                   self.learningRate)

                mean = mean / self.perceptronNum

                for p in range(self.perceptronNum):
                    self.sumSquareError[count] += ((self.desiredOutput[p] - self.output[p]) - mean) ** 2
                print(
                    "Epoch: " + str(count) + " Desired Output: " + str(self.desiredOutput) + " Current Output: " + str(
                        self.output) + "Sum Squared Error: " + str(self.sumSquareError[count]))
                if self.sumSquareError[count] == 0:
                    print("Solution Found, moving to next number")
                    break
                count += 1


# epochs,number,perceptrons
ann = ANN(1000)
ann.initialization()
ann.run()
