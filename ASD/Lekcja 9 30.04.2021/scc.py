# SCC - strongly conected components
# DFS- if cannot go to next vertex - backtracking with marking the fields
# reversing moving in DFS from last vertex from highest executing time, and reversing the path

g = [
    [1,4],
    [3,2],
    [0,7],
    [4,6],
    [5],
    [3],
    [5],
    [9],
    [6,7],
    [10],
    [8]
]


def SSC_components(graph_opposite,vertex,used):
    components = [vertex]
    used[vertex] = True # marking that was used
    for neighbour in graph_opposite[vertex]:
        if used[neighbour] == False:
            components.extend(SSC_components(graph_opposite,neighbour,used))
    return components


# I'll colect elements and mark them
def DFS_with_opposite_path(graph, times, vertex, time, graph_opposite):
    times[vertex] = (True,vertex) # tmp mark to not come in in recursion of neighbours
    for children in graph[vertex]:
        graph_opposite[children].add(vertex)
        if times[children][0] == False: # wasn't before this vertex visited
            time = DFS_with_opposite_path(graph, times, children,time, graph_opposite)
    times[vertex] = (time,vertex)
    return time+1


def SCC(graph):
    n = len(graph)
    times =[(False,i) for i in range(n)] # I need to mark whih vertex has whih points, becose, after that I need to sort descending them during searching oposite neighbors 
    graph_opposite = [set() for _ in range(n)]
    components = []
    time = 1
    for i in range(n):
        if times[i][0] == False:
            time = DFS_with_opposite_path(graph,times, i, time, graph_opposite)
    # I have small bug, becouse, i made opposite paths easly, from this reason I used a set to do not multiply, the same neighbours
    graph_opposite = [list(graph_opposite[i]) for i in range(n)]
    # sort descending of times
    times.sort(key=lambda item: item[0],reverse=True)
    # starting from highest recreating strongly connected components
    used = [False] * n
    for i in range(n):
        if used[times[i][1]] == False:
            components.append(SSC_components(graph_opposite,times[i][1],used))

    return components


print(SCC(g))