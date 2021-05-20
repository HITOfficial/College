from copy import deepcopy
from queue import Queue
from find_union import * # another folder with data structure functions


g = [
    [(1,4),(3,3)],
    [(0,4),(4,10),(5,2)],
    [(3,9),(4,5),(5,6)],
    [(0,3),(2,9),(4,9)],
    [(1,10),(2,5),(3,9),(5,7)],
    [(1,2),(2,6),(4,7)]
]


def convert_to_edges(g):
    edges = []
    for i in range(len(g)):
            edges.extend([(i,el[0],el[1]) for el in g[i]])  # Firstly I need to convert graph to list of Edges -> (vertex1,vertex2,weight)
    return list(set(edges))


def Kruskal_MST(graph,n=None): # graph, length of graph
    edges = deepcopy(graph) # mutable 2 dimension list
    if n is None: # graph is as list of vertexes
        n = len(graph)
        edges = convert_to_edges(g)

    trees = [make_set(i) for i in range(n)] # vertexes to strustur
    MST = [] * n

    counter = len(g) # while counter == 0 -> found MST in graph

    edges.sort(key=lambda element: element[2]) # sort by value

    p_queue = Queue()
    for edge in edges: # updating all sorted vertexes to queue
        p_queue.put(edge)

    while not p_queue.empty() and counter > 0:
        b,e,w = p_queue.get() # begin, end, weight of edge
        if union(trees[b],trees[e]) == False: # found an cycle
            continue
        else:
            counter -= 1
            MST.append((b,e,w))

    return *[(v1,v2) for v1,v2,_ in MST], sum([weight for _,_,weight in MST]) # returning -> edges, sum of MST


print(Kruskal_MST(g))