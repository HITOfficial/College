# Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy każda liczba z tablicy
# jest sumą dwóch innych liczb z tablicy. Zaproponowany
# algorytm powinien być możliwie jak najszybszy. Proszę oszacować jego złożoność obliczeniową

Arr = [2,1,3,0,-1,0,0,1,5] # posortuje pierwsze

def partition(Arr,l,r):
    pivot = Arr[r]
    limit = l-1
    for i in range(l,r):
        if pivot > Arr[i]:
            limit += 1
            Arr[limit], Arr[i] = Arr[i], Arr[limit]
    limit += 1 
    Arr[limit], Arr[r] = Arr[r], Arr[limit]
    return limit


def quick_sort(Arr,l,r):
    if l < r:
        limit = partition(Arr,l,r)
        quick_sort(Arr,l,limit-1)
        quick_sort(Arr,limit+1,r)


quick_sort(Arr,0,len(Arr)-1)
print(Arr)


def el_as_sum_others(Arr):
    n = len(Arr)
    k = i = 0
    j = n-1
    quick_sort(Arr,0,n-1) # posortuje tablice
    while k < n:
        if i == j: # wskazniki się skrzyżują nie jest sumą 2 innych el
            return False
        if k == j: # prawy
            j -= 1
        if k == i: # lewy
            i += 1
        
        el_to_find = Arr[k]
        a_sum = Arr[i]+Arr[j]
        if a_sum == el_to_find:
            k += 1
            i = 0
            j = n-1
        elif el_to_find < a_sum:
            j -= 1
        else:
            i += 1
    return True
    
print(el_as_sum_others(Arr))