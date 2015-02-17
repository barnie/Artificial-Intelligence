import random
import pickle

def funkcja1(a,b,c):
    return ((a*a)+(b*b))/c;

def funkcja2(d,e):
    return (d*d) + (e*e);



if __name__ == '__main__':
    j = 0;
    lista = [];
    while j < 800:
        tmp = [random.random() + 1 for i in range(5)]
        a = funkcja1(tmp[0], tmp[1], tmp[2])
        b = funkcja2(tmp[3], tmp[4])
        tmp.append(a)
        tmp.append(b)
        j += 1
        lista.append(tmp)
    print lista
    pickle.dump(lista,open("save.p","wb"))
