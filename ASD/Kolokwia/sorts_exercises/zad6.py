# Dana jest tablica A oraz liczba k. Znaleźć liczbę różnych par elementów z tablicy A o różnicy równej k.
# Przykład: Dla tablicy [7,11,3,7,3,9,5] oraz k = 4 odpowiedź to 3
from random import randint
n= 1000
Arr = [randint(1,100) for _ in range(n)]


def find_pairs(Arr,k): # zakładam, że parę tworzą unikalne indexy a nie unikalne wartosciach
    Arr.sort()
    n = len(Arr)
    count = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if Arr[j]-Arr[i] > k:
                break
            if Arr[j]-Arr[i] == k:
                count += 1
                
    return count