__author__ = 'piotr'
from Neuron import Neuron
from data import electric_handler
import math


class Network:
    # Wejscie: a) p(-2), p(-1) - energia z ostatnich dwoch godzin tego dnia,
    # b) p(-26), p(-25) - analogicznie ale z dnia poprzedniego,
    # c) dzien tygodnia opisany jako punkt na okregu,
    # d) dzien roku analogicznie jak dzien tygodnia,
    # e) dane meteorologiczne dla 9 miast (punktow): temperatura, cisnienie,
    # wilgotnosc powietrza, opady.

    def __init__(self):
        self.layouts = []
        neurons = []
        for i in range(1000):
            neurons.append(Neuron(6, self.f_unipolarna))
        self.layouts.append(neurons)
        self.beta = -1
        neurons = []
        for i in range(24):
            neurons.append(Neuron(6, self.f_unipolarna))

    def f_unipolarna(self, x):
        return 1.0 / (1 + (math.pow(math.e, self.beta * x)))

    def f_unipolarna_prim(self, x):
        return self.beta * self.f_unipolarna(x) * (1 - self.f_unipolarna(x))

    def f_bipolarna(self, x):
        return (1 - (math.pow(math.e, self.beta * x))) / (1 + (math.pow(math.e, -self.beta * x)))

    def f_bipolarna_prim(self, x):
        return self.beta * (1 - math.pow(self.f_bipolarna(x), 2))

    def learn(self):
        for i in range(1000):
            pass