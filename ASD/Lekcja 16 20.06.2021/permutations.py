# inspiring with wikipedia/geeks alg.
# complexity:
# -time O(N!)
# -memory O(N!)


def permutation(permutations_array,array,k):
    if k == 1:
        permutations_array.append(array.copy())
    else:
        for i in range(k):
            permutation(permutations_array,array,k-1)
            # k is even
            if k%2 == 0:
                array[i], array[k-1] = array[k-1], array[i]
            else:
                array[0], array[k-1] = array[k-1], array[0]


def permutations(array):
    permutations_array = []
    permutation(permutations_array,array,len(array))
    # returning all permutations
    return permutations_array

print(permutations([1,2,3]))
