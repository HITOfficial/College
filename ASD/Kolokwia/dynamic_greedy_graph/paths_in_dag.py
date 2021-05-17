# Otrzymujemy na wejściu w postaci listy krawędzi skierowany graf acykliczny (DAG - Directed Acyclic Graph)
# oraz parę wierzchołków s i t. Naszym zadaniem jest obliczyć, ile jest możliwych ścieżek między s i t.


#complexity O(N+E)

# using DFS, memorizing amount of paths

graph = [
    [1,2],
    [0,2],
    [0,1,3],
    [2,4,5,7],
    [3,5],
    [3,4,7],
    [3],
    [3,5],
]


def DFS_find_t(graph,paths,vertex,parent,t):
    if vertex == t: # found t element so, shouldn't move more
        paths[parent] += 1
        return 
    if paths[vertex] == -float("inf"):
        paths[vertex] = 0

    for children in graph[vertex]:
        if paths[children] == -float("inf") and children != parent or children == t: # wasn't visited before, and is not a single leaf 
            DFS_find_t(graph,paths,children,vertex,t)
        if children != parent:
            paths[vertex] += paths[children]            


def amount_of_paths(graph,s=0,t=None):
    if t == None:
        t = len(graph)-1 # last element in graph

    n = len(graph)
    paths = [-float("inf")]* n # becouse 0 == False, on a start will be -infinity on every vertex
    paths[t] = 0
    DFS_find_t(graph,paths,s,s,t)
    print(paths)
    return paths[s]


print(amount_of_paths(graph,0,5))
    