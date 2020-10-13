# Zadanie 5. Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.
import time
def zad5(liczba):
    a = liczba 
    b = 0
    eps = 0.000_001
    while abs(a - b) > eps:
        a = (a + b) / 2
        b = liczba / a
        print(a)
        time.sleep(0.3)


zad5(8)