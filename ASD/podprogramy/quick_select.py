# partition
# Qucik select


def partition(Arr,l,r):
    pivot = Arr[l]
    limit = r+1
    for i in range(r,l,-1):
        if Arr[i] > pivot:
            limit -= 1
            Arr[limit], Arr[i] = Arr[i], Arr[limit]
    limit -= 1
    Arr[l], Arr[limit] = Arr[limit], Arr[l]
    return limit


def quick_select(Arr,l,r,k):
    limit =  partition(Arr,l,r)
    if limit == k:
        return Arr[limit]
    elif limit < k:
        return quick_select(Arr,limit+1,r,k)
    else:
        return quick_select(Arr,l,limit-1,k)


Arr = [1,2,3,5,2,1,3,7,6]
k = 2
print(quick_select(Arr,0,len(Arr)-1,len(Arr)-k-1)) # od końca K-ty element
print(quick_select(Arr,0,len(Arr)-1,k)) # od początku K-ty element