# 9.Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie jeden raz.
# Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz.
# Mówimy, że liczba naturalna A jest ładniejsza od liczby naturalnej B, 
# jeżeli w liczbie A występuje więcej cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych
#  jest tyle samo to ładniejsza jest ta liczba, która posiada mniej cyfr wielokrotnych.
#  Na przykład: liczba 123 jest ładniejsza od 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
# Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję: pretty_sort(T),
# która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm powinien  być  możliwie  jak  najszybszy.  Proszę  w  rozwiązaniu  umieścić  1-2  zdaniowy  opis algorytmu oraz proszę oszacować jego złożoność czasową.

from math import ceil, log10
from random import randint
# od najładniejszych do najmniej ładnych
# 133 = 155 == 555 > 1122
# Radixsort + countsort

def digits(n):
    Arr = [0] * 10
    while n>0:
        Arr[n%10] += 1
        n //=10
    return Arr


def beautiful_numbers(n):
    Arr = digits(n)
    single = 0    
    duplicates= 0
    for el in Arr:
        if el == 1:
            single += 1
        if el >= 2:
            duplicates += 1
    return (single*10)+duplicates


def count_sort(Arr,k):
    n = len(Arr)
    # za 1wszym malejąco, za drugim rosnąco
    Arr_count = [0]*10
    Arr_sorted = [None] * n
    for el in Arr:
        if k == 1:
            Arr_count[beautiful_numbers(el)%10] += 1
        else:
            Arr_count[beautiful_numbers(el)//10] += 1
    for i in range(1,10):
        Arr_count[i] += Arr_count[i-1]

    for i in range(n):
        if k == 1: #
            Arr_sorted[Arr_count[beautiful_numbers(Arr[i])%10]-1] = Arr[i]
            Arr_count[beautiful_numbers(Arr[i])%10] -= 1
        else:
            Arr_sorted[Arr_count[beautiful_numbers(Arr[i])//10]-1] = Arr[i]
            Arr_count[beautiful_numbers(Arr[i])//10] -= 1
            
    if k == 1:
        for i in range(n):
                Arr[i] = Arr_sorted[i]
        return
    for i in range(n):
        Arr[i] = Arr_sorted[n-1-i]


def radix_sort(Arr):
    for i in range(1,-1,-1): # [a,b)
        count_sort(Arr,i)
    return Arr


Arr = [randint(1,1111) for _ in range(150)]
print(radix_sort(Arr))

