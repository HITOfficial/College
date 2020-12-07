# Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym iloczynie.

from random import randint


# dodatkowo wypisuję z których elementów iloczyn tworzy tą wartość
count = 0 # na globalnej zmiennej zliczam

def find_multiply_combinations(list_t, val_to_find, numbers, start=0, end=None, multiply_actual =1, l=[]): # określony iloczyn, "enki", aktualna enka, iloczyn już znaleziony
    if end == None: # warunek aby sobie sprawdzić do którego elementu ma byc szukany pierwszy z tablicy
        end = numbers-1

    if len(l) == numbers:
        if multiply_actual == val_to_find:
            global count
            count += 1
            print(l)
        return

    for i in range(start, len(list_t)-(end)):
        find_multiply_combinations(list_t, val_to_find, numbers, i+1, end-1, multiply_actual * list_t[i], [*l, list_t[i]]) # przy każdej kolejnej rekurencji zaczynam od range(i+1,dotychczasowy zakres -1)



t = [randint(1,8) for _ in range(17)]

find_multiply_combinations(t,12,3)
print(count)