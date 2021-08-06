# Merge Sort algorithm with extra O(n) space

# complexity:
# - time O(nlogn)
# - space O(n)

# creating only once extra array and using on every level of recurse


def merge(array, extra_array, n, l, m, r):
    i = l
    j = m+1
    k = l
    while(i <= m and j <= r):
        if extra_array[i] <= extra_array[j]:
            array[k] = extra_array[i]
            i += 1
        else:
            array[k] = extra_array[j]
            j += 1
        k += 1

    while i <= m:
        array[k] = extra_array[i]
        i += 1
        k += 1
    while j <= r:
        array[k] = extra_array[j]
        j += 1
        k += 1
    # copied all replaced elements, to extra array
    for i in range(l, r+1):
        extra_array[i] = array[i]


def merge_rec(array, extra_array, n, l, r):
    if l < r:
        m = (l+r)//2
        merge_rec(array, extra_array, n, l, m)
        merge_rec(array, extra_array, n, m+1, r)
        merge(array, extra_array, n, l, m, r)


def merge_sort(array):
    n = len(array)
    l = 0
    r = n-1
    extra_array = array.copy()
    merge_rec(array, extra_array, n, l, r)
    return array


a = [1, 0, 2, 5, 6, 87, 0, 3, 3465, 0, 3, 2, 4, 6, 2, 7, 8, 0, 34, 53, 4]
print(merge_sort(a))
