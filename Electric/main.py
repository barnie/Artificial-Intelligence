__author__ = 'piotr'

from data import electric_handler as el
from ffnet import tmlgraph, ffnet
import copy
from data import weather_city


global ELECTRIC
ELECTRIC = el.electric_hander()

BIALYSTOK = weather_city.weather_cit('bialystok')
GORZOW = weather_city.weather_cit('gorzow')
KATOWICE = weather_city.weather_cit('katowice')
KIELCE = weather_city.weather_cit('kielce')
KRAKOW = weather_city.weather_cit('krakow')
LUBLIN = weather_city.weather_cit('lublin')
OLSZTYN = weather_city.weather_cit('olsztyn')

LEARNING_SPECIALIST = [[],[],[],[],[]]
LEARNING_SPECIALIST_OUTPUT = [[],[],[],[],[]]
TESTING_SPECIALIST = []
TESTING_SPECIALIST_OUTPUT = []
NETWORKS = []

METEO = [BIALYSTOK.getWeather(), GORZOW.getWeather(), KATOWICE.getWeather(),
 KIELCE.getWeather(), KRAKOW.getWeather(), LUBLIN.getWeather(), OLSZTYN.getWeather()]


def prepare_input():
    """ Prepare input to neuronal network """
    #so lazy! do it in future without copying list -.-
    dane = copy.copy(ELECTRIC.getElectricDays())
    for i in range(len(dane)):
        dane[i].getHourList().append(dane[i].getDate().timetuple().tm_yday)
        weekday = dane[i].getDate().weekday() + 1
        dane[i].getHourList().append(weekday)
        for j in METEO:
            if i < 1460:
                dane[i].getHourList().append(j[i][3])
                dane[i].getHourList().append(j[i][4])
                dane[i].getHourList().append(j[i][5])
                dane[i].getHourList().append(j[i][6])
    input1 = []
    #splitting days
    for i in dane[:-1]:
        input1.append(i.getHourList())
        day = i.getHourList()[25]
        if day == 1: #monday
            LEARNING_SPECIALIST[0].append(i.getHourList())
        elif day == 5: #friday
            LEARNING_SPECIALIST[1].append(i.getHourList())
        elif day == 6: #saturday
            LEARNING_SPECIALIST[2].append(i.getHourList())
        elif day == 7: #sunday
            LEARNING_SPECIALIST[3].append(i.getHourList())
        else: #work days
            LEARNING_SPECIALIST[4].append(i.getHourList())
    return input1


def prepare_target():
    """Prepare target to compare if output from network is good"""
    target = []
    dane = el.electric_hander().getElectricDays()
    i = 0
    while i < (len(dane) - 1):
        target.append(dane[i].getHourList())
        weekday = dane[i].getDate().weekday() + 1
        if weekday == 1: #monday
            LEARNING_SPECIALIST_OUTPUT[0].append(dane[i].getHourList())
        elif weekday == 5: #friday
            LEARNING_SPECIALIST_OUTPUT[1].append(dane[i].getHourList())
        elif weekday == 6: #saturday
            LEARNING_SPECIALIST_OUTPUT[2].append(dane[i].getHourList())
        elif weekday == 7: #sunday
            LEARNING_SPECIALIST_OUTPUT[3].append(dane[i].getHourList())
        else: #work days
            LEARNING_SPECIALIST_OUTPUT[4].append(dane[i].getHourList())
        i += 1
    return target

TARGET = prepare_target()
INPUT = prepare_input()


def calculate_network(input_, target_, test_input, test_output, net1):
    """" Return learned network and, outpur,regression for test """
    network = net1.train_rprop(input_, target_, mimin=1e-06, mimax=500.0,
        xmi=0.2, maxiter=100, disp=1)
    #run our neuronal network
    output, regression = net1.test(test_input, test_output, iprint=2)
    #test network
    summ = 0.0
    for index in range(len(output)):
         for j in range((len(output[index]))):
             summ = summ + ( (abs(float(target_[index][j]) - float(output[index][j]))) / float(target_[index][j]) )
    print summ, summ/len(test_output) # print error for all networks
    return network, output, regression


CONEC = tmlgraph((54, 10, 24)) #model of connections
NET = ffnet(CONEC)


# NX.draw_graphviz(net.graph, prog='dot') show the network that's nice!
# pl.show()

#calculate special days
for i in range(4):
    net = ffnet(CONEC) #year have 52 weeks so, run networks for year
    network, output, regression = calculate_network(
        LEARNING_SPECIALIST[i][:-52],
        LEARNING_SPECIALIST_OUTPUT[i][:-52],
        LEARNING_SPECIALIST[i][-52:],
        LEARNING_SPECIALIST_OUTPUT[i][-52:], net)
#calculate work days
calculate_network(LEARNING_SPECIALIST[4][:-156],
 LEARNING_SPECIALIST_OUTPUT[4][:-156], LEARNING_SPECIALIST[4][-156:],
        LEARNING_SPECIALIST_OUTPUT[4][-156:], NET)

