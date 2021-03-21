from math import ceil
from random import randint, shuffle, seed


def insertion_sort(T, p, r): # przedział prawostronnie otwarty
    for i in range(p+1, r):
        key = T[i]
        j = i-1
        while j >= p and T[j] > key:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = key
    return T


def median(T, p, r): # sortuję liczby z podanego przedziału -> po 5 elementów albo mniej i zwracam index środkowego i będzie to mediana
    insertion_sort(T, p, r)
    return (p+r)//2


def partition(T, p, r, pivot):
    T[pivot], T[r] = T[r], T[pivot]
    i = p-1
    for j in range(p, r):
        if T[j] <= T[r]:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


def select(T, p, r, k):
    median_idx = median_medians(A, p, r)
    if median_idx == k:
        return T[k]
    elif median_idx < k:
        return select(T, median_idx+1, r, k)
    else:
        return select(T, p, median_idx-1, k)


def median_medians(A, p, r): # Tablica, przedział [a,b]
    n = r-p+1 # ilość elementów w przedziale
    index = p # na początek danego przedziału będę przestawiał wszystkie mediany
    start = p
    end = r
    if n <= 5: # przedział mniejszy elementów max 5 ->  tworze mediane i dziele na podstawie mediany elementy
        pivot = median(A, p, r)
        q = partition(A, start, end, pivot)
        return q
    for i in range(p, r, 5): # sortuje przedziały po 5 elementów, wyciągnam z nij mediany i przerzucam na początek przedziału
        if i+5 > r:
             break
        r = i+5
        q = median(A, i, r)
        A[index], A[q] = A[q], A[index]
        index += 1
    if n % 5 != 0: # ostatni przedział zawierał bym mniej niz 5 elementów
        r = n+start
        p = start + (n - n % 5)
        q = median(A, p, r)
        A[index], A[q] = A[q], A[index]
    if ceil(n/5) < 5:
        r = ceil(n/5)+start
        pivot = median(A, start, r)
    else:
        pivot = median_medians(A, start, ceil(n/5)+start) # rekurencyjnie zaczynam liczyć mediane median
    q = partition(A, start, end, pivot)
    return q


def linearselect(A, k):
    value = select(A, 0, len(A)-1, k)
    return value


seed(42)
n = 25
for i in range(n):
    A = list(range(n))
    shuffle(A)
    print(A)
    x = linearselect( A, i )
    if x != i:
        print("Blad podczas wyszukiwania liczby", i)
        exit(0)
    
print("OK")


