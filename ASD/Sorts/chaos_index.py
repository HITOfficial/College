# complexity:
# -time O(NlogK)
# -memory O(N)


# merge sort alg. with copy of the list
def merge(T,l,m,r):
    L = [T[i] for i in range(l,m+1)]
    R = [T[i] for i in range(m+1,r+1)]
    i = j = 0
    k = l
    while(i <= m-l and j <= r-m-1): 
        if L[i][1] <= R[j][1]:
            T[k] = L[i]
            i+=1
        else:
            T[k] = R[j]
            j+=1
        k+=1
    while i <= m-l:
        T[k] = L[i]
        i+=1
        k+=1
    while j <= r-m-1:
        T[k] = R[j]
        j+=1
        k+=1


def merge_sort(T,l=0,r=None):
    if r is None:
        r = len(T)-1
    if l < r:
        m = (l+r)//2
        merge_sort(T, l, m)
        merge_sort(T,m+1, r)
        merge(T,l,m,r)


def chaos_index(T):
    n = len(T)
    # enumerating list to get tuple (index,value)
    array = list(enumerate(T))
    merge_sort(array,0,n-1)
    k = 0
    for index, element in enumerate(array):
        if abs(index-element[0]) > k:
            k = abs(index-element[0])
    return k


T = [0,2,1.1,2]


print(chaos_index(T))
