from math import pi
import time


def silnia_liczby(n):
    wynik_z_silni = 1
    i = 1
    if n == 0:
        wynik_z_silni = 1 # domyslnie 0! jest rowne niby 1 ale tutaj funkcja nie ma pojecia o tym dlatego recznie wpisuje dla n = 0
    while i <= n:
        wynik_z_silni *= i
        i += 1
    return wynik_z_silni


def pochodna_dla_cos_maclaurinem(stopien_pochodnej):
    if stopien_pochodnej %4 == 1: return 0 # chyba dobrze uwarunkowane, ze dla co czwartego elementu ta sama wartosc ma byc przybierana  
    if stopien_pochodnej %4 == 2: return -1 
    if stopien_pochodnej %4 == 3: return 0
    if stopien_pochodnej %4 == 0: return 1

def cosinus_liczby(x):
    wynik = 0
    # poprzedni = 1
    stopien = 1
    while 1: # nieskonczona petla z wyniku danego cosinusa
        wynik += pochodna_dla_cos_maclaurinem(stopien)/silnia_liczby(stopien)  
        print(wynik)
        stopien += 1
        time.sleep(0.3)



cosinus_liczby(pi/17)

# jak powinno leciec

# cos(x) = 1/0! - (0/1!)x - (1/2!)x^2 + (0/3!)x^3 + (1/4!)x^4 cosik takiego 

# pochodne powtazaja sie co 4 samo cos pochodne rozpisane
# f(x) = cosx
# f'(x) = -sinx
# f''(x) = -cosx
# f3(x) = sinx
# f4(x) = cos(x)
# f5(x) = f(x)


# Napisać program obliczający wartości cos(x) z rozwinięcia w szereg Maclaurina
# x0 = 0
# f(x) = f(x) + f'(0)x
# Zakładam, że wiadomo że cos(x)=0 cos'(x)=0 cos''(x) = -1  cos'''(x) = 0 i cos''''(x) = cos(x) itd.

from math import *
iteracje = 5
x = pi/6
wynik = 1  #wartość cos(0)


def silnia(y):
    s = y
    while y > 1:
        y -= 1
        s *= y
    return s


for i in range(1, iteracje):
    if i % 2 == 0:
        wynik += (1/silnia(i*2))*pow(x, i*2)
    else:
        wynik -= (1/silnia(i*2))*pow(x, i*2)
print(wynik)