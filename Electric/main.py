__author__ = 'piotr'

from data import electric_handler as el
from ffnet import tmlgraph, ffnet
import copy
from data import weather_city
import numpy as np


global ELECTRIC
ELECTRIC = el.electric_hander()

BIALYSTOK = weather_city.weather_cit('bialystok')
GORZOW = weather_city.weather_cit('gorzow')
KATOWICE = weather_city.weather_cit('katowice')
KIELCE = weather_city.weather_cit('kielce')
KRAKOW = weather_city.weather_cit('krakow')
LUBLIN = weather_city.weather_cit('lublin')
OLSZTYN = weather_city.weather_cit('olsztyn')

LEARNING_SPECIALIST = [[], [], [], [], []]
LEARNING_SPECIALIST_OUTPUT = [[], [], [], [], []]
TESTING_SPECIALIST = []
TESTING_SPECIALIST_OUTPUT = []
NETWORKS = []

HOLIDAYS = [
    [{"day": 1, "month": 1, "year": 2010}, {"day": 1, "month": 1, "year": 2011}, {"day": 1, "month": 1, "year": 2012},
     {"day": 1, "month": 1, "year": 2013}],
    [{"day": 0, "month": 0, "year": 2010}, {"day": 6, "month": 1, "year": 2011}, {"day": 6, "month": 1, "year": 2012},
     {"day": 6, "month": 1, "year": 2013}],
    [{"day": 4, "month": 4, "year": 2010}, {"day": 24, "month": 4, "year": 2011}, {"day": 8, "month": 4, "year": 2012},
     {"day": 31, "month": 3, "year": 2013}],
    [{"day": 5, "month": 4, "year": 2010}, {"day": 25, "month": 4, "year": 2011}, {"day": 9, "month": 4, "year": 2012},
     {"day": 1, "month": 4, "year": 2013}],
    [{"day": 1, "month": 5, "year": 2010}, {"day": 1, "month": 5, "year": 2011}, {"day": 1, "month": 5, "year": 2012},
     {"day": 1, "month": 5, "year": 2013}],
    [{"day": 3, "month": 5, "year": 2010}, {"day": 3, "month": 5, "year": 2011}, {"day": 3, "month": 5, "year": 2012},
     {"day": 3, "month": 5, "year": 2013}],
    [{"day": 23, "month": 5, "year": 2010}, {"day": 12, "month": 6, "year": 2011},
     {"day": 27, "month": 5, "year": 2012}, {"day": 19, "month": 5, "year": 2013}],
    [{"day": 3, "month": 6, "year": 2010}, {"day": 23, "month": 6, "year": 2011}, {"day": 7, "month": 6, "year": 2012},
     {"day": 30, "month": 5, "year": 2013}],
    [{"day": 15, "month": 7, "year": 2010}, {"day": 15, "month": 7, "year": 2011},
     {"day": 15, "month": 7, "year": 2012}, {"day": 15, "month": 7, "year": 2013}],
    [{"day": 1, "month": 11, "year": 2010}, {"day": 1, "month": 11, "year": 2011},
     {"day": 1, "month": 11, "year": 2012}, {"day": 1, "month": 11, "year": 2013}],
    [{"day": 11, "month": 11, "year": 2010}, {"day": 11, "month": 11, "year": 2011},
     {"day": 11, "month": 11, "year": 2012}, {"day": 11, "month": 11, "year": 2013}],
    [{"day": 25, "month": 12, "year": 2010}, {"day": 25, "month": 12, "year": 2011},
     {"day": 25, "month": 12, "year": 2012}, {"day": 25, "month": 12, "year": 2013}],
    [{"day": 26, "month": 12, "year": 2010}, {"day": 26, "month": 12, "year": 2011},
     {"day": 26, "month": 12, "year": 2012}, {"day": 26, "month": 12, "year": 2013}]]

training_holidays = []
def if_holida(day, month, year):
    for i in HOLIDAYS:
        for j in i:
            if j['day'] == day and j['month'] == month and j['year'] == year:
                return True
    return False

METEO = [BIALYSTOK.getWeather(), GORZOW.getWeather(), KATOWICE.getWeather(),
         KIELCE.getWeather(), KRAKOW.getWeather(), LUBLIN.getWeather(), OLSZTYN.getWeather()]

def calculate_expert():
    pass

def prepare_input():
    """ Prepare input to neuronal network """
    # so lazy! do it in future without copying list -.-
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
    # splitting days
    for i in dane[:-1]:
        input1.append(i.getHourList())
        day = i.getHourList()[25]
        if if_holida( i.getDate().day, i.getDate().month, i.getDate().year):
            training_holidays.append([[{"day": i.getDate().day, "month": i.getDate().month, "year": i.getDate().year}], i.getHourList()])
        else :
            if day == 1:  #monday
                LEARNING_SPECIALIST[0].append(i.getHourList())
            elif day == 5:  #friday
                LEARNING_SPECIALIST[1].append(i.getHourList())
            elif day == 6:  #saturday
                LEARNING_SPECIALIST[2].append(i.getHourList())
            elif day == 7:  #sunday
                LEARNING_SPECIALIST[3].append(i.getHourList())
            else:  #work days
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
        if not if_holida( dane[i].getDate().day, dane[i].getDate().month, dane[i].getDate().year):
            if weekday == 1:  # monday
                LEARNING_SPECIALIST_OUTPUT[0].append(dane[i].getHourList())
            elif weekday == 5:  # friday
                LEARNING_SPECIALIST_OUTPUT[1].append(dane[i].getHourList())
            elif weekday == 6:  # saturday
                LEARNING_SPECIALIST_OUTPUT[2].append(dane[i].getHourList())
            elif weekday == 7:  # sunday
                LEARNING_SPECIALIST_OUTPUT[3].append(dane[i].getHourList())
            else:  # work days
                LEARNING_SPECIALIST_OUTPUT[4].append(dane[i].getHourList())
        i += 1
    return target


TARGET = prepare_target()
INPUT = prepare_input()


def single_network(input_, target_, test_input, test_output, net1):
    """" Return learned network and, outpur,regression for test """
    network = net1.train_rprop(input_, target_, mimin=1e-06, mimax=500.0,
                               xmi=0.2, maxiter=100, disp=0)
    # run our neuronal network
    output, regression = net1.test(test_input, test_output, iprint=0)
    # test network
    summ = 0.0
    for index in range(len(output)):
        for j in range((len(output[index]))):
            summ = summ + ( (abs(float(target_[index][j]) - float(output[index][j]))) / float(target_[index][j]) )
    #print summ, summ/len(test_output) # print error for all networks
    return network, output, regression, (summ / len(test_output))


def calculate_network(input_, target_, test_input, test_output, net1):
    network, output, regression, error = single_network(input_, target_, test_input, test_output, net1)
    for i in range(4):
        network1, output1, regression1, error1 = single_network(input_, target_, test_input, test_output, net1)
        if (error1 < error):
            network = network
            output = output1
            regression = regression1
            error = error1
    return network, output, regression, error


CONEC = tmlgraph((54, 10, 24))  # model of connections
NET = ffnet(CONEC)


# NX.draw_graphviz(net.graph, prog='dot') show the network that's nice!
# pl.show()
#
# calculate special days
summ_error = 0.0
for i in range(4):
    net = ffnet(CONEC)  # year have 52 weeks so, we have 52 special days in year
    network, output, regression, error = calculate_network(
        LEARNING_SPECIALIST[i][:-52],
        LEARNING_SPECIALIST_OUTPUT[i][:-52],
        LEARNING_SPECIALIST[i][-52:],
        LEARNING_SPECIALIST_OUTPUT[i][-52:], net)
    summ_error += error
    print "COMMITTE LEADER: ", error
# calculate work days
network, output, regression, error = calculate_network(LEARNING_SPECIALIST[4][:-156],
                                                       LEARNING_SPECIALIST_OUTPUT[4][:-156],
                                                       LEARNING_SPECIALIST[4][-156:],
                                                       LEARNING_SPECIALIST_OUTPUT[4][-156:], NET)

print "WORK DAY LEADER: ", error
summ_error + error

average_list = []
average_day = []
for i in range(13):
    for j in range(23):
        average_list.append((float(training_holidays[i][1][j]) + float(training_holidays[i+13][1][j]) + float(training_holidays[i+26][1][j]))/3.0)
    average_day.append(average_list)
    average_list = []
print len(average_day)
index = 0
h_error = 0.0
for i in training_holidays[-13:]:
    tmp = 0.0
    for j in range(23):
        tmp += abs(float(i[1][j]) - float(average_day[index][j])) / float(i[1][j])
    h_error += tmp/23.0
    index += 1
print "H error", h_error/13.0
print "summ_error: ", summ_error /5.0
print "Total error", ( summ_error / 5.0 + (h_error / 13.0))




