# complexity:
# -time: O(nlogk) / klogk, but k is much lower than n
# -memory O(1) only single values to remember



# binary search alg, but returning only bool if is element in array
def binary_find(array,element,left,right):
    if right >= left:
        mid = (left+right)//2
        if array[mid] == element:
            return True
        elif array[mid] < element:
            return binary_find(array,element,mid+1,right)
        else:
            return binary_find(array,element,left,mid-1)
    else:
        return False


def longest_incomplete(A,k):
    n = len(A)
    # sorting k array, to check later elements in log(k) time
    k.sort()
    left, right = 0,len(k)-1
    longest, actual = 0, 0
    for i in range(n):
        if not binary_find(k,A[i],left,right):    
            actual += 1
            longest = max(actual,longest)
        else:
            actual = 0
    return longest


k = [10,100,500]
A = [1,100,5,100,1,5,1,5]

print(longest_incomplete(A,k))