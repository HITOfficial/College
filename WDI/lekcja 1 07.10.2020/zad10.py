# liczba piekna - liczba naturalna ktora jest rowna liczbie podzielnikow mniejszych od tej liczby
# 6 = 3+2+1 liczba pierwsza

# TODO wyszukac podzielniki danej liczby
# dodac wszystkie podzielniki tej liczby i sprawdzic czy sa one rowne tej liczbie a jesli tak

# podzielniki do tablicy

def podzielniki_liczby(liczba):
    liczba_podzielniki = []
    i = 1
    while i <= liczba:
        if(liczba % i == 0):
            liczba_podzielniki.append(i)
        i+=1
    return liczba_podzielniki


def suma_dzielnikow(lista):
    suma = 0
    for el in lista[0:-1]: # bo jest podzielna przez sama siebie, ale musimy ja obciac w sprawdzaniu, czy jest ona liczba piekna
        suma += el
    return suma

def liczby_piekne(przedzial):
        
    liczba = 1
    while liczba <= przedzial:
        if liczba == suma_dzielnikow(podzielniki_liczby(liczba)):
            print(liczba)
        liczba+=1

liczby_piekne(1_000_000)