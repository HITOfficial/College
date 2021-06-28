# Floyd-Warshall alg. to calculate min distance between all vertices O(V^3)
# BFS alg. on sticked vertices O(V^4)
from queue import Queue

# complexity:
# -time O(V^4)
# -memory O(V^4)


def Floyd_Warshall_distances(G):
    n = len(G)
    weights = [[0 if u == v else G[u][v] if G[u][v] != 0 else float("inf") for v in range(n)] for u in range(n)]
    for vertex in range(len(G)):
        for begin in range(len(G)):
            for end in range(len(G)):
                if weights[begin][end] > weights[begin][vertex] + weights[vertex][end]:
                    weights[begin][end] = weights[begin][vertex] + weights[vertex][end]
    return weights


# checking minimum distance between vertices
def verivy_distance(distances,x,y,d):
    if distances[x][y] >= d:
        return True
    else:
        return False


def new_vertices(graph,distances,d):
    n = len(graph)
    # creating n^2 vertices
    # can not do moves using the same edge at the same time
    # edges between (i,j) -> (a,b)
    # very ugly if statement but works fine
    new_grap = [[0 if (graph[i][a] == 0 and i != a) or (graph[j][b] == 0 and j != b) or (a==j and b==i) or a==b or i==j else 1 if verivy_distance(distances,a,b,d) else 0  for a in range(n) for b in range(n)] for i in range(n) for j in range(n)]
    return new_grap
    

def get_path(paths,actual,n):
    path = []
    if actual is not None:
        path.append((actual%n,actual//n))
        path.extend(get_path(paths,paths[actual],n))
    return path


# BFS without executing time
def BFS(graph,x,y,prev_n):
    n = len(graph)
    # reverse to linearization table
    index = x*prev_n + y
    visited = [False]*n
    visited[index] = True
    paths = [None]*n
    queue = Queue()
    queue.put(index)

    while not queue.empty():
        next_queue = Queue()
        while not queue.empty():
            actual = queue.get()
            for k in range(n):
                # checking if is edge b
                if visited[k] is False and graph[actual][k] != 0:
                    paths[k] = actual
                    visited[k] = True
                    next_queue.put(k)
        queue = next_queue
    return paths


def keep_distance(M, x, y, d):
    n = len(M)
    distances = Floyd_Warshall_distances(M)
    graph = new_vertices(M,distances,d)
    paths = BFS(graph,x,y,n)
    return get_path(paths,y*n+x,n)


M1 = [ 
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

M = [
    [0, 5, 1, 0, 0, 0],
    [5, 0, 0, 5, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [0, 5, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0]
]

print(keep_distance(M1,0,5,1))
print(keep_distance(M,0,5,4))