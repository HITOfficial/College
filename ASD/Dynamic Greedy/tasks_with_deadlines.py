# We have a given set of tasks T = {t1 ,. . . , tn}. Each task ti
# additionally includes: (a) date of execution d (ti) (natural number) and (b) profit g (ti) for timely execution
# (Natural number). Each task takes a unit of time. If ti has finished
# before exceeding the d (ti) deadline you get g (ti) (first selected task)
# is executed at 0 o'clock, second selected job at 1 o'clock, third job at 2 o'clock, etc.).
# Provide an algorithm that finds a subset of tasks that can be performed in a timely manner and that runs
# for maximum profit. Please justify the correctness of the algorithm.

from heapq import heappop, heappush

# complexity:
# - time O(D*NlogK), where D is last deadline N number of elements, K elements in correctly heap


def tasks_with_deadlines(T):
    n = len(T)
    array = list((t[0], t[1], idx) for idx, t in enumerate(T))
    last_deadline = max([deadline for deadline, _ in T])
    allready_used = [False]*n
    buckets = [list() for _ in range(last_deadline+1)]
    # adding all
    for deadline, value, idx in array:
        # pushing into heaps negative value, to use min heap structure
        for i in range(deadline, last_deadline+1):
            heappush(buckets[i], (-value, idx))
    total_profit = 0
    used_indexes = []
    for deadline in range(last_deadline+1):
        while len(buckets[deadline]) > 0:
            val, idx = heappop(buckets[deadline])
            if allready_used[idx] is False:
                allready_used[idx] = True
                used_indexes.append(idx)
                total_profit -= val
                break
    return total_profit, used_indexes


T = [(0, 3), (0, 2), (1, 1), (1, 1), (1, 1),
     (2, 4), (3, 1), (4, 6), (4, 9), (2, 12)]


print(tasks_with_deadlines(T))
