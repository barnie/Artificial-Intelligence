__author__ = 'piotr'

import polynomial
import math
import generator


from Pair import Pair
class chromosom:

    def __init__(self,a,b,c,d,e):
        self.a = a;
        self.b = b;
        self.c = c;
        self.d = d;
        self.e = e;
        self.fit = 1000000.0; #dopasowanie

    def getList(self):
        return [self.a, self.b, self.c, self.d, self.e];

    def setList(self, lista):
        self.a = lista[0]
        self.b = lista[1]
        self.c = lista[2]
        self.d = lista[3]
        self.e = lista[4]

    def updateFit(self,i):
        wynik =  ( i.getX() * ( i.getX() * ( i.getX() * ( i.getX() * (self.a + 0) + self.b) + self.c ) + self.d) + self.e )
        self.fit = abs(wynik - i.getY());

    def getFit(self):
        return self.fit;

    def setFit(self,fit):
        self.fit = fit;

