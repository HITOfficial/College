# Given is the table This called numerical edition. In the indicated position, you can jump to position b
# if the number T [a] and T [b] have one digit operator. The cost of such a jump is equal to ∣T [a] -T [b] ∣.
# Please write a function that determines the total cost of exit document that you have access to the T table value - 1.

# complexity:
# - time O(L*N^2) -> Dijkstra on list adjacency -> ElogN, but constructing graph takes L*N^2, where L is number of digits in number
# - space O(E) -> data to construct graph

from queue import PriorityQueue


def digit_marking(number):
    A = [False]*10
    while number > 0:
        A[number % 10] = True
        number //= 10
    return A


def common_digit(A, B):
    for i in range(10):
        if A[i] == B[i] == True:
            return True
    return False


def jump_cost(A, B, a, b):
    if common_digit(A, B):
        return abs(a-b)
    else:
        # distance equal infinity if numbers have not at least one common digit
        return float("inf")


def construct_graph(T, n):
    digits = [digit_marking(T[i]) for i in range(n)]
    # creating list adjacency with connections between numbers
    graph = [list() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist = jump_cost(digits[i], digits[j], T[i], T[j])
                # has connection
                if dist != float("inf"):
                    graph[i].append((j, dist))
    return graph


def Dijkstra_distance(graph, n, b, e):
    distances = [float("inf")]*n
    distances[b] = 0
    p_queue = PriorityQueue()
    # adding all edges outgoing from beggining vertex
    for v, w in graph[b]:
        # tuple values: edge weight, vertex from, vertex to
        p_queue.put((w, b, v))
    while not p_queue.empty():
        w, u, v = p_queue.get()
        if distances[v] > distances[u] + w:
            distances[v] = distances[u] + w
            for k, d in graph[v]:
                p_queue.put((d, v, k))
    if distances[e] == float("inf"):
        # cannot find connection to edging vertex
        return -1
    else:
        return distances[e]


def find_cost(T):
    n = len(T)
    graph = construct_graph(T, n)
    b, e = min(enumerate(T), key=lambda x: x[1])[0], max(
        enumerate(T), key=lambda x: x[1])[0]
    return Dijkstra_distance(graph, n, b, e)


T = [123, 890, 688, 587, 257, 246]

print(find_cost(T))
