# longest pull ascending
from random import randint
A = [randint(1,100) for _ in range(100)]


def print_pull(Arr,Pull_indexes, i):
    if Pull_indexes[i] != None:
        print_pull(Arr,Pull_indexes,Pull_indexes[i])
    print(Arr[i])


def longest_pull(Arr):
    n = len(Arr)
    Pull = [1]* n
    Pull_indexes = [None] * n # dodatkowa tablica w której będę przetrzymywał indexy poprzednika w aktualnym rosnącym podciągu
    for i in range(n):
        longest = Pull[i];
        for j in range(0,i):
            if Arr[j] < Arr[i] and Pull[j]+1 > longest:
                longest = Pull[j] + 1
                Pull_indexes[i] = j # nadpisuje index poprzednika w aktulanym podciągu 
        Pull[i] = longest
    maximum = max(Pull)
    last = Pull.index(maximum) # index ostatniego elementu w najdłuższym rosnącym podciągu
    print_pull(Arr,Pull_indexes,last)
    return maximum


print("length:",longest_pull(A))