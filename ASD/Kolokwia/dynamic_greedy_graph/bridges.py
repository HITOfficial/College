# DFS - finding all bridges in graph
# complexity O(N+E)

graph = [
    [1,6],
    [0,2,5],
    [1,3,4],
    [2,4],
    [2,3],
    [1,6,7],
    [0,5],
    [5,8,9],
    [7,9],
    [7,8]
]


def bridges(graph,start=None):
    time = 0
    if start is None:
        start = 0
    lowest = [float("inf")] * len(graph) # In this array, will be save lowest processing value of every vertex
    times = [float("inf")] * len(graph) # original times visitations from DFS
    arr_bridges = []

    def DFS_bridges(graph,lowest,times,vertex,parent): # I could fill all times array until this function, but later, I need to verify to do not come twice to the same vertex, s
        nonlocal time # working on nonlocal variable
        time += 1
        lowest[vertex] = min(lowest[vertex],time)
        for children in graph[vertex]:
            if children == parent:
                continue
            if lowest[children] == float("inf"): # vertex has not been visited before
                DFS_bridges(graph,lowest,times,children,vertex)
            lowest[vertex] = min(lowest[vertex],lowest[children])

    DFS_bridges(graph,lowest,times,start,start)
    time = 0 # reseting value of bridges

    def DFS_find_bridges(graph,lowest,arr_bridges,times,vertex,parent=None):
        nonlocal time
        time += 1
        times[vertex] = time
        if parent != None: # 
            if lowest[vertex] == times[vertex]: # found the bridge
                arr_bridges.append((parent,vertex))

        for children in graph[vertex]:
            if times[children] == float("inf"): # wasn't visited before
                DFS_find_bridges(graph,lowest,arr_bridges,times,children,vertex)

    DFS_find_bridges(graph,lowest,arr_bridges,times,start)
    
    return arr_bridges
    
    
print(bridges(graph))