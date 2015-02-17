__author__ = 'piotr'


def toByte(liczba):
    L = str(liczba).split(".")
    output = ""
    if (liczba > 0):
        output = "0"+ bin(int(L[0]))[2:] + "." + bin(int(L[1]))[2:]
    else :
        output = "1" + bin(int(L[0]))[3:] + "." + bin(int (L[1]))[2:]
    while len(output.split(".")[1]) < 2:
        output += '0'
    if len(output.split(".")[1]) > 2:
        t = len(output.split(".")[1]) - 2;
        return output[0:len(output)-t]
    return output

def toDecimal(liczba):
    L = str(liczba).split(".")
    output = "";
    znak = 1.0;
    if (L[0][0] == '1'):
        znak = -1.0;
    print L[0][1:len(L[0])]
    output += str( int((L[0][1:len(L[0])]),2) )+ "." + str(int(L[1],2))
    return float(output) * znak;
