__author__ = 'piotr'

import random

class Neuron:
    def __init__(self, length, activation_function):
        self.input = []
        self.length = length
        self.weights = [random.random() for i in range(length + 1)]
        self.output = 0;
        self.activation_function = activation_function

    def getInput(self):
        return self.input

    def getWeights(self):
        return self.weights

    def getOutput(self):
        return self.output

    def getActivationFunction(self):
        return self.activation_function

    def setWeights(self, weights):
        self.weights = weights

    def setInput(self, input):
        self.input = input

    def getActivation(self):
        sum = 0.0
        for i in range(self.input):
            sum = sum + self.input[i] * self.weights[i]
        sum += self.weights[len(self.input)] #we have one more weight
        return self.activation_function(sum)
