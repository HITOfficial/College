# Edmonds-Karp algorithm to find max flow in flow network
from queue import Queue

# complexity:
# -time O(V*E^2)
# -memory O(V^2)


class MinFlow(): # Class to memorize lowest edge value in BFS path
    def __init__(self,flow):
        self.flow = flow
        

def bfs_min_flow(graph,parents,b,e,min_flow):
    n = len(graph)
    for i in range(n): # to do not remove reference to parents list
        parents[i] = None
    parents[b] = b

    queue = Queue()
    queue.put(b)
    while not queue.empty():
        actual = queue.get()
        for children in range(n):
            if parents[children] is None and graph[actual][children] != 0: # vertex wasn't visited before
                parents[children] = actual
                queue.put(children)

    if parents[e] is not None: # is able to get into last vertex
        while e != b:
            min_flow.flow = min(min_flow.flow, graph[parents[e]][e])
            e = parents[e]
        return True
    else:
        return False


def Edmonds_Karp_max_flow(graph,source,sink):
    n = len(graph)
    max_flow = 0
    parents = [None] * n
    new_flow = MinFlow(float("inf"))
    while bfs_min_flow(graph, parents, source, sink,new_flow): # finding if is able to move from source to sink
        max_flow += new_flow.flow

        actual = sink
        while actual != source: # changing residual network
            graph[parents[actual]][actual] -= new_flow.flow # changing edges flow capacity
            graph[actual][parents[actual]] += new_flow.flow
            actual = parents[actual]
        new_flow.flow = float("inf") # reset of flow, to next BFS run

    return max_flow


graph = [
    [0,8,5,0,0,0,0,0],
    [0,0,0,2,0,4,0,0],
    [0,0,0,0,4,0,0,0],
    [0,0,0,0,2,3,0,0],
    [0,0,0,0,0,0,4,6],
    [0,0,0,0,0,0,2,0],
    [0,0,0,0,0,0,0,4],
    [0,0,0,0,0,0,0,0],
]

print(Edmonds_Karp_max_flow(graph,0,7))
