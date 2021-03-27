# lowest index of value in Table
def binary_search(T, b=0, e=None, val=None): # table, begin, end, value to search
    if e == None:
        e = len(T)-1
    if b > e:
        return None
    half = (e+b)//2
    if T[half] == val:
        ret = binary_search(T, b, half-1, val)
        if ret == None:
            return half
    if T[half] > val:
        return binary_search(T,b, half-1, val)
    else:
        return binary_search(T,half+1, e, val)



def binary_search(Arr,k,l,r):
    half = l+(r-l+1)//2
    if Arr[l] > k or Arr[r] <k or r == -1: # zeby nie wyskoczyć poza zakres
        return False
    if Arr[half] == k:
        lowest = binary_search(Arr,k,l,half-1)
        if lowest is not False:
            return lowest
        else:
            return half
    if Arr[half] > k: # idę w lewo
        return binary_search(Arr,k,l,half-1)
    else: # idę w prawo
        return binary_search(Arr,k,half+1,r)