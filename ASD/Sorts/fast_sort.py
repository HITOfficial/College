# The giver of time gave real number in particulars x,
# where is a certain number constant from 1 (a> 1) and notes that the value of x on a [0, 1].
# Write a fast sort function that takes an array of numbers from the search results, and determines a and
# arrays with the results of the experiment sorted in ascending order. The function should work as it works.

# complexity:
# - time O(N)
# - space O(N)

# using buckets to sort every elements
from math import log


def fast_sort(tab, a):
    n = len(tab)
    buckets = [list() for _ in range(n+1)]
    for value in tab:
        # value which was before a**x
        log_value = log(value, a)
        index = int((log_value-1)*n)
        buckets[index].append(log_value)
    for i in range(n):
        buckets[i].sort()
    result_tab = []
    for bucket in buckets:
        for el in bucket:
            result_tab.append(round(el, 3))
    return result_tab


T1 = [0.1, 0.5, 0.2, 0.78, 0.01]
D1 = [2**x for x in T1]
T1.sort()
print(T1)
print(fast_sort(D1, 2))
