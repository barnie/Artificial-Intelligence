__author__ = 'piotr'
import Pair
from generator import generateChromosomePopulation, generateNumbers
import polynomial
from chromosom import chromosom
from ByteConverter import *
import math
import struct

LENPOLUATION = 100
ITERATION = 400
LENDANE = 600
X = float(-1.5)
Y = float(1.0)


global weryfikujacy;
weryfikujacy = []
global population
population = []



def main():
    print "Witaj Swiecie!"
    weryfikujacy = generateNumbers(LENDANE, X, Y) #ile, przedzial-przedzial
    population = generateChromosomePopulation(LENPOLUATION, X, Y)
    #Generacja Danych i populacja
    # for i in weryfikujacy:
    #     print i.toStr()
    # for i in population:
    #     print i.getList()
    print "Wyrzucenie danych"
    c = chromosom (1.0,2.0,3.0,4.0,5.0)
    c.updateFit(weryfikujacy[0])
    print "####"
    print toByte(-15.5)
    #print toDecimal(toByte(-15.5))


if __name__ == "__main__":
    main();