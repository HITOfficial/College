# Tablica T jest długości n, ale zawiera tylko log(n) roznych wartości.
# Proszę zaproponować jak najszybszy algorytm sortujący taką tablicę
from random import randint


def number_len(n):
    count = 0
    while n > 0:
        count += 1
        n //=10
    return count


def get_digit(n,digit): # indexowane od 1 od końca
    n_len  = number_len(n)
    if n_len < digit:
        return 0
    else:
        return (n%(10**digit)) // (10**(digit-1))


def count_sort(T,digit):
    count_T = [0]*10
    T_sorted_by_digit = [None] * len(T)

    for el in T:
        count_T[get_digit(el,digit)] +=1
    for i in range(1,len(count_T)):
        count_T[i] += count_T[i-1]
    
    for i in range(len(T)-1,-1,-1):
        T_sorted_by_digit[count_T[get_digit(T[i],digit)]-1] = T[i] # indexy w tablicy od 0 dlatego -1
        count_T[get_digit(T[i],digit)] -= 1


    for i in range(len(T)): # nadpisuje 
        T[i] = T_sorted_by_digit[i]
    

def radix_sort(T):
    max_len=0
    for el in T:
        max_len = max(number_len(el),max_len) # maxymalna długość liczby
    for i in range(1,max_len+1):
        count_sort(T,i)
    return T
