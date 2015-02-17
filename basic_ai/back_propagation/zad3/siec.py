import random
import math
import pickle

beta = 1.0;
ntrain = 300; # ile jest prezentacji zbioru uczacego
maxits = 100000; # max iteracji
errtol = 0.1; #max blad
h = 0.3

def funkcja1(a,b,c):
    return ((a*a)+(b*b))/c;

def funkcja2(d,e):
    return (d*d) + (e*e);


global dane;
dane = []
rozmiar_bledu = 0.1

class Neuron:
    def __init__(self,funkcja,length):
        self.length = length + 1
        self.wagi = [random.random()  for i in range(self.length)]
        self.funkcja = funkcja

    def suma(self,wejscie):
        wejscie.append(1)
        suma = 0.0
        for i in range(self.length):
            suma += wejscie[i] * self.wagi[i];
        return float(suma)

    def wyjscie(self,wejscie):
        return self.funkcja(self.suma(wejscie))


def funkcja_logistyczna(s):
    return 1 / ( 1 + math.pow(math.e,-s))

def pochodna(s):
    licznik = math.pow(math.e,-s);
    mianownik = math.pow(licznik+1,2)
    return licznik / mianownik

def funkcja_id(s):
    return s;

# def propaguj(Neuron X,delta,zalezy,suma,wyjscie):
#     for i in range(len(X.wagi)):
#         X.wagi[i] -= (h*delta)*zalezy*pochodna(suma) * wyjscie

def propaguj(neuron1, neuronOut,delta,lista):
    for i in range(5):
        neuron1.wagi[i] -= (h * delta) * neuronOut * pochodna(neuron1.suma(lista)) * lista[i]
    neuron1.wagi[5] -= (h * delta) * neuronOut * pochodna(neuron1.suma(lista))


def licz_siec():
    print "Start Nauki!"
    A = Neuron(funkcja_logistyczna, 5)
    B = Neuron(funkcja_logistyczna, 5)
    C = Neuron(funkcja_logistyczna, 5)
    D = Neuron(funkcja_logistyczna, 5)
    G = Neuron(funkcja_logistyczna,5)
    H = Neuron(funkcja_logistyczna,5)
    I = Neuron(funkcja_logistyczna,5)
    J = Neuron(funkcja_logistyczna,5)
    K = Neuron(funkcja_logistyczna,5)
    L = Neuron(funkcja_logistyczna,5)
    E = Neuron(funkcja_id, 10)
    F = Neuron(funkcja_id, 10)
    # 5 wejsc + prog
    arr_error = []
    for i in range(800):
        arr_error.append([1000,1000])
    for i in range(300):
        print "i: ", i
        for j in range(800):
            a = dane[j][0]
            b = dane[j][1]
            c = dane[j][2]
            d = dane[j][3]
            e = dane[j][4] #init danych z pickle
            wyjscie1 = dane[j][5] # poprawne wyjscie 1
            wyjscie2 = dane[j][6] # poprawne wyjscie 2
            wyjscieA = A.wyjscie([a,b,c,d,e])
            wyjscieB = B.wyjscie([a,b,c,d,e])
            wyjscieC = C.wyjscie([a,b,c,d,e])
            wyjscieD = D.wyjscie([a,b,c,d,e])
            wyjscieG = G.wyjscie([a,b,c,d,e])
            wyjscieH = H.wyjscie([a,b,c,d,e])
            wyjscieI = I.wyjscie([a,b,c,d,e])
            wyjscieJ = J.wyjscie([a,b,c,d,e])
            wyjscieK = K.wyjscie([a,b,c,d,e])
            wyjscieL = L.wyjscie([a,b,c,d,e])
            wyjscieE = E.wyjscie([wyjscieA,wyjscieB,wyjscieC,wyjscieD,wyjscieG,wyjscieH,wyjscieI,wyjscieJ,wyjscieK,wyjscieL])
            wyjscieF = F.wyjscie([wyjscieA,wyjscieB,wyjscieC,wyjscieD,wyjscieG,wyjscieH,wyjscieI,wyjscieJ,wyjscieK,wyjscieL])
            # neurony wyliczone
            delta1 = -d + wyjscieE
            delta2 = -e + wyjscieF


            # POMIARY BLEDOW!
            print "ERR: ", delta1, " ERR2: ", delta2
            print "d: ",d, "e: ",e,"w1 : ",wyjscieE,"w2 : ",wyjscieF

            if ( delta1 > arr_error[0] or delta2 > arr_error[1]):
               break



            arr_error[j] = [delta1,delta2]
            #poprawianie wag dla wyjsciowych:
            propaguj(A,E.wagi[0],delta1,[a,b,c,d,e])
            propaguj(B,E.wagi[1],delta1,[a,b,c,d,e])
            propaguj(G,E.wagi[2],delta1,[a,b,c,d,e])
            propaguj(I,E.wagi[3],delta1,[a,b,c,d,e])
            propaguj(K,E.wagi[4],delta1,[a,b,c,d,e])

            propaguj(C,F.wagi[0],delta2,[a,b,c,d,e])
            propaguj(D,F.wagi[1],delta2,[a,b,c,d,e])
            propaguj(H,F.wagi[2],delta2,[a,b,c,d,e])
            propaguj(J,F.wagi[3],delta2,[a,b,c,d,e])
            propaguj(L,F.wagi[4],delta2,[a,b,c,d,e])
            E.wagi[0] -= (h*delta1) * wyjscieA
            E.wagi[1] -= (h*delta1) * wyjscieB
            E.wagi[2] -= (h*delta1) * wyjscieC
            E.wagi[3] -= (h*delta1) * wyjscieD
            E.wagi[4] -= (h*delta1) * wyjscieG
            E.wagi[5] -= (h*delta1) * wyjscieH
            E.wagi[6] -= (h*delta1) * wyjscieI
            E.wagi[7] -= (h*delta1) * wyjscieJ
            E.wagi[8] -= (h*delta1) * wyjscieK
            E.wagi[9] -= (h*delta1) * wyjscieL
            E.wagi[10] -= (h*delta1)
            F.wagi[0] -= (h*delta2) * wyjscieA
            F.wagi[1] -= (h*delta2) * wyjscieB
            F.wagi[2] -= (h*delta2) * wyjscieC
            F.wagi[3] -= (h*delta2) * wyjscieD
            F.wagi[4] -= (h*delta2) * wyjscieG
            F.wagi[5] -= (h*delta2) * wyjscieH
            F.wagi[6] -= (h*delta2) * wyjscieI
            F.wagi[7] -= (h*delta2) * wyjscieJ
            F.wagi[8] -= (h*delta2) * wyjscieK
            F.wagi[9] -= (h*delta2) * wyjscieL
            F.wagi[10] -= (h*delta2)
    for i in range(800):
        print "%.20f %.20f"%(arr_error[i][0], arr_error[i][1])
       # print arr_error[i][0],arr_error[i][1]
        #print "%.10f | %.10f",(arr_error[i][0],arr_error[i][1])





if __name__ == '__main__':
    dane = pickle.load(open("save.p","rb"))
    licz_siec()

