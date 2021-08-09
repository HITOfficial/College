# greedy method:
# need to push allways first block of dominoes
# I assume also that pushing block whos end has value X, will also push every blocks with start of X

# complexity:
# - time O(nlogn) -> sorting values O(nlogn), n times binary_search
# - space O(logn) -> stack size in recursion


class Time():
    def __init__(self, time=0):
        self.time = time


def binary_find_connections(array, n, used, time, l, r, pivot):
    if r >= l and time.time <= n:
        # middle index
        m = (l+r)//2
        # found element
        if array[m][0] == pivot:
            # wasnt used block
            if used[m] is False:
                used[m] = True
                # memorizing used dominos to statement in O(1)
                time.time += 1
                # finding connections to new pivot
                binary_find_connections(
                    array, n, used, time, m, n-1, array[m][1])
            # binary select to find the same elements in left and right side
            binary_find_connections(array, n, used, time, l, m-1, pivot)
            binary_find_connections(array, n, used, time, m+1, r, pivot)
        # left side of  array
        elif array[m][0] > 0:
            binary_find_connections(array, n, used, time, l, m-1, pivot)
        # middle element value is to low
        else:
            binary_find_connections(array, n, used, time, m+1, r, pivot)


def dominos(A):
    n = len(A)
    # sorting by first value in tuple
    # array = sorted([(i, t[0], t[1]) for i, t in enumerate(A)])
    # default sort in tuple by first element
    array = sorted(A)
    # marking up all used dominos
    used = [False]*n
    # extra variable of times, to reduce findding in some cases of algorithm (if one block will be enought, to push all other blocks), to do not continue while loop N-1 times
    time = Time()
    # extra variable to count lowest number of dominos to push
    counter, index = 0, 0
    dominos_to_push = []
    # while are elements in array
    while time.time <= n and index < n:
        if used[index] is False:
            used[index] = True
            # pushing new domino block
            counter += 1
            time.time += 1
            b, e = array[index]
            dominos_to_push.append((b, e))
            binary_find_connections(array, n, used, time, index+1, n-1, e)
        index += 1
    return counter, dominos_to_push


array = [(1, 2), (1, 3), (3, 4), (3, 7), (5, 9), (10, 11), (4, 5)]

print(dominos(array))
