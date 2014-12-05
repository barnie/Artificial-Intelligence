__author__ = 'piotr'

from data import electric_handler as el
from Neuron import Network
import neurolab as nl
from ffnet import *
import networkx as NX
import pylab as pl
import math
import copy
from numpy import linspace
from data import weather_city
from theano import *

# Wejscie: a) p(-2), p(-1) - energia z ostatnich dwoch godzin tego dnia,
# b) p(-26), p(-25) - analogicznie ale z dnia poprzedniego,
# c) dzien tygodnia opisany jako punkt na okregu,
# d) dzien roku analogicznie jak dzien tygodnia,
# e) dane meteorologiczne dla 9 miast (punktow): temperatura, cisnienie,
# wilgotnosc powietrza, opady.
global e
e = el.electric_hander()

bialystok = weather_city.weather_cit('bialystok')
gorzow = weather_city.weather_cit('gorzow')
katowice = weather_city.weather_cit('katowice')
kielce = weather_city.weather_cit('kielce')
krakow = weather_city.weather_cit('krakow')
lublin = weather_city.weather_cit('lublin')
olsztyn = weather_city.weather_cit('olsztyn')

meteo = [bialystok.getWeather(), gorzow.getWeather(), katowice.getWeather(), kielce.getWeather(),
         krakow.getWeather(), lublin.getWeather(), olsztyn.getWeather()]

# at now only for one hour

def prepareInput():
    dane = copy.copy(e.getElectricDays())
    for i in range(len(dane)):
        dane[i].getHourList().append(dane[i].getDate().timetuple().tm_yday)
        for j in meteo:
            if i < 1460:
                dane[i].getHourList().append(j[i][3])
                dane[i].getHourList().append(j[i][4])
                dane[i].getHourList().append(j[i][5])
                dane[i].getHourList().append(j[i][6])
    input = []
    for i in dane:
        input.append(i.getHourList())
    return input[:-1]


def prepareTarget():
    target = []
    dane = el.electric_hander().getElectricDays()
    i = 0
    while i < len(dane):
        if i != 0:
            target.append(dane[i].getHourList())
        i += 1
    return target


target = prepareTarget()
input = prepareInput()
#
conec = tmlgraph((53, 45, 45, 24))  # tmlgraph or imlgraph? which one will be better ?
net = ffnet(conec)
print len(input), len(target)
# NX.draw_graphviz(net.graph, prog='dot') show the network that's nice!
# pl.show()
dd = net.train_rprop(input[:-365], target[:-365], mimin=1e-06, mimax=500.0, xmi=0.2, maxiter=10000, disp=1)
output, regression = net.test(input[-365:], target[-365:], iprint=2)

sum = 0.0

for i in range(len(output)):
    for j in range((len(output[i]))):
        sum = sum + ((abs(float(target[i][j]) - float(output[i][j]))) / float(output[i][j]))
print sum / 365

print len(bialystok.getWeather()), len(prepareInput())
