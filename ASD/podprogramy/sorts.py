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


def quick_sort_half(t,start=0,end=None): # pivot w połowie
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




def quick_sort(T,begin=0, end=None):
    def hindus_quick_sort(T, begin, end): # lewym szukam wiekszych, prawym mniejszych
        pivot = T[begin]
        left = begin+1
        right = end
        while left < right:
            while T[left] <= pivot and left < end: # szukam większych dodatkowe ograniczenie zeby nie wyskoczyc poza liste
                left += 1
            while T[right] > pivot: # szukam mniejszych
                right -= 1
            if left < right:
                T[left], T[right] = T[right], T[left]
        T[begin], T[right] = T[right], T[begin]
        return right
        

    if end is None:
        end = len(T)-1
    if begin < end: # pozostał 1 element do sprawdzenia
        part = hindus_quick_sort(T, begin, end)        
        quick_sort(T, begin, part-1)        
        quick_sort(T, part+1, end)
    return T        


from random import randint, seed
from time import time
seed(40)




def revers_list(t):
    i = 0
    while i < len(t)//2:
        t[i], t[len(t)-1-i] = t[len(t)-1-i], t[i]
        i+=1 
    return t

def merge(T,l,m,r):
    L = [T[i] for i in range(l,m+1)]
    R = [T[i] for i in range(m+1,r+1)]
    i = j = 0
    k = l
    while(i <= m-l and j <= r-m-1): # robię m-l ponieważ w indexach w tymczasowych tablicach zaczynam od indexu 0 
        if L[i] <= R[j]:
            T[k] = L[i]
            i+=1
        else:
            T[k] = R[j]
            j+=1
        k+=1
    while i <= m-l: # dopełniam elementami pozostałymi z i
        T[k] = L[i]
        i+=1
        k+=1
    while j <= r-m-1: # dopełniam elementami pozostałymi w j
        T[k] = R[j]
        j+=1
        k+=1


def mergesort(T,l=0,r=None):
    if r is None:
        r = len(T)-1
    if l < r:
        m = (l+r)//2 # element środkowy
        mergesort(T, l, m)
        mergesort(T,m+1, r)
        merge(T,l,m,r)

def count_sort(T): # działa mega szybko na mały range liczb
    max_el = min_el = 0
    for el in T:
        max_el = max(max_el, el) # najwiekszy element
        min_el = min(min_el, el) # najwiekszy element

    count_T = [0] * (max_el-min_el+1) # max()-min() +1 bo wlacznie z 0
    for el in T:
        count_T[el-min_el] += 1 # uwzglednienie liczb ujemnych
    for j in range(1, len(count_T)): 
        count_T[j] += count_T[j-1] # sumuje z wartoscia pod poprzednim
    sort_T = [None] * len(T) # posortowana tablica
    min_el_negation = min_el*-1
    for i in range(0,len(T)):
        sort_T[count_T[T[i] + min_el_negation]-1] = T[i] # indexy w tablicy od 0 dlatego -1
        count_T[T[i] + min_el_negation] -= 1

    return sort_T


def quicksort(T):
    def quick_sort(T,l=0,r=None): # table, range to sort: left, right
        while l<r:
            limit = partition(T,l,r)
            quick_sort(T,l,limit-1)
            l=limit+1

    def partition(T,i,r):
            pivot = T[r]
            limit = i-1 # granica 
            for j in range(i,r): # szuka do elementu przed pivotem
                if T[j] <= pivot:
                    limit +=1 
                    T[limit], T[j] = T[j], T[limit]
            T[limit+1], T[r] = T[r], T[limit+1]
            return limit+1
    quick_sort(T,0,len(T)-1)
    return T


def heapsort(T):
    def max_heap(T,n,i): # table, len(T), index rodzica
        left = 2*i +1
        right = 2*i +2
        i_copy = i
        if left < n and T[left] > T[i]: i_copy = left
        if right < n and T[right] > T[i_copy]: i_copy = right
        if i != i_copy: # znalezione dziecko z wartoscia wieksza
            T[i], T[i_copy] = T[i_copy], T[i]
            max_heap(T,n, i_copy) # szuka poddzieci do dzieci

    n = len(T)
    def build_heap(T,n):
        for i in range(((n//2)-1),-1,-1): # budowa kopca
            max_heap(T,n,i)
            
    build_heap(T,n)
    for i in range(n-1,0,-1):
        T[0], T[i] = T[i], T[0] # podmieniam aktualnie znaleziony najwiekszy z kolejnymi elementami od konca z tablicy
        max_heap(T,i,0)
    return T



T = [randint(-10000,10000) for i in range(1000000)]
s1 = time()
quick_sort(T)
e1 = time() - s1
print("Hindus quicksort: ",e1)
T = [randint(-10000,10000) for i in range(1000000)]
s2 = time()
quick_sort_half(T)
e2 = time() - s2
print("G quicksort: ",e2)
T = [randint(-10000,10000) for i in range(1000000)]
s3 = time()
comb_sort(T)
e3 = time() - s3
print("Combsort: ",e3)
T = [randint(-10000,10000) for i in range(1000000)]
s4 = time()
mergesort(T)
e4 = time() - s4
print("Merge: ",e4)
T = [randint(-10000,10000) for i in range(1000000)]
s5 = time()
count_sort(T)
e5 = time() - s5
print("count: ",e5)
T = [randint(-10000,10000) for i in range(1000000)]
s6 = time()
quicksort(T)
e6 = time() - s6
print("quicksort last_p: ",e6)
T = [randint(-10000,10000) for i in range(1000000)]
s7 = time()
heapsort(T)
e7 = time() - s7
print("heapsort: ",e7)








    
    
    