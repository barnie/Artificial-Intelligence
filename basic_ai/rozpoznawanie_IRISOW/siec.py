import random
import math


global flower_list
flower_list = []


def readFile():
    with open("../IRIS/iris.data") as f:
        content = f.readlines()

    for i in content:
        a = float(i[0:3])
        b = float(i[4:7])
        c = float(i[8:11])
        d = float(i[12:15])
        k = Flower(a,b,c,d,i[16:len(i)-1])
        flower_list.append(k)
    f.close();


class Flower:

    def __init__(self,x,y,z,w, nazwa):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.nazwa = nazwa
    def show(self):
        print self.x,self.y,self.z,self.w,self.nazwa
    def getList(self):
        return [self.x, self.y, self.z, self.w]
    def getName(self):
        return self.nazwa

class Neuron:
    def __init__(self, length):
        self.length = length
        self.weights = [random.uniform(1,10)  for i in range(self.length)]
        self.output = 0
        self.activation = [0,0,0]
        self.suma = 0.0

    def add_activation(self,cos):
        if cos == flower_list[1].getName():
            self.activation[0] += 1
        elif cos == flower_list[51].getName():
            self.activation[1] += 1
        elif cos == flower_list[102].getName():
            self.activation[2] += 1

    def calc(self,wejscie):
        self.suma = 0.0
        for i in range(self.length):
            self.suma += wejscie[i] * self.weights[i];
    def getCalc(self):
        return self.suma
    def getActivation(self):
        return self.activation
    def getOutput(self):
        return self.output
    def getWeights(self):
        return self.weights





def norma(wektor):
    suma = 0.0;
    for i in range( len(wektor) ):
        suma += wektor[i] * wektor[i]
    return math.sqrt(suma)

def normalization(wektor):
    suma = norma(wektor)
    for i in range( len(wektor) ):
        wektor[i] = wektor[i] / suma;
    return wektor


def m_euclides(x, weights):
    wynik = 0.0
    for i in range(len(x)):
        wynik += pow( (x[i] - weights[i]) , 2)
    return math.sqrt(wynik)

def cos_vector(x, weights):
    wynik = 0.0
    for i in range( len(x) ):
        wynik += x[i] * weights[i]
    wynik = wynik / (norma(x) * norma(weights))
    return wynik

def scalar_distance(x, weights):
    return ( 1.0 - ( norma(x) * norma(weights) * cos_vector(x,weights) ) )

def vector_difference(x,weights):
    suma = 0.0
    for i in range( len(x) ):
        suma += x[i] - weights[i]
    return suma

global learn;
learn = []
global verify;
verify = []

def randomize(): #losowanie 30 - uczace 20 - weryfikujace
    for i in range(30):
        learn.append(flower_list[random.randint(0,49)])
    for i in range(30):
        learn.append(flower_list[random.randint(50,99)])
    for i in range(30):
        learn.append(flower_list[random.randint(100,149)])
    for i in range(20):
        verify.append(flower_list[random.randint(0,49)])
    for i in range(20):
        verify.append(flower_list[random.randint(50,99)])
    for i in range(20):
        verify.append(flower_list[random.randint(100,149)])
    for i in range(90):
        normalization(learn[i].getList())
h = 2.0/5.0 #moje h moj krok o ktory ide

def net():
    randomize() # vectors
    Neurons = [] #neuronal network
    for i in range(10000):
        Neurons.append(Neuron(4)) #init neurons
    for i in range(100): #how long we learn
        for k in range (90): # for every input
            for j in range( len(Neurons) ): # for every neuron
                Neurons[j].calc( learn[k].getList() ) #in here we just do for i in range(len(input)): sum += input[i] * x[i]
            index_winner = 0
            d_winner = 100000.0
            for j in range( len(Neurons) ):
                tmp = scalar_distance(learn[k].getList(), Neurons[j].getWeights()) #get distance
                if (d_winner > tmp):
                    index_winner = j
                    d_winner = tmp
            Neurons[index_winner].output = 1
            Neurons[index_winner].add_activation(learn[k].getName())
            our_h = h * vector_difference(learn[k].getList(), Neurons[index_winner].getWeights());
            for o in range (4):
                Neurons[index_winner].weights[o] += our_h;
        if i <= 2: #Optimalization
            for x in Neurons:
                _list = x.getActivation()
                if ( _list[0] < 2 or _list[1] < 2 or _list[2] < 2 ):
                    Neurons.remove(x)
            for x in Neurons:
                _list = x.getActivation()
                if ( _list[0] < 2 or _list[1] < 2 or _list[2] < 2 ):
                    Neurons.remove(x)
    
    print "***********Validation**************"
    for x in Neurons:
        x.activation = [0,0,0]
    for i in range(60):
        for j in range( len(Neurons) ): # dla kazdego neuronu
            Neurons[j].calc( verify[i].getList() )
            index_winner = 0
            d_winner = 100000.0
        for j in range( len(Neurons) ):
            tmp = scalar_distance(verify[i].getList(), Neurons[j].getWeights())
            if (d_winner > tmp):
                index_winner = j
                d_winner = tmp
            Neurons[index_winner].output = 1
            Neurons[index_winner].add_activation(verify[i].getName())

    counter = 0
    for x in Neurons:
        if x.getActivation()[0] != 0 or x.getActivation()[1] != 0 or x.getActivation()[2]:
            print counter, " " ,x.getActivation();
            counter += 1


if __name__ == '__main__':
    readFile()
    net()
