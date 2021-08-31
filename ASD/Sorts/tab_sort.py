from math import floor
# double bucket sort

# complexity:
# - time O(N)
# - space O(N)


# simple bubble sort sort
def bubblesort(T):
    for i in range(len(T)-1):
        for j in range(i+1, len(T)):
            if T[i] > T[j]:
                T[i], T[j] = T[j], T[i]
    return T


def bucket_sort(A, l, r):
    n = len(A)
    buckets = [list() for _ in range(n)]
    for val in A:
        idx = floor(((val-l)/(r-l))*n)
        buckets[idx].append(val)
    # sorting every bucket
    for i in range(n):
        buckets[i] = bubblesort(buckets[i])
    T = []
    for bucket in buckets:
        for val in bucket:
            T.append(val)
    return T


def sort_tab(T, P):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    k = len(P)
    buckets = [list() for _ in range(k)]
    for val in T:
        # bucket range
        for i in range(k):
            l, r, _ = P[i]
            if val > l and val < r:
                # adding elements into right bucket
                buckets[i].append(val)
                break
    # now all elements are in correctly bucket
    for i in range(k):
        l, r, _ = P[i]
        buckets[i] = bucket_sort(buckets[i], l, r)
    # all elements are sorted in correctly buckets
    new_bucket = []
    for bucket in buckets:
        new_bucket.extend(bucket)
    l = min([x for x, _, _ in P])
    r = max([x for _, x, _ in P])
    return bucket_sort(new_bucket, l, r)


T1 = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
P1 = [(1, 5, 0.75), (4, 8, 0.25)]

T3 = [5.2, 2.7, 6.6, 3.9, 1.4, 4.8, 6.3, 7.0, 6.4, 1.1, 7.4, 5.4,
      5.1, 4.3, 6.7, 7.2, 5.6, 7.7, 6.9, 1.6, 2.7, 4.1, 4.3, 6.5]
P3 = [(1, 4, 0.25), (4, 7, 0.5), (6, 8, 0.25)]

print(sort_tab(T1, P1))
print(sort_tab(T3, P3))
