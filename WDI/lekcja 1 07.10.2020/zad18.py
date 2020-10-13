# Zmodyfikować wzór Newtona aby program z zadania 5 obliczał pierwiastek stopnia 3
import time
def zad18(liczba):
    a = liczba 
    b = 0
    while 1:
        a = (a + b) / 3 # zamienienie dwójki z trójką liczy 3Ciego stopnia pierwiastek
        b = liczba / a
        print(a)
        time.sleep(0.1)


zad18(8)