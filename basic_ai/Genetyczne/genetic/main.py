__author__ = 'piotr'
import Pair
from generator import generateChromosomePopulation, generateNumbers
import polynomial
from chromosom import chromosom
from ByteConverter import *
import math
import struct
from genetic import Genetic
LENPOLUATION = 300
LENDANE = 2000
X = float(-3.5)
Y = float(3.5)


global weryfikujacy;
weryfikujacy = []
global population
population = []




def main():
    print "Witaj Swiecie!"
    weryfikujacy = generateNumbers(LENDANE, X, Y) #ile, przedzial-przedzial
    print "Stworzono ciag weryfikacyjny"
    print "Wyrzucenie danych"
    Genetic(weryfikujacy, LENPOLUATION, X, Y).run()
    #print "####"
    #print toByte(-15.5)
    #print toDecimal(toByte(-15.5))


if __name__ == "__main__":
    main();