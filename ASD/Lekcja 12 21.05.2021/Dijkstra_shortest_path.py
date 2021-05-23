from queue import PriorityQueue

g = [
    [(1,4),(3,3)],
    [(0,4),(4,10),(5,2)],
    [(3,9),(4,5),(5,6)],
    [(0,3),(2,9),(4,9)],
    [(1,10),(2,5),(3,9),(5,7)],
    [(1,2),(2,6),(4,7)]
]


def relax(costs,start,end,weight,flag): # costs array, start,end, weight of edge, flag to transfer first vertex
    if flag:
        costs[end] = weight
        return True
    if costs[end] > costs[start] + weight:
        costs[end] = costs[start] + weight
        return True
    return False



def get_path(parent,actual):
    path = []
    if parent[actual] is not None:
        path += [parent[actual]] + get_path(parent,parent[actual])
    return path



def Dijkstra_shortest_path(graph,start= None,end=None): # graph, starting vertex
    if start is None:
        start = 0
    if end == None:
        end = len(graph)-1

    n = len(graph)
    counter = len(graph)
    costs = [float("inf")] *n # cost to move from vertex start, to everty vertex
    parent = [None] * n # in this array I'll memorize path
    p_queue = PriorityQueue()
    p_queue.put((start,start,0))
    flag = True

    while not p_queue.empty() and counter > 0:
        start_vertex, end_vertex, weight = p_queue.get() # edge,weight, of vertex
        if relax(costs, start_vertex, end_vertex, weight,flag) is True: # found better way
            if flag is False:
                parent[end_vertex] = start_vertex
            flag = False
            start_vertex = end_vertex
            for edge in graph[end_vertex]: # addding all edges from end vertex
                end_vertex, weight = edge
                tpl = start_vertex, end_vertex, weight
                p_queue.put((tpl))
                
    path = get_path(parent,end)
    path.insert(0,end) # I need to insert last element manualy

    return costs[end], list(reversed(path)), # tuple -> cost, array of vertexes


print(Dijkstra_shortest_path(g,0,4))