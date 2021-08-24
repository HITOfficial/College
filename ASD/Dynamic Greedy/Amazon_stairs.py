# number of ways to get into destination
# using simple knapsack alg. solution

# complexity:
# - time O(N^2)
# - space O(N^2)


def Amazon_stairs(A):
    n = len(A)
    ways = [[0]*n for _ in range(n)]
    # ways using only first item
    for i in range(min(A[0]+1, n)):
        ways[0][i] = 1
    for item in range(1, n):
        for dist in range(n):
            ways[item][dist] = ways[item-1][dist]
            if dist > item and dist <= item + A[item]:
                ways[item][dist] += 1
    return ways[-1][-1]


A = [1, 3, 2, 1, 0]
print(Amazon_stairs(A))
