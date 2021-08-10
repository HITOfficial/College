
# dynamic algorithm
# complexity:
# - time O(D*N), where D is a difference between min and max value in data
# - space (D)

# algorithm calculate maximum size of tower, which can be build, using blocks- works on integers


def falling_blocks(array):
    n = len(array)
    min_val, max_val = float("inf"), -float("inf")
    for b, e, h in array:
        min_val, max_val = min(min_val, b), max(max_val, e)
    D = [0]*(max_val-min_val+2)
    for index in range(n):
        b, e, h = array[index]
        # finding highest element inside range
        highest = 0
        for d in range(b-min_val, e+1-min_val):
            highest = max(highest, D[d])
        for d in range(b-min_val, e+1-min_val):
            D[d] = highest + h
    return max(D)


array = [(-8, 1, 3), (1, 3, 1), (2, 5, 2), (0, 3, 2), (8, 9, 3), (4, 6, 1)]

print(falling_blocks(array))
