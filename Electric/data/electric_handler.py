__author__ = 'piotr'
import csv
from electric_day import electric_day as el
from electric_month import electric_month
from electric_year import electric_year


class electric_hander:
    def __init__(self):
        electric_day = []
        electric_months = []
        self.electric_years = []
        print "START LOADING DATA"
        with open('electric.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                electric_day.append(el(row))
        month = []
        prev = electric_day[0]
        for day in electric_day:
            if day.getDate().month == prev.getDate().month:
                month.append(day)
            else:
                electric_months.append(electric_month(prev.getDate().month, month))
                month = []
                month.append(day)
            prev = day
        month = []
        prev = electric_months[0]
        for y in electric_months:
            if y.getYear() == prev.getYear():
                month.append(y)
            else:
                self.electric_years.append(electric_year(prev, month))
                month = []
                month.append(y)
            prev = y
        print "LOADING DATA COMPLETED"

    def printYears(self):
        for y in self.electric_years:
            print "#####################################################"
            print y.getYear()
            for m in y.getMonths():
                print m.getMiesiac()
                for d in m.getDays():
                    print d.getDate().day, d.getHourList()
            print "######################################################"

    def getYears(self):
        return self.electric_years

    def getYear(self, year):
        return self.electric_years[year]

    def getMonth(self, year, month):
        return self.electric_years[year].getMonths()[month]

    def getDay(self, year, month, day):
        return self.electric_years[year].getMonths()[month].getDays()[day]


def main():
    e = electric_hander()
    e.getYears()
    e.getYear(1)
    e.getMonth(1,2)
    print e.getDay(1,1,1).getHourList()

main()