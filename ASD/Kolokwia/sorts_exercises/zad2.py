# 3.Dana jest tablica liczb rzeczywistych wielkości n reprezentująca kopiec minimum (array-based heap).
# Mając daną liczbę rzeczywistą x sprawdź, czy k-ty najmniejszy element jest większy lub równy x.
from random import randint
n = 15
T = [321,43123,3123,12,22,2]


def heapsort(T,k,x):

    def heapyfy(T,n,i): # table, len(T), index rodzica
        left = 2*i +1
        right = 2*i +2
        i_copy = i
        if left < n and T[left] > T[i]: i_copy = left
        if right < n and T[right] > T[i_copy]: i_copy = right
        if i != i_copy: # znalezione dziecko z wartoscia wieksza
            T[i], T[i_copy] = T[i_copy], T[i]
            heapyfy(T,n, i_copy) # szuka poddzieci do dzieci

    n = len(T)
    def build_heap(T,n): # Tworzymy sens kopca -> każdy rodzic ma mniejsze dzieci
        for i in range(((n//2)-1),-1,-1): # budowa kopca
            heapyfy(T,n,i)
            
    build_heap(T,n)
    for i in range(n-1,n-k-1,-1):
        T[0], T[i] = T[i], T[0] # podmieniam aktualnie znaleziony najwiekszy z kolejnymi elementami od konca z tablicy
        heapyfy(T,i,0)
    print(T)
    if T[n-k] == x:
        return True
    return False


print(T)
print(heapsort(T,2,3123))
