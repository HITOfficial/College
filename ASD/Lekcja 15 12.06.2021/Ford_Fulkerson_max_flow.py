# Folrd-Fulkerson algorithm: calculating max flow in weighted graph network
from queue import Queue

# algorithm from https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/

# complexity:
# -time O(E*V^3)
# -memory O(V^2)

# BFS O(V*2) on matrix adjacency
def bfs(Graph,b,e,parent):
    n = len(Graph)
    visited = [False] * n
    queue = Queue()
    queue.put(b)
    visited[b] = True
    counter = n # added extra counter to be able stop faster while loop, if all elements

    while not queue.empty() and counter > 0:
        actual = queue.get()
        for children in range(n):
            if visited[children] is False and Graph[actual][children] != 0: # is edge between vertexes        
                counter -= 1
                visited[children] = True
                parent[children] = actual
                queue.put(children)
                
    return visited[e] # returning if is posible to come into e endge, to enlarge flow


def Ford_Fulkerson_max_flow(Graph, source, sink): # graph matrix adjacency, source, sink
    n = len(Graph)
    max_flow = 0
    parent = [None] * n

    while bfs(Graph, source, sink, parent):
        actual_flow = float("inf")
        actual = sink # starting from the end

        while actual != source: # creating max flow to parent, until parent is not a source
            actual_flow = min(actual_flow,Graph[parent[actual]][actual])
            actual = parent[actual] 
        max_flow += actual_flow # adding actual flow to max flow

        actual = sink # updating residual flow
        while actual != source: # updating graph edges
            p = parent[actual]
            Graph[p][actual] -= actual_flow
            Graph[actual][p] += actual_flow
            actual = p

    return max_flow


Graph = [
    [0,5,4,0,0],
    [0,0,2,0,2],
    [0,0,0,2,3],
    [0,0,0,0,2],
    [0,0,0,0,0],
]

print(Ford_Fulkerson_max_flow(Graph,0,4))
