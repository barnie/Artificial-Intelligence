__author__ = 'piotr'


def polynomial(_x):
    x = float(_x)
    return round((x * (x * (x * (x * (1.12 + 0) - 1.11) + 5.65) + 11.25) - 14.82), 2)


def getPolynomial(x, a, b, c, d, e):
    return round((x * (x * (x * (x * (a + 0) - b) + c) + d) - e), 2)
