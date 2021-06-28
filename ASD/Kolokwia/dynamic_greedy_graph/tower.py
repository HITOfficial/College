# highest tower can be built with the blocks

# complexity:
# time O(N^2)
# memory O(N)


def tower(array):
    n = len(array)
    size = [1]*n
    for i in range(1,n):
        i1, i2 = array[i]
        for j in range(i):
            j1, j2 = array[j]
            if j1 <= i1 and j2 >= i2:
                size[i] = max(size[i],size[j]+1)
    return max(size)


A1 = [(1,4),(0,5),(1,5),(2,6),(1,2),(2,4)]
A2 = [(10,15),(8,14),(1,6),(3,10),(8,11),(6,15)]

print(tower(A1))
print(tower(A2))