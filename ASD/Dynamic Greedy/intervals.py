# A list of I closed intervals is given [a1, b1], [a2, b2],. . . , [an, bn]. Break function intervals (
# I), which computes for each i ∈ {1, 2,. . . , n} length of the longest interval that
# one of the selected periods selected from among the selected ones. Function
# she should be ours as soon as possible.
# The intervals are represented as pairs. The function is the appropriate list of numbers in which the request is confirmed
# element to the length of the longest interval that is searched for, built of the prime and elements
# implementation. For example, for episode lists:

# complexity:
# - time O(K*N^2) creating previously element connections N^2, finding longest connection O(N)
# - space O(N)

def intervals(A):
    n = len(A)
    A = [(tpl[1][0], tpl[1][1], tpl[0])for tpl in enumerate(A)]
    # sorting array by begginings
    A.sort()
    prev = [None]*n
    for i in range(n):
        a, b, _ = A[i]
        for j in range(i-1, -1, -1):
            c, d, _ = A[j]
            # finding first closest interval to beggining (can stink with him in one point or can be inside a bit)
            if a <= d:
                prev[i] = j
                break
    # dynamic data array
    DD = [0]*n
    for i in range(n):
        if prev[i] is not None:
            # without connecting point becouse he will be added twice
            DD[i] = max(DD[prev[i]] + A[i][1]-A[i][0] - 1, A[i][1]-A[i][0]+1)
        else:
            DD[i] = A[i][1]-A[i][0]+1
    return max(DD)


def intervals_queries(A, queries):
    ans = []
    for a, b in queries:
        ans.append(intervals(A[a:b+1]))
    return ans


A = [(1, 3), (5, 6), (4, 7), (6, 9)]
queries = [(0, 1), (0, 2), (2, 3), (0, 3)]

print(intervals_queries(A, queries))
