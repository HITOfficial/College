# Check if actual graph is bipartite
from queue import Empty, Queue


graph = {
    0 : [6,8],
    1 : [3,7],
    2 : [6],
    3 : [1,6],
    4 : [5,7],
    5 : [4],
    6 : [0,2,3,7],
    7 : [1,6,4],
}


def BFS_bipartite(graph):
    n = len(graph)
    bipartition = [0] * n # -> 2 colors: -1,1  <- also if will be 0 it will show that, it was not been visited earlier
    queue = Queue()
    queue.put(*graph[0])
    bipartition[0] = 1
    while not queue.empty():        
        parent = queue.get()
        children_color = 1
        if bipartition[parent] == 1:
            children_color = -1
        for children in graph[parent]:            
            if bipartition[children] == 0: # wasn't visited before
                bipartition[children] = children_color
                queue.put(children)
            elif bipartition[children] == bipartition[parent]:
                return False
    return True

print(BFS_bipartite(graph))