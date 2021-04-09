from random import randint


def binary_index(Arr,l,r,k,last=None): # zwracam el większy
    if l>r:
        return last
    half = (l+r)//2 # el po środku
    if Arr[half] < k:
        return binary_index(Arr,half+1,r,k,last)
    else:
        return binary_index(Arr,l,half-1,k,half)


def LIS(Arr):
    n = len(Arr)
    A = [None] * n
    if len(Arr) == 0:
        return 0
    A[0] = Arr[0] # wrzucam defaultowo 1wszy element do listy
    l = 1; # index ostatniego elementu w aktualnym podciągu rosnącym
    for i in range(1,n):
        k = Arr[i]
        if k < A[0]: # będzie szukało nowego podciągu do utworzenia
            A[0] = k
        elif k > A[l-1]:
            A[l] = k # dopinam nowy element
            l += 1
        else: # dorzucam pomiędzy nowy element
            A[binary_index(A,0,l-1,k)] = k
    return l


A = [randint(1,800) for _ in range(5000)]
print(LIS(A))




