# complexity:
# - time O(NlogN)
# - space O(N)


def binary_intervals(I, n, visited, in_intervals, actual_intervals, l, r, pivot, y):
    # full interval
    if l <= r:
        m = (r+l)//2
        # full interval, or interval form m has full connections to Y
        if pivot == y or in_intervals[m]:
            for idx in actual_intervals:
                in_intervals[idx] = True
            return
        # found connections
        if I[m][0] == pivot:
            if visited[m] is False:
                visited[m] = True
                binary_intervals(I, n, visited, in_intervals,
                                 actual_intervals[:]+[m], min(m+1, n-1), n-1, I[m][1], y)
            # left side elements equal to pivot
            binary_intervals(I, n, visited, in_intervals,
                             actual_intervals, l, m-1, pivot, y)
            # right side elements equal to pivot
            binary_intervals(I, n, visited, in_intervals,
                             actual_intervals, m+1, r, pivot, y)
        # searching in left side in binary search
        elif I[m][0] > pivot:
            binary_intervals(I, n, visited, in_intervals,
                             actual_intervals, l, m-1, pivot, y)
        else:
            binary_intervals(I, n, visited, in_intervals,
                             actual_intervals, m+1, r, pivot, y)


def instuse(I, x, y):
    n = len(I)
    I = [(*tpl, idx) for tpl, idx in zip(I, range(n))]
    I.sort()
    visited = [False]*n
    in_intervals = [False]*n
    binary_intervals(I, n, visited, in_intervals, [], 0, n-1, x, y)
    intervals_indexes = []
    for i in range(n):
        if in_intervals[i]:
            intervals_indexes.append(I[i][2])
    return intervals_indexes


I = [(3, 4), (2, 5), (1, 3), (4, 6), (1, 4)]
x, y = 1, 6

print(instuse(I, x, y))
