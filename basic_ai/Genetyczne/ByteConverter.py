__author__ = 'piotr'

def float_to_binary(num):
    exponent=0
    shifted_num=num
    while shifted_num != int(shifted_num):
        shifted_num*=2
        exponent+=1
    if exponent==0:
        return '{0:0b}'.format(int(shifted_num))
    binary='{0:0{1}b}'.format(int(shifted_num),exponent+1)
    integer_part=binary[:-exponent]
    fractional_part=binary[-exponent:].rstrip('0')
    return '{0}.{1}'.format(integer_part,fractional_part)



def floathex_to_binary(floathex):
    num = float.fromhex(floathex)
    return float_to_binary(num)

def toByte(liczba):
    L = str(liczba).split(".")
    output = ""
    if (liczba > 0) :
        output = "0"+ bin(int(L[0]))[2:] + "." + bin(int(L[1]))[2:]
    else :
        output = "1" + bin(int(L[0]))[3:] + "." + bin(int (L[1]))[2:]
    while len(L[1]) < 2:
        L[1] += '0'
        output += '0'
    print output
    if len(L[1]) > 2 :
        return output [:(len(L[1])-2)]
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
