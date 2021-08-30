# The investor plans to build a new student housing estate. The architects presented building designs from which the investor has to select a subset meeting his expectations. Every building
# it is represented as a rectangle with a certain height h, based on point a to point b,
# and the construction price w (where h, a, b and w are natural numbers, where a <b). In a building like this there may be h ⋅ (b - a) students.
# Please implement the function: def select_buildings (T, p): which takes:
# • Table T with descriptions of n buildings. Each description is a tuple of the form (h, a, b, w), consistent
# with the markings introduced above.
# • A natural number p defining the limit of the total price of building buildings.
# The function should return an array with building numbers (according to the sequence in T, numbered
# from 0) that do not overlap, cost less than p in total and hold the maximum number
# students. If more than one set of buildings meet the conditions of the task, the feature should return
# the set with the lowest total cost of construction. Two buildings do not overlap if they do not have one common point.
# It can be assumed that there is always a solution that includes at least one building. Function
# it should be as fast as possible and use as few wrinkles as possible. It should be made very briefly
# justify its correctness and estimate the computational complexity.

# complexity:
# - time O(N*P)
# - space O(N*P)

# F(x), first building, ending before x block
def get_path(A, T, cost, prev, i, w):
    p = []
    if i == 0 and w >= cost[i]:
        p.append(T[i][4])
        return p
    elif i >= 1:
        if A[i][w] > A[i-1][w]:
            p.append(T[i][4])
            # actual element has previolsy element in path
            if prev[i] is not None:
                p.extend(get_path(A, T, cost, prev, prev[i], w-cost[i]))
        else:
            p.extend(get_path(A, T, cost, prev, i-1, w))
    return p


def select_buildings(T, p):
    n = len(T)
    # sorting array by endings
    T = sorted([(*tpl, idx) for idx, tpl in enumerate(T)], key=lambda x: x[2])
    # Dynamic array to get best value
    A = [[0]*(p+1) for _ in range(n)]
    # using only first item
    cost = [0]*n
    size = [0]*n
    prev = [None]*n
    for i in range(n):
        size[i] = T[i][0]*(T[i][2]-T[i][1])
        cost[i] = T[i][3]
        # finding first element which starting closest, actual ending
        for j in range(i-1, -1, -1):
            if T[i][1] > T[j][2]:
                prev[i] = j
                break
    # updating data using only first element
    for w in range(T[0][3], p+1):
        A[0][w] = size[0]
    for i in range(1, n):
        for w in range(p+1):
            A[i][w] = A[i-1][w]
            if cost[i] <= w and prev[i] is not None:
                A[i][w] = max(A[i-1][w], size[i] + A[prev[i]][w-cost[i]])
            # actual block hasn't previously element in row
            else:
                A[i][w] = max(A[i-1][w], size[i])
    s, idx = 0, 0
    for i in range(p+1):
        if s < A[-1][i]:
            s = A[-1][i]
            idx = i
    return list(sorted(get_path(A, T, cost, prev, n-1, idx)))


P1 = ([(7, 23, 24, 1), (2, 10, 14, 3), (7, 17, 22, 1),
       (9, 20, 22, 2), (4, 19, 22, 8), (2, 2, 6, 1)], 10)
P2 = ([(2, 1, 5, 3), (3, 7, 9, 2), (2, 8, 11, 1)], 6)

print(select_buildings(P1[0], P1[1]))
print(select_buildings(P2[0], P2[1]))
