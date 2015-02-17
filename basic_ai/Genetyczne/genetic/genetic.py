#!/usr/bin/env python
from generator import *
from chromosom import *
from Pair import *
from polynomial import *
import math
import random

class Genetic:

    def __init__(self, weryfikujacy, LENPOPULATION, X, Y):
        self.weryfikujacy = weryfikujacy
        self.ITERATION = 500
        self.LENPOPULATION = LENPOPULATION
        self.population = population = generateChromosomePopulation(self.LENPOPULATION, -16, 16)
        self.all_fit = 0
        self.pmutacja = 0.30

    def checkFit(self, x):
        self.all_fit = 0
        for i in self.population:
            final = polynomial(x)
            sol = getPolynomial(x, i.a, i.b, i.c, i.d, i.e)
            tmp = abs(final - sol)
            self.all_fit += tmp
            i.setFit(tmp)
        return self.all_fit / self.LENPOPULATION

    def getParents(self):
        ###### obliczanie randomu ruletki
        randomize = [randomFloatFromRange(0.0, 100.0) for j in range(self.LENPOPULATION)]
        randomize.sort() # posortowane
        ###### koniec obliczania randomu ruletki
        parents = []
        j = 0;
        suma = self.population[j].best
        for i in range(self.LENPOPULATION):
            while randomize[i] > suma and j < self.LENPOPULATION:
                suma += self.population[j].best
                j += 1
            parents.append(j)
        random.shuffle(parents, random.random)
        return parents

    def crossing(self, parents):
        new_population = []
        #nie ma wspolczynika krzyzowania na razie :)!
        i = 0
        j = 1
        while i < self.LENPOPULATION:
            a = self.population[parents[i]].getList()
            b = self.population[parents[j]].getList()
            a_list = [0.0, 0.0, 0.0, 0.0, 0.0]
            b_list = [0.0, 0.0, 0.0, 0.0, 0.0]
            
            for j in range(5):
                if (a[j] >= 0):
                    a_chron = list((bin(int(a[j] * 100))[2:]))
                else:
                    a_chron = list((bin(int(a[j] * 100))[3:]))
                if (b[j] >= 0):
                    b_chron = list((bin(int(b[j] * 100))[2:]))
                else:
                    b_chron = list((bin(int(b[j] * 100))[3:]))
                #mamy binarne
                length = len(a_chron) if len(a_chron) < len(b_chron) else len(b_chron)
                od_ktorego = random.randrange(length)
                for k in range(length):
                    tmp = a_chron[k]
                    a_chron[k] = b_chron[k]
                    b_chron[k] = tmp
                a_list[j] = float(int("".join(a_chron), 2)) / 100.0
                b_list[j] = float(int("".join(b_chron), 2)) / 100.0
            new_population.append(chromosom(a_list[0], a_list[1], a_list[2], a_list[3], a_list[4]))
            new_population.append(chromosom(b_list[0], b_list[1], b_list[2], b_list[3], b_list[4]))
            i += 2
            j += 2
        return new_population

    def mutacja(self, population):
        #TO DO: mutation end debugging
        j = 0;
        for i in population:
            propabilistic = random.random()
            if propabilistic < self.pmutacja:
                a = i.getList()
                a_list = [0.0, 0.0, 0.0, 0.0, 0.0]
                for j in range(5):
                    if (a[j] >= 0):
                        a_chron = list((bin(int(a[j] * 100))[2:]))
                    else:
                        a_chron = list((bin(int(a[j] * 100))[3:]))
                    ktory = random.randrange(len(a_chron))
                    if a_chron[ktory] == '0':
                        a_chron[ktory] = '1'
                    else:
                        a_chron[ktory] = '0'
                    a_list[j] = float(int("".join(a_chron), 2)) / 100.0
                    i = chromosom(a_list[0], a_list[1], a_list[2], a_list[3], a_list[4])
        return population

    def run(self):
        #TO DO: DOdac fory
        #print '\033[1;35mEPOKA:\033[1;m'
        for j in range(1000):
            for i in range(len(self.weryfikujacy)): # dla kazdego x    
                self.checkFit(self.weryfikujacy[i].getX()) # obliczony blad
                for i in self.population:
                    i.setFit((i.getFit() / self.all_fit) * 100) # obliczony fit
    
                self.population.sort(key=lambda x: x.getFit())
                _min = 0
                _max = len(self.population) - 1
                while (_min != _max and _min != self.LENPOPULATION / 2):
                    self.population[_min].best = self.population[_max].fit
                    self.population[_max].best = self.population[_min].fit
                    _min += 1
                    _max -= 1
                ##
                #print "\033[1;32mRULETKA Wartosci (Best w ruletce posortowanej):"
                #for i in self.population: print i.best, " ",
                #print "\nEND RULETKI\033[1;m"
                # posortowane wedlug fitu, ale kawalek ciasta na ruletce rozdajemy wedlug besta :)
                parents = self.getParents()
                #print "\033[1;33mRodzice ", len(parents)
                #for i in parents: print i," ",
                #print "\nRodzice\033[1;m"
                new_population = self.crossing(parents)
                #print "\033[1;34m##############################",len(new_population)
                #for i in new_population : print i.getList(), " ",
                #print "\n##############################\033[1;m"
            self.mutacja(self.population)
            #print '\033[1;35mKONIEC EPOKI\033[1;m'
            print self.population[0].getList()



