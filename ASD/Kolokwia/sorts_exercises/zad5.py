# 6.Dane jest n punktów na osi liczbowej jednowymiarowej. Napisz algorytm, który stwierdzi,
# w którym z nim należy wybudować dom, tak aby suma euklidesowych odległości od tego punktu
#  do wszystkich pozostałych była minimalna. Należy zwrócić również tę sumę.
#  Algorytm powinien być jak najszybszy.

# sortuje elementy
from random import randint
 
n = 10
Arr = [randint(1,500) for _ in range(n)]

def place_for_house(Arr):
    Arr.sort()
    half = len(Arr)//2
    if len(Arr)%2 == 0: # parzysta
        return (Arr[half+1]-Arr[half-1])/2 + Arr[half-1]
    else:
        return Arr[n//2]

