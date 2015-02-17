import os
import sys
import math
import random
import numpy as np
import matplotlib.pyplot as plt



x = [[0,0,0],[1,0,1],[0,1,1],[1,1,0]]
h = 0.333333


def funkcja(s):
	return 1 / ( 1 + math.pow(math.e,-s))

def pochodna(s):
	licznik = math.pow(math.e,-s);
	mianownik = math.pow(licznik+1,2)
	return licznik / mianownik


w = [random.random() + 1 for i in range(9)]
blad = 0.01

if __name__ == '__main__':
	print "Siec neuronowa"
	print w
	bledy = [9,9,9,9]
	i = 0
	lista_bledow = []
	while i < 100000 :
		_blad = 0.0;
		for j in range (4):
			s1 = w[0] * x[j][0] + w[1]*x[j][1] + w[2] # 1 neuron
			s2 = w[3] * x[j][0] + w[4]*x[j][1] + w[5] # 2 neuron
			wynik1 = funkcja(s1); # funkcja aktywujaca dla pierwszego
			wynik2 = funkcja(s2); # funkcja aktywujace dla drugiego
			s3 = wynik1 * w[6] + wynik2 * w[7] + w[8] # 3 neuron
			wynik3 = funkcja(s3)
			delta3 = -x[j][2] + wynik3 # BLAD WYJSCIA to co ma wyjsc - to co wyszlo
			_blad += delta3
			#print "blad", delta3, "wyszlo", wynik3
			w[0] = w[0] - (h * delta3) * w[6] * pochodna(s1) * x[j][0]
			w[1] = w[1] - (h * delta3) * w[6] * pochodna(s1) * x[j][1]
			w[2] = w[2] - (h * delta3) * w[6] * pochodna(s1) # 1 neuron

			w[3] = w[3] - (h * delta3) * w[7] * pochodna(s2) * x[j][0]
			w[4] = w[4] - (h * delta3) * w[7] * pochodna(s2) * x[j][1]
			w[5] = w[5] - (h * delta3) * w[7] * pochodna(s2) # 2 neuron

			w[6] = w[6] - (h * delta3) * wynik1
			w[7] = w[7] - (h * delta3) * wynik2
			w[8] = w[8] - (h * delta3) #ostatni neuron
			print "x: ",x[j][0], " y: ", x[j][1], " = ",wynik3, " ?=? ", x[j][2]
			bledy[j] = abs(x[j][2] - wynik3)
		lista_bledow.append(_blad/4)
		c = 0;
		for k in range(4):
			if bledy[k] > blad:
				c = 1
		if c == 0:
			break
		i+=1
	print "epoki", i, "\nwagi:", w
	bins = np.linspace(-1, 1, i)
	plt.hist(lista_bledow, bins, alpha=0.5)
	plt.show()

