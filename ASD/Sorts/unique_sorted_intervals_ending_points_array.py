# alg. converting intervals into unique ending points

# complexity:
# - time O(N) / O(H-L), where H is the highest number in range array, and L lowest
# space O(H-L)


def unique_array(array):
    min_el, max_el = float("inf"), -float("inf")
    for b, e in array:
        if b < min_el:
            min_el = b
        if e > max_el:
            max_el = e
    range_array = [False]*(max_el-min_el+2)
    for b, e in array:
        range_array[b-min_el] = True
        range_array[e-min_el] = True
    unique = []
    for val in range(max_el-min_el+2):
        if range_array[val]:
            unique.append(val+min_el)
    return unique


array1 = [(3, 10), (5, 20), (7, 12), (10, 15)]
array2 = [(15, 20), (5, 20), (17, 19), (12, 15), (30, 40)]

print(unique_array(array1))
print(unique_array(array2))
