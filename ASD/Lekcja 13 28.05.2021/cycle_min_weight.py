# min weight of cycle in graph 
# complexity O(V^2*Elog(V)) # removing all possible edges, and finding dijkstra between vertex s,t

from queue import PriorityQueue
from typing import Counter

# -1 -> there is no edges between
g = [
    [-1,1,-1,-1,2,3,7],
    [1,-1,7,-1,3,-1,-1],
    [-1,7,-1,6,-1,12,-1],
    [-1,-1,6,-1,2,-1,-1],
    [2,3,-1,2,-1,-1,4],
    [3,-1,12,-1,-1,-1,-1],
    [7,-1,-1,-1,4,-1,-1]
]


def get_solution(paths,actual): # geting array, of dijkstra path
    path = []
    if paths[actual] is not None:
        path.append(paths[actual])
        path.extend(get_solution(paths,paths[actual]))
    return path


def relax(costs,start,end,weight,flag): # costs array, start,end, weight of edge, vertex which started Dijkstra
    if flag:
        costs[end] = weight
        return True
    elif costs[end] > costs[start] + weight:
        costs[end] = costs[start] + weight
        return True
    else:
        return False


def Dijkstra(g,s,t,w): # graph, begin, end, weight of edge removed
    n = len(g)
    p_queue = PriorityQueue()
    counter = n
    parents = [None] * n # memorizing the paths
    costs = [float("inf")] * n
    flag = True
    p_queue.put((w,s,s))

    while not p_queue.empty() and counter > 0:
        w,b,e = p_queue.get()
        if relax(costs,b,e,w,flag):
            if not flag:
                parents[e] = b
            for ch in range(n):
                if g[e][ch] != -1 and ch != b:
                    p_queue.put((g[e][ch],e,ch))
        flag = False
    if costs[t] is not False:
        path = get_solution(parents,t)
        path.reverse()
        path.append(t)
        return costs[t],path
    else:
        return float("inf"), []


# returing weight, of min weight cycle with the path, otherwise None if is not an cycle in graph 
def Dijkstra_cycle(g): # graph
    n = len(g)
    best_solution_w = float("inf") # lowest weight of cycle
    best_solution_p = [] # path of the best cycle
    for s in range(n-1):
        for t in range(s+1,n):
            if g[s][t] != -1: # there is an edge
                edge_weight= g[s][t]
                g[s][t] = g[t][s] = -1 # removing the edge
                weight,path = Dijkstra(g,s,t,edge_weight)
                if best_solution_w > weight:
                    best_solution_w = weight
                    best_solution_p = path
                g[s][t] = g[t][s] = edge_weight # adding again the same edge

    if best_solution_w is float("inf"):
        return None # didn't find the path
    else:
        return best_solution_w, best_solution_p


print(Dijkstra_cycle(g))
