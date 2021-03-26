# 4.Dana jest nieskończona tablica A, gdzie pierwsze n pozycji zawiera posortowane liczby naturalne,
# a reszta tablicy ma wartości None. Nie jest dana wartość n. Przedstaw algorytm, który dla danej liczby
# naturalnej x znajdzie indeks w tablicy, pod którym znajduje się wartość x. Jeżeli nie ma jej w tablicy,
# to należy zwrócić None.

# i = 2**i # szukam ostatni element w tablicy
# lece w prawo potęgowo (2**i) aż przelece do:wartosci none -> cofam się wtedy o1/2**j do ostatniego elementu i binary search
from zad1 import binary_search
from random import randint

def last_or_greater(Arr,k):
    i = 1
    while Arr[i] is not None and Arr[i] < k:
        i *= 2 # idę o 2x dalej przy kazdej iteracji
    if Arr[i] is None: # przeskoczyłem za index -> # cofam sie do ostaniego elementu
        while Arr[i] is None:
            i -= 1
    return i


def find_index(Arr,k):
    # tablica jest infinity
    # lecę o 2 razy dalej w każdej iteracji szukając ostatniego elementu, albo trafiając na element: równy szukanej, lub większy od niej, bo tablica jest posortowana do N
    i = last_or_greater(Arr,k) # index N-1 lub T[i]>= k
    if Arr[i] == k:
        return i
    return binary_search(Arr,k,0,i)


Arr =[999999] * 5675670
for i in range(567567):
    Arr[i] = randint(-1000,1000)
Arr.sort()
for i in range(567567,len(Arr)):
    Arr[i] = None

print(find_index(Arr,5))

