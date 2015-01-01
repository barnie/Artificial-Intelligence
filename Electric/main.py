__author__ = 'piotr'

from data import electric_handler as el
from ffnet import tmlgraph, ffnet
import copy
from data import weather_city


# Wejscie: a) p(-2), p(-1) - energia z ostatnich dwoch godzin tego dnia,
# b) p(-26), p(-25) - analogicznie ale z dnia poprzedniego,
# c) dzien tygodnia opisany jako punkt na okregu,
# d) dzien roku analogicznie jak dzien tygodnia,
# e) dane meteorologiczne dla 9 miast (punktow): temperatura, cisnienie,
# wilgotnosc powietrza, opady.
global ELECTRIC
ELECTRIC = el.electric_hander()

BIALYSTOK = weather_city.weather_cit('bialystok')
GORZOW = weather_city.weather_cit('gorzow')
KATOWICE = weather_city.weather_cit('katowice')
KIELCE = weather_city.weather_cit('kielce')
KRAKOW = weather_city.weather_cit('krakow')
LUBLIN = weather_city.weather_cit('lublin')
OLSZTYN = weather_city.weather_cit('olsztyn')

LEARNING_COMMITTEE = []
TESTING_COMMITTEE = []

NETWORKS = []

METEO = [BIALYSTOK.getWeather(), GORZOW.getWeather(), KATOWICE.getWeather(),
 KIELCE.getWeather(), KRAKOW.getWeather(), LUBLIN.getWeather(), OLSZTYN.getWeather()]


def prepare_input():
    """ Prepare input to neuronal network """
    dane = copy.copy(ELECTRIC.getElectricDays())
    for i in range(len(dane)):
        dane[i].getHourList().append(dane[i].getDate().timetuple().tm_yday)
        for j in METEO:
            if i < 1460:
                dane[i].getHourList().append(j[i][3])
                dane[i].getHourList().append(j[i][4])
                dane[i].getHourList().append(j[i][5])
                dane[i].getHourList().append(j[i][6])
    input1 = []
    for i in dane:
        input1.append(i.getHourList())
    return input1[:-1]


def prepare_target():
    """Prepare target to compare if output from network is good"""
    target = []
    dane = el.electric_hander().getElectricDays()
    i = 0
    while i < len(dane):
        if i != 0:
            target.append(dane[i].getHourList())
        i += 1
    return target


TARGET = prepare_target()
INPUT = prepare_input()


def prepare_data():
    """Preparing data for specific neuronal networks problem"""
    pass

def calculate_network(input_, target_, test_input, test_output, net1):
    """" Return learned network and, outpur,regression for test """
    network = net1.train_rprop(input_, target_, mimin=1e-06, mimax=500.0,
        xmi=0.2, maxiter=1, disp=1)
    output, regression = net1.test(test_input, test_output, iprint=2)
    return network, output, regression

#
CONEC = tmlgraph((53, 45, 45, 24))  # tmlgraph or imlgraph? which one will be better ?
NET = ffnet(CONEC)
print len(INPUT), len(TARGET)
# NX.draw_graphviz(net.graph, prog='dot') show the network that's nice!
# pl.show()

calculate_network(INPUT[:-365], TARGET[:-365], INPUT[-365:], TARGET[-365:], NET)

# sum = 0.0
# for i in range(len(output)):
#     for j in range((len(output[i]))):
#         sum = sum + ((abs(float(target[i][j]) - float(output[i][j]))) / float(output[i][j]))
# print sum / 365

# print len(bialystok.getWeather()), len(prepareInput())
