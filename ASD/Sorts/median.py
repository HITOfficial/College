# complexity:
# - time O(N^2logN) -> N^2log(N^2) -> worst case of parition
# - space O(N^2) creating extra array parition elements

def partition(Arr, l, r):
    pivot = Arr[l]
    limit = r+1
    for i in range(r, l, -1):
        if Arr[i] > pivot:
            limit -= 1
            Arr[limit], Arr[i] = Arr[i], Arr[limit]
    limit -= 1
    Arr[l], Arr[limit] = Arr[limit], Arr[l]
    return limit


def quick_select(Arr, l, r, k):
    limit = partition(Arr, l, r)
    if limit == k:
        return Arr[limit]
    elif limit < k:
        return quick_select(Arr, limit+1, r, k)
    else:
        return quick_select(Arr, l, limit-1, k)


def median(A):
    n = len(A)
    Arr = [A[i][j] for i in range(n) for j in range(n)]
    n = (n**2)
    l, r = 0, n-1
    k = n//2
    mid_el = quick_select(Arr, l, r, k)
    # partionion by middle element
    while l <= r:
        while Arr[l] < mid_el:
            l += 1
        while Arr[r] > mid_el:
            r -= 1
        if l <= r:
            Arr[l], Arr[r] = Arr[r], Arr[l]
            l += 1
            r -= 1
    idx_r = n-1
    idx_l = 0
    # isering values from parition up to diagonal and down to diagonal
    n = len(A)
    for row in range(n):
        for col in range(n-1, row, -1):
            A[row][col] = Arr[idx_r]
            idx_r -= 1
        if row >= 1:
            for col in range(0, row):
                A[row][col] = Arr[idx_l]
                idx_l += 1

    # inserting values into diagonal
    for i in range(n):
        A[i][i] = Arr[idx_r]
        idx_r -= 1
    return A


A = [
    [43, 74, 53, 97],
    [80, 61, 61, 19],
    [61, 73, 89, 93],
    [42, 17, 89, 80]
]

print(median(A))
