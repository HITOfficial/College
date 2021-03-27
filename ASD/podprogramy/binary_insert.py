Arr = [1,2,3,4,6]


def binary_insert(Arr,k):
    x = smallest_or_equal(Arr,0,len(Arr),k)+1
    Arr.append(None)
    for i in range(len(Arr)-1,x,-1):
        Arr[i] = Arr[i-1]
    Arr[x] = k
    return Arr


def smallest_or_equal(Arr,l,r,k,last=None): # idex ostatniego elementu mniejszego lub równego
    if l > r:
        if last is not None:
            return last
        else:
            return -1
    half = (r+l)//2 # element środkowy
    if Arr[half] <= k:
        return smallest_or_equal(Arr,half+1,r,k,half)
    else:
        return smallest_or_equal(Arr,l,half-1,k,last)


print(binary_insert(Arr,5))
