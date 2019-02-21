import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm


# from PIL import Image


class DigitBitmap:
    def __init__(self, num):
        self.num = num
        self.bitmap = np.empty([9, 5])

    def initialize(self):
        if self.num == 1:
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
        if self.num == 2:
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
        if self.num == 3:
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
        if self.num == 4:
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
        if self.num == 5:
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
        if self.num == 6:
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
        if self.num == 7:
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
        if self.num == 8:
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
        if self.num == 9:
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
        if self.num == 0:
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
                self.weight[i][j] = random.uniform(0, 1)

    def updateWeight(self, i, j, inp, error, learningRate):
        self.weight[i][j] += learningRate * inp * error


class ANN:

    def __init__(self, epochs, number, perceptrons):
        self.output = np.empty(10)
        self.desiredOutput = np.empty(10)
        self.epochs = epochs
        self.number = number
        self.threshold = 0.2
        self.learningRate = 0.2
        self.hiddenPerceptrons = [Perceptron() for i in range(perceptrons)]
        self.workingBitmap = DigitBitmap(self.number)

    def initialization(self):
        self.workingBitmap.initialize()

        if self.number == 0:
            self.desiredOutput = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if self.number == 1:
            self.desiredOutput = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        if self.number == 2:
            self.desiredOutput = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        if self.number == 3:
            self.desiredOutput = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        if self.number == 4:
            self.desiredOutput = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        if self.number == 5:
            self.desiredOutput = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        if self.number == 6:
            self.desiredOutput = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        if self.number == 7:
            self.desiredOutput = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        if self.number == 8:
            self.desiredOutput = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        if self.number == 9:
            self.desiredOutput = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

    def run(self):
        count = 0
        while count < self.epochs:
            for p in range(self.hiddenPerceptrons.__sizeof__()):
                self.output[p] = 0
                for i in range(9):
                    for j in range(5):
                        self.output += (self.workingBitmap.bitmap[i][j] * self.hiddenPerceptrons[i].weight[j])
                # adjust threshold value when testing for better results
                print(self.output[p])
                self.output[p] -= self.threshold
                if self.output[p] >= 0:
                    self.output[p] = 1
                else:
                    self.output[p] = 0
            for p in range(self.hiddenPerceptrons.__sizeof__()):
                for i in range(9):
                    for j in range(5):
                        self.hiddenPerceptrons[p].updateWeight(i, j, self.workingBitmap.bitmap[i][j],
                                                         (self.desiredOutput[p] - self.output[p]), self.learningRate)
            print("Epoch: " + str(count) + " Desired Output: " + str(self.desiredOutput) + "Current Output: " + str(
                self.output))
            count += 1
