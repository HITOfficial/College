num = int(input('wprowadz liczba, a sprawdze podzielniki: '))

def podzielniki_liczby(liczba):
    i = 1
    while i <= liczba:
        if(liczba % i == 0):
            print(i)
        i+=1


podzielniki_liczby(num)