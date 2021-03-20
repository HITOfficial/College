# Proszę zaproponować jak najszybszy algorytm sortujący n elementową tablice
# zawierającą liczby ze zbioru [0,1,2,...,n^2-1]


def dec_to_N(k,n): # k-ty element, system
    T = [k//n,k%n] # końcówka -> k%n, początek -> k//n
    return T


def count_sort(T,part):
    n = len(T)
    count_T = [0] * n
    sorted_T = [None] * n
    for el in T:
        count_T[dec_to_N(el,n)[part]] += 1
    for i in range(1,n):
        count_T[i] += count_T[i-1]

    for i in range(n-1,-1,-1):
        sorted_T[count_T[dec_to_N(T[i],n)[part]]-1] = T[i]
        count_T[dec_to_N(T[i],n)[part]] -= 1
    for i in range(n):
        T[i] = sorted_T[i]


def radix_sort(T):
    for i in range(1,-1,-1):
        count_sort(T,i)
    return T
