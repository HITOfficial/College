# Pojemniki z wodą
from random import randint
from math import floor
n=10
Arr =[(randint(1,100),randint(1,100),randint(1,100),randint(1,100)) for _ in range(21)]


def partiotion(Arr,l,r):
    pivot = Arr[r][2]
    limit = l-1
    for i in range(l,r):
        if Arr[i][2] < pivot:
            limit += 1
            Arr[limit], Arr[i] = Arr[i], Arr[limit]
    limit += 1
    Arr[limit], Arr[r] = Arr[r], Arr[limit]
    return limit


def quick_sort(Arr,l,r):
    if l < r:
        limit = partiotion(Arr,l,r)
        quick_sort(Arr,l,limit-1)
        quick_sort(Arr,limit+1,r)


def bucket_sort(Arr): # sortuje pojemniki po X
    n = len(Arr)
    el_min = Arr[0][2]
    el_max = Arr[0][2]
    for el in Arr:
        el_min = min(el_min,el[2])
        el_max = max(el_max,el[2])
    el_max = floor(el_max) + 1 # podbijam do wyższej bo sortowanie kubełkowe defaultowe przedział [a,b)
    buckets = [list() for _ in range(n)]
    for el in Arr:
        index = floor(((el[2]-el_min)/(el_max-el_min))*n)
        buckets[index].append(el)

    i = 0
    for bucket in buckets:
        if len(bucket) > 0:
            quick_sort(bucket,0,len(bucket)-1) # sortuje kubełki
            for el in bucket:
                Arr[i] = el
                i+= 1


# tuple(x1,y1,x2,y2)
def rectangle_area(x1,y1,x2,y2):
    a = x2-x1
    b = y2-y1
    return a*b


def add_water(actual,Y_end):
    x1, y1, x2, y2 = actual[0], actual[1], actual[2], actual[3]
    if y1 >= Y_end: # kubełek aktualny zaczyna się wyżej
        return 0
    if y2 > Y_end: # zakańcza się później 
        y2 = Y_end
    return rectangle_area(x1,y1,x2,y2)
    

def amount_of_water(Arr,index): # Table, index 
    water_sum = 0
    Y_end =Arr[index][3]
    for i in range(len(Arr)): # albo kubełek się zaczyna poniżej, albo w trakcie albo powyżej
         water_sum += add_water(Arr[i], Y_end)
    return water_sum


def water_buckets(Arr, water=15000):
    for i in range(len(Arr)):
        Arr[i] = (min(Arr[i][0], Arr[i][2]),min(Arr[i][1], Arr[i][3]), max(Arr[i][0],Arr[i][2]), max(Arr[i][1], Arr[i][3]))
    bucket_sort(Arr) # sortuje po wartości X rosnąco wszystkie pojemniki
    print(Arr)
    return binary_water_search(Arr,0,len(Arr)-1, water)


def binary_water_search(Arr,l,r,water):
    if l > r :
        return False
    half = ((r-l)//2)+l
    if half >= len(Arr) or half <0:
        return False
    water_sum = amount_of_water(Arr,half)
    if water_sum > water:
        return binary_water_search(Arr,l,half-1,water)
    if water_sum <= water:
        if half == len(Arr)-1: # bo defaultowo nie rozpatruje ostatniego pojemnika
            last_bucket_area = rectangle_area(*Arr[half])
            if water_sum + last_bucket_area <= water: 
                return half+1
            return half
        tmp = binary_water_search(Arr,half+1,r,water)
        if tmp is not False:
            return tmp
        else:
            return max(half,tmp)


print(water_buckets(Arr,7000))
