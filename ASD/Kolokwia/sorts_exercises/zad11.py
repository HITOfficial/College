# Największy przedział Dany ciąg przedziałów [a1,b1],....[an,bn].
# Prosze zaproponować algo, który znajduje przedział zawierający nwjwiecej pozostałych przedziałów
from math import floor
from random import randint
# bucket sort + quicksort

# coo'rdinates  (A,B)
def partition(Arr,l,r):
    pivot = Arr[l][0]
    limit = r+1
    for i in range(r,l,-1):
        if Arr[i][0] > pivot:
            limit -= 1
            Arr[limit], Arr[i] = Arr[i], Arr[limit]
    limit -= 1
    Arr[l], Arr[limit] = Arr[limit], Arr[l]
    return limit


def quick_sort(Arr,l,r):
    if l<r:
        limit = partition(Arr,l,r)
        quick_sort(Arr,l,limit-1)
        quick_sort(Arr,limit+1,r)


def bucket_sort(Arr):
    n = len(Arr)
    el_min = el_max = Arr[0][0]
    for el in Arr:
        el_min = min(el_min,el[0])
        el_max = max(el_max,el[0])
    el_max = floor(el_max) + 1

    buckets = [list() for _ in range(n)]
    for el in Arr:
        index = floor((el[0]-el_min)/(el_max-el_min)*n)
        buckets[index].append(el)
    for bucket in buckets:
        quick_sort(bucket,0,len(bucket)-1)
    i = 0
    for bucket in buckets:
        for j in range(0,len(bucket)):
            Arr[i] = bucket[j]
            i += 1
    return Arr
    
def area(Arr):
    n = len(Arr)
    bucket_sort(Arr)
    count_max = 0
    for i in range(n-1):
        count = 0
        for j in range(i+1,n):
            if Arr[i][1] > Arr[j][1]:
                count += 1
        count_max = max(count_max,count)
    return count_max


n = 10000
Arr = [(randint(1,10000),randint(11000,100000)) for _ in range(n)]
print(area(Arr))

