def selection_sort(t):
    for i in range(len(t)-1):
        lowest_index = i
        for j in range(i+1,len(t)):
            if t[lowest_index] > t[j]:
                lowest_index = j
        t[i], t[lowest_index] = t[lowest_index], t[i] 
    return t


def bubble_sort(t):
    for i in range(len(t)):
        for j in range(1,len(t)):
            if t[j] < t[j-1]:
                t[j], t[j-1] = t[j-1], t[j]
    return t


def comb_sort(t):
    swap = True
    distance = len(t)
    while (distance>1 or swap == True):
        distance = max(int(distance/1.3), 1)
        top = len(t)-distance
        swap = False
        for i in range(0,top):
            j = i+distance
            if t[i] > t[j]:
                t[i], t[j] = t[j], t[i]
                swap = True
    return t


def quick_sort_half(t,start=0,end=None):
    if end is None:
        end = len(t)-1 
    left = start
    right = end
    half_element = t[(start+end)//2]
    while left <= right:
        while t[left] < half_element:
            left += 1
        while t[right] > half_element:
            right -= 1
        if left <= right:
            t[left], t[right] = t[right], t[left]
            left +=1
            right -=1
    if start < right:
        quick_sort_half(t, start, right)
    if end > left:
        quick_sort_half(t, left, end)    
    return t


def hindus_quick_sort(T, begin, end): # lewym szukam wiekszych, prawym mniejszych
    pivot = T[begin]
    left = begin+1
    right = end
    while left < right:
        while T[left] <= pivot: # szukam większych
             left += 1
        while T[right] > pivot: # szukam mniejszych
             right -= 1
        if left < right:
            T[left], T[right] = T[right], T[left]
    T[begin], T[right] = T[right], T[begin]
    return right

def quick_sort(T,begin=0, end=None):
    if end is None:
        end = len(T)-1
    if begin < end: # pozostał 1 element do sprawdzenia
        part = hindus_quick_sort(T, begin, end)        
        quick_sort(T, begin, part-1)        
        quick_sort(T, part+1, end)
    return T        

T = [7,8,10,5,9,2,1,15,7]

print(quick_sort(T))



def revers_list(t):
    i = 0
    while i < len(t)//2:
        t[i], t[len(t)-1-i] = t[len(t)-1-i], t[i]
        i+=1 
    return t

