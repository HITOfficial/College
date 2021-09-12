# complexity:
# - time O(NlogN)
# - space O(E) / O(N)

def DFS_visit(G, visited, u):
    visited[u] = True
    for v in G[u]:
        if visited[v] is False:
            DFS_visit(G, visited, v)


def binary_search(A, l, r, pivot):
    if l <= r:
        m = (l+r)//2
        if A[m] == pivot:
            return m
        # right side
        elif A[m] < pivot:
            return binary_search(A, m+1, r, pivot)
        # left
        else:
            return binary_search(A, l, m-1, pivot)


def intuse(I, x, y):
    n = len(I)
    # taking ony unique values from I values
    B = []
    for i in range(n):
        B.append(I[i][0])
        B.append(I[i][1])
    B.sort()
    A = [B[0]]
    idx = 0
    # list without duplicates
    for i in range(2*n):
        if B[i] == A[idx]:
            continue
        else:
            A.append(B[i])
            idx += 1
    # A has a points without duplicates
    # adding connections
    A_len = len(A)
    graph_b = [[] for _ in range(A_len)]
    graph_e = [[] for _ in range(A_len)]
    if binary_search(A, 0, A_len-1, x) is None or binary_search(A, 0, A_len-1, y) is None:
        return []

    # alg. can make double connections to vertex but this won't increse complexity
    for i in range(n):
        # connections to begginging
        idx_b = binary_search(A, 0, A_len-1, I[i][0])
        # connections to ending
        idx_e = binary_search(A, 0, A_len-1, I[i][1])
        graph_b[idx_b].append(idx_e)
        graph_e[idx_e].append(idx_b)
    # running DFS twice
    b_visited = [False]*A_len
    e_visited = [False]*A_len
    DFS_visit(graph_b, b_visited, binary_search(A, 0, A_len-1, x))
    DFS_visit(graph_e, e_visited, binary_search(A, 0, A_len-1, y))
    solution = []
    for i in range(n):
        idx_b = binary_search(A, 0, A_len-1, I[i][0])
        idx_e = binary_search(A, 0, A_len-1, I[i][1])
        if b_visited[idx_b] and e_visited[idx_e]:
            solution.append(i)

    return solution


I = [(3, 4), (2, 5), (1, 3), (4, 6), (1, 4)]
x, y = 1, 6

print(intuse(I, x, y))
