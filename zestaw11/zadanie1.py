#11.1
import random
import math

def losowe_liczby(size):
    L = []
    for i in range(0, int((random.random())*1000)):
        L.append(random.randint(0, size-1))
    return L

def prawie_posortowana(size):
    L = []
    for i in range(0, int((random.random())*1000)):
        if i % 2 == 0:
            L.append(i+1)
        else:
            L.append(i-1)
    return L

def prawie_posortowana_odwrotnie(size):
    L = prawie_posortowana(size)
    L.reverse()
    return L

def losowe_gauss(size, mu, sigma):
    L = []
    for x in range(0, int((random.random())*1000)):
        L.append(random.gauss(mu, sigma))
    return L

def losowe_set(size):
    L = []
    for i in range(0, size):
        L.append(random.randint(0, int(math.sqrt(size))))
    return L

#print(losowe_liczby(6))
#print(prawie_posortowana(6))
#print(prawie_posortowana_odwrotnie(6))
#print(losowe_gauss(1, 6, 1))
#print(losowe_set(6))
