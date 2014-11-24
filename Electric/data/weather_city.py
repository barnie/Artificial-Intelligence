__author__ = 'piotr'
import csv


class weather_cit:
    def __init__(self, city):
        self.rows = []
        with open('/home/piotr/Projects/Advanced_Method_Of_AI/Electric/Electric/data/' + city + ".csv", 'rb') as f:
            reader = csv.reader(f)
            j = 0
            prev = 0
            tmp1 = tmp2 = tmp3 = tmp4 = 0;
            for i in reader:
                if prev == 0:
                    prev = i[2]
                if prev == i[2]:
                    self.row = i
                    j+=1
                    tmp1 += float(self.row[3])
                    if float(self.row[4]) < 200:
                        tmp2 += 998.5
                    else:
                        tmp2 += float(self.row[4])
                    tmp3 += float(self.row[5])
                    tmp4 += float(self.row[6])
                elif prev != i[2]:
                    self.rows.append([i[0], i[1], i[2], tmp1/j, tmp2/j, tmp3/j, tmp4/j])
                    tmp1 = tmp2 = tmp3 = tmp4 = 0
                    prev = i[2]
                    j = 0
                j = j + 1
        print len(self.rows)

    def getWeather(self):
        return self.rows

    def printWeather(self):
        for i in self.rows:
            print i