__author__ = 'piotr'


class electric_month:
    def __init__(self, index, days):
        self.index = index - 1
        self.days = days
        self.months = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze', 'Lip', 'Sie', 'Wrz', 'Paz', 'Lis', 'Gru']
        self.miesiac = self.months[self.index]

    def getMonth(self):
        return self.index

    def getDays(self):
        return self.days

    def getMiesiac(self):
        return self.miesiac

    def getYear(self):
        return self.days[0].getDate().year