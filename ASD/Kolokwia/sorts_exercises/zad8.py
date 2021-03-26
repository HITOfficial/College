# 1. (implementacyjne) była tablica punktów (structy z intami x, y). Punkt
# 1 dominuje 2 gdy x1 > x2 i y1 > y2 i trzeba było podać liczność
# najmniejszego zbioru z nich by wybrane punkty dominowały wszystkie pozostałe

# bucketsort
from math import floor, ceil
from random import randint


def bubble_sort(Arr,k):
    for i in range(len(Arr)-1):
        for j in range(i+1,len(Arr)):
            if Arr[j][k] > Arr[j-1][k]:
                Arr[j], Arr[j-1] = Arr[j-1], Arr[j]


def bucket_sort(Arr,k):
    n = len(Arr)
    el_min= Arr[0][k]
    el_max= Arr[0][k]
    for el in Arr:
        el_min = min(el_min,el[k])
        el_max = max(el_max,el[k])
    el_max = floor(el_max)+1
    buckets = [list() for _ in range(n)]
    for el in Arr:
        index = floor(((el[k]-el_min)/(el_max-el_min))*n)
        buckets[index].append(el)
    for bukcet in buckets:
        bubble_sort(bukcet,k)
    i = 0
    for bucket in buckets:
        if len(bucket) ==0:
            continue
        else:
            for el in bucket:
                Arr[i] = el
                i += 1


def binary_search(Arr,k,l,r):
    half = l+(r-l+1)//2
    if Arr[l][1] > k or Arr[r][1] <k or r == -1: # zeby nie wyskoczyć poza zakres
        return False
    if Arr[half][1] == k:
        lowest = binary_search(Arr,k,l,half-1)
        if lowest is not False:
            return lowest
        else:
            return half
    if Arr[half][1] > k: # idę w lewo
        return binary_search(Arr,k,l,half-1)
    else: # idę w prawo
        return binary_search(Arr,k,half+1,r)

        
# Tworze dwie pomocnicze tablice, sortuję ją po danej wartości X lub Y oraz wstawiam index pod którym stoi w pierwotnej
# szukam dominacji binary searchem po X i po Y, aby zliczyć ile elementów dominują, i zwracam większą z dominacji
def count_domination(Arr):
    dominationsX = dominationsY =  0
    n = len(Arr)
    X_sort = [(Arr[i][0],i) for i in range(n)]
    bucket_sort(X_sort,0)
    Y_sort = [(Arr[i][1],i) for i in range(n)]
    bucket_sort(Y_sort,0)
    startX = startY = 0
    for i in range(n-1,-1,-1): # lece od elementu dominującego wszystkie po X'ach i sprawdzam które elementy jego współrzędna po Y dominuje inne i na odwrót
        tmpX = binary_search(X_sort,Y_sort[i][1], startY, n-1) # znajduję pod którym elementem jest w drugiej tablicy ten index
        tmpY = binary_search(Y_sort,X_sort[i][1], startX, n-1)
        if tmpX is not False and tmpX > startX: # albo już wykluczyłem ten element bo był już wcześniej dominowany (False), jest na początku przedziału, więc nie dominuje żadnego elementu
            startX = tmpX
            dominationsX += 1
        if tmpY is not False and tmpY > startY:
            startY = tmpY
            dominationsY += 1
    return max(dominationsX,dominationsY)  # zwracam większą liczbę dominacji


Arr =[(randint(-10000,10000),randint(-10000,10000)) for _ in range(20000)]
print(count_domination(Arr))