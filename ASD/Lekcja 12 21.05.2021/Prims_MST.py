from queue import PriorityQueue

# a little bit modyfied Djikstra algorithm

g = [
    [(1,4),(3,3)],
    [(0,4),(4,10),(5,2)],
    [(3,9),(4,5),(5,6)],
    [(0,3),(2,9),(4,9)],
    [(1,10),(2,5),(3,9),(5,7)],
    [(1,2),(2,6),(4,7)]
]


class PriorityEdge:
    def __init__(self,start,end,weight):
        self.start = start
        self.end = end
        self.weight = weight
    
    def __gt__(self, other):
        if self.weight is None:
            return False
        return self.weight > other

    def __lt__(self, other):
        if self.weight is None:
            return True
        return self.weight < other


def Prims_MST(graph,start=None): # graph, starting vertex
    max_weight = 0

    def relax(costs,costs_on_path,start,end,weight,flag): # costs array,costs to get the path, start,end, weight of edge, flag to transfer first vertex
        nonlocal max_weight
        if flag:
            costs[end] = weight
            costs_on_path[end] = (start,max_weight)
            return True
        if costs[end] > costs[start] + weight:
            if costs[end] != float("inf"): # actual MST weight is cheaper
                max_weight -= costs[end]
            max_weight += weight
            costs_on_path[end] = (start,max_weight)
            costs[end] = costs[start] + weight
            return True
        return False


    if start is None:
        start = 0

    n = len(graph)
    counter = len(graph)
    costs = [float("inf")] *n # cost to move from vertex start, to everty vertex
    costs_on_path = [(0,float("inf"))] * n # tuple to see the path     
    p_queue = PriorityQueue()
    p_queue.put(PriorityEdge(start,start,max_weight))
    flag = True

    while not p_queue.empty() and counter > 0:
        actual_vertex =  p_queue.get()
        start_vertex, end_vertex, weight = actual_vertex.start, actual_vertex.end, actual_vertex.weight # vertexes from edge, weight of edge
        if relax(costs, costs_on_path, start_vertex, end_vertex, weight,flag) is True: # found better way
            counter -= 1
            flag = False # to mark up the next vertexes are no more first one
            start_vertex = end_vertex
            for edge in graph[end_vertex]: # addding all edges from end vertex
                end_vertex, weight = edge
                next_edge = PriorityEdge(start_vertex, end_vertex, weight)
                p_queue.put(next_edge)

    
    return max_weight # weird abs, but works, becuse normaly I'll need a flag, to stor recursion


print(Prims_MST(g))