# A - tablica zawierajaca n parami roznych liczb (nieposortowana)
# Prosze znaleźć liczby A[i], A[j], takie że 
# a) A[i], A[j] jest jak największe # róznica wartości najwieksza, i brak el pomiedzy
# b) nie ma liczby A[t]: A[i]>A[t]>A[j]

# różnica w wartościach jest najwieksza

from random import random
from math import floor, ceil
n =  10
Arr = [(random()*4)+2 for _ in range(n)] # 2-6 <- (0,1) -> (0,4) -> (2,6)  


def bubble_sort(Arr):
    for i in range(len(Arr)-1):
        for j in range(i+1,len(Arr)):
            if Arr[j] < Arr[j-1]:
                Arr[j], Arr[j-1] = Arr[j-1], Arr[j]
    return Arr


def max_diff(Arr):
    n = len(Arr)
    el_min = min(Arr)
    el_max = ceil(max(Arr))
    Arr_sorted = [list() for _ in range(n)]
    for el in Arr: # kubełkowanie
        index = floor(((el-el_min)/(el_max-el_min)) * n)
        Arr_sorted[index].append(el)
    biggest_diff = 0
    
    for i in range(n):
        bubble_sort(Arr_sorted[i])

    i = 0;
    while i < n-1:
        Arr_l_len = len(Arr_sorted[i])
        if Arr_l_len == 0: # pusty kubełek
            i += 1
            continue
        Arr_l_max = Arr_sorted[i][Arr_l_len-1]
        j = i+1
        while j < n:
            i = j
            if len(Arr_sorted[j]) == 0: # pusty kubełek
                j += 1
                continue
            Arr_r_min = Arr_sorted[j][0]
            biggest_diff = max(biggest_diff, Arr_r_min - Arr_l_max)
            break

    return biggest_diff

print(max_diff(Arr))

