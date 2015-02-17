__author__ = 'piotr'

import random
from chromosom import *
from polynomial import polynomial
from Pair import Pair

def randomFloatFromRange(x, y):
    tmp = random.uniform(x, y)
    return round(tmp,2)

def generateChromosome(x,y):
    return chromosom(randomFloatFromRange(x,y), randomFloatFromRange(x,y), randomFloatFromRange(x,y), randomFloatFromRange(x,y), randomFloatFromRange(x,y))

def generateChromosomePopulation(ILE, X, Y):
    lista = []
    for i in range(ILE):
        lista.append(generateChromosome(X,Y))
    return lista

def generateNumbers(ile, x, y):
    lista = []
    for i in range (ile):
        wartosc = randomFloatFromRange(x,y)
        wynik = polynomial(wartosc)
        lista.append(Pair(wartosc,wynik))
    return lista;

