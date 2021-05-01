# find an cycle in graph
# I'll do it using BFS algorithm, corectly -> if a vertex will be, again visited, it will mean, that, he haave an cycle

g = [
    [1],
    [2,3],
    [1,4],
    [1,4],
    [2,3,5],
    [6,4],
    [5]
]


def bfs(graph,vertex): # graph, index of verex
    n = len(graph)
    visited = [False] * n
    parent = [None] * n
    queue = []
    queue.append(vertex)
    visited[vertex] = True
    while len(queue) > 0:
        tmp_vertex = queue.pop(0) # taking nodes from actual graph
        # I need to unzip all parents firstly, after that childrens
        for k in graph[tmp_vertex]:
            if visited[k] is True:
                if parent[tmp_vertex] == k:
                    continue
                return True # graph has an cycle
            else:
                visited[k] = True
                parent[k] = tmp_vertex
                queue.append(k)
    return False # graph has not an cycle

print(bfs(g,0))

    