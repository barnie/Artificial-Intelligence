__author__ = 'piotr'

class Pair:

    def __init__(self, x, y):
        self.x = x
        self.y = y;

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x;

    def setY(self, y):
        self.y = y;

    def getList(self):
        return [self.x, self.y]

    def toStr(self):
        return "" + str(self.x) + " -> " + str(self.y);
