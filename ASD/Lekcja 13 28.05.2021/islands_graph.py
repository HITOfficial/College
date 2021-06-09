# exercise in PL lang. -> islands_graph.PNG
from queue import PriorityQueue
# Finding best option to travel from island A -> B in lowest cost, and also on every next island using different communication transport

# complexity
# O(ElogV)

def get_path(path,actual,transport):
    p = []
    parent = path[actual][transport][0]
    next_transport = path[actual][transport][1]
    if next_transport is not None:
        p.append(parent)
        p.extend(get_path(path, parent ,next_transport))

    return p


def options(costs,path,w,b,e):
    l = r = c = None
    if w == 1:
        c = 0
        l = 1
        r = 2
    elif w == 5:
        c = 1
        l = 0
        r = 2
    else:
        c = 2
        l = 0
        r = 1

    flag = False # removing reference, and also it will be as a flag to check if find beter option
    if costs[e][c] > costs[b][l] + w: # paying less to get to this island using b island and 
        costs[e][c] = costs[b][l] + w
        path[e][c] = (b,l) # path is weird, becouse im looking one step into (which transport I will use in the next island)
        flag = True
    if costs[e][c] > costs[b][r] + w:
        costs[e][c] = costs[b][r] + w
        path[e][c] = (b,r) # memorizing from which vertex and last transport should come
        flag = True
    return flag


def relax(costs,path,w,b,e):
    # taking best option to get into => e insland from b
    return options(costs,path,w,b,e)


def islands(Graph,A,B): # matrix adjacency, begin, end
    n = len(Graph)
    costs = [[float("inf")]*3 for _ in range(n)] # indexes: 0 <- transport 1, 1 <- transport 5, 2 <- transport 8
    costs[A] = [0,0,0]
    path = [[(None,None)]*3 for _ in range(n)] # parent, transport on parent
    p_queue = PriorityQueue() # weight, begin edge, end edge
    for i in range(n): # edges from starting vertex
        if Graph[A][i] != 0:
            p_queue.put((Graph[A][i],A,i))

    while not p_queue.empty():
        w, b, e = p_queue.get()
        if relax(costs, path, w, b, e):
            for i in range(n):
                if i != b and Graph[e][i] != 0:
                    p_queue.put((Graph[e][i],e,i))

    min_cost_index, cost = 0, float("inf")
    for i in range(3):
        if cost > costs[B][i]:
            min_cost_index = i
            cost = costs[B][i]

    if cost == float("inf"): # cannot get into B island
        return False
    else:
        best_path =  get_path(path,B,min_cost_index)
        best_path.reverse()
        best_path.append(B)
        return cost, best_path # cost, path


Graph = [
    [0,5,1,8,0,0,0],
    [5,0,0,1,0,8,0],
    [1,0,0,8,0,0,8],
    [8,1,8,8,5,0,1],
    [0,0,0,5,0,1,0],
    [0,8,0,0,1,0,5],
    [0,0,8,1,0,5,0],
]

print(islands(Graph,5,1))