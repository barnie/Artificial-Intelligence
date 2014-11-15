__author__ = 'piotr'

import datetime


class electric_day:
    def __init__(self, row):
        # print row[1]
        self.date = datetime.datetime.strptime(row[1], '%Y-%m-%d').date()
        self.electric_hours = row[2:]

    def getDate(self):
        return self.date

    def getHourList(self):
        return self.electric_hours

    # from 0 to 23
    def getElectricByHour(self, hour):
        return self.electric_hours[hour]


