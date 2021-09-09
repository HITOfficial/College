# There are N opinions on the number line for M = 10K. You can jump from point A
# on point B w then and only then A% 10K == B // 10K. Please implement the function:
# def sequence (L, K): There are no points so that it is possible to go from the earliest point in this order,
# For all the points, make the last one. A lookup function for a list of position point values ​​on the number line, and be sure to check the point list on your visiting site. li
# Check the availability of points is possible, the function is guaranteed None.
# The feature should be as fast as possible. Please estimate the time and memory complexity algorithm used.


def get_path(path, u):
    p = []
    if u is not None:
        p.append(u)
        p.extend(get_path(path, path[u]))
    return p


def rec_order(L, n, K, visited, parent, u, idx, e_idx, k=0):
    for i, v in enumerate(L):
        # isn't last connection
        if u % 10**K == v//10**K and visited[i] is False:
            # isn't connection to last vertex
            if k < n-2 and e_idx != i:
                visited[i] = True
                parent[i] = idx
                if rec_order(L, n, K, visited, parent, v, i, e_idx, k+1):
                    return True
            # checking if it is connection to last vertex
            elif k == n-2 and e_idx == i:
                parent[i] = idx
                visited[i] = True
                return True
        # taking of parent
            parent[i] = None
            visited[i] = False


def order(L, K):
    n = len(L)
    visited = [False]*n
    parent = [None]*n
    b = L.index(min(L))
    e = L.index(max(L))
    visited[b] = True
    if rec_order(L, n, K, visited, parent, L[b], b, e, 0):
        return [L[i] for i in list(reversed(get_path(parent, e)))]
    else:
        return


# using Hamiltonian path -> constructing graph


def rec_Hamiltonian(graph, n, visited, parent, idx, e, k=0):
    for i in range(n):
        # isn't last connection
        if graph[idx][i] == 1 and visited[i] is False:
            # isn't connection to last vertex
            if k < n-2 and e != i:
                visited[i] = True
                parent[i] = idx
                if rec_Hamiltonian(graph, n, visited, parent, i, e, k+1):
                    return True
            # checking if it is connection to last vertex
            elif k == n-2 and e == i:
                parent[i] = idx
                visited[i] = True
                return True
        # taking of parent
            parent[i] = None
            visited[i] = False


def Hamiltonian_paths(graph, b, e):
    n = len(graph)
    parent, visited = [None]*n, [False]*n
    visited[b] = True
    if rec_Hamiltonian(graph, n, visited, parent, b, e, 0):
        return list(reversed(get_path(parent, e)))
    else:
        return []


def F(A, B, K):
    if A % 10**K == B//10**K:
        return 1
    else:
        return 0


def construct_graph(L, n, K):
    return [[0 if i == j else F(L[i], L[j], K) for j in range(n)] for i in range(n)]


def order_Hamiltonian(L, K):
    n = len(L)
    graph = construct_graph(L, n, K)
    # lowest number in array
    b = min(enumerate(L), key=lambda x: x[1])[0]
    # highest number in array
    e = max(enumerate(L), key=lambda x: x[1])[0]
    path = Hamiltonian_paths(graph, b, e)
    if len(path):
        return [L[el] for el in path]
    else:
        return


L = [56, 15, 31, 43, 54, 35, 12, 23]
K = 1

print(order(L, K))
print(order_Hamiltonian(L, K))
