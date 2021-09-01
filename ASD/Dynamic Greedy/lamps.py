# - 0 -> green, 1 -> red, 2 -> blue

# complexity:
# - obliczeniowa O(Q*P) / Jest to równoważne z O(N+T) z polecenia( ponieważ T jest równe łącznej ilości wciśnieć przycisków), gdzie Q jest ilością przedziałów w L, P rozmiarem przedziałów
# - pamięciowa O(N), pomocnicza tablica z zapamiętywaniem aktualnego koloru lampki


def change_color(A, idx):
    # changing from green on red
    if A[idx] == 0:
        A[idx] = 1
        return 0
    # red -> blue
    elif A[idx] == 1:
        A[idx] = 2
        # actual sub sum incrementing by one
        return 1
    # blue -> green
    else:
        A[idx] = 0
        # changing blue light
        return -1


def lamps(n, L):
    A = [0]*n
    # max sum of actual turned on light, acutal sequence of turned on blue lights
    max_sum = 0
    actual_sum = 0
    for a, b in L:
        if actual_sum < 0:
            actual_sum = 0
        for idx in range(a, b+1):
            actual_sum += change_color(A, idx)
        # checking if actual is more turned on blue lights
        if actual_sum > max_sum:
            max_sum = actual_sum
    return max_sum


n = 10
L = [(7, 8), (2, 5), (2, 5), (6, 8), (5, 8),
     (9, 9), (7, 7), (1, 3), (9, 9), (7, 9)]

print(lamps(n, L))
