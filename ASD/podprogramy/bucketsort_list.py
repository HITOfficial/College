from math import floor
from time import time


def bubblesort(T):
    for i in range(len(T)-1):
        for j in range(i+1,len(T)):
            if T[i] > T[j]:
                T[i], T[j] = T[j], T[i]
    return T


def bucketsort(T,a=0,b=1): # Table, przedzial defaultowo [0-1) bo inaczej muszę przedział przekręcić
    n = len(T)
    B = [list() for _ in range(n)] # kubełki
    for el in T:
        # rozpisałem na kartce i działa
        index = floor(((el-a)/(a+b))*n) # przestawienie na przedział 0-1 -> ((element - dół przedziału) / (suma granic przedziału)) * ilość elementów w przedziale
        B[index].append(el) # podłoga ponieważ indexy liczymy od 0
    for b_id in range(n): # bucket id
        B[b_id] = bubblesort(B[b_id])
    T_id = 0 # Table id
    for bucket in B:
        for el in bucket:
            T[T_id] = el
            T_id += 1
    return T