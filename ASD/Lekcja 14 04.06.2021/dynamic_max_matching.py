# finding maximum matching in tree, using dynamic programing
from collections import deque
# on every vertex can be maximum only one edge

# complexity:
# -time O(V)
# -memory O(V)

def get_matches(Graph,path): # geting path of matched edges
    edges = []
    for i in range(len(Graph)):
        if path[i] is not None:
            edges.append((i,path[i]))
    return edges


# G(x) = Sum(max(F(i),G(i)))+ edge weight, where is child of x element <- including edge to G element
def G(Graph,f,g,path,actual): # including edge to children
    best_variant = None, 0, None, None, None # index, best value, including edge weight
    # need to find best children vertex option to match new edge, so twice runing for loop for childrens to find best variant
    for i,weight in Graph[actual]:
        if best_variant[1] <= g[i] and weight + f[i] > g[i]:
            if best_variant[3] is not None:
                path[best_variant[3]] = best_variant[4]
            if best_variant[0] is not None: # found better option so need to change            
                g[actual] -= best_variant[2]
            path[actual] = i
            best_variant = i, weight + f[i], weight, i, path[i]
            g[actual] += weight + f[i]
            path[i] = None
        else:
            g[actual] += g[i]


# F(x) = Sum(G(i)), where i are childrens of x element <- without edge (x-i)
def F(Graph,f,g,actual): # without edge to children
    for i,weight in Graph[actual]:
        f[actual] += g[i] # taking best option
        

def max_matching(Graph):
    n = len(Graph)
    g = [0] * n
    f = [0] * n
    path = [None] * n
    # becouse algorithm should work bottom up, from this reason im using deque to memorize elements
    deq = deque()
    deq.appendleft(0)
    deq_tmp = deque()
    deq_tmp.appendleft(0)
    while deq_tmp: # until are elements in dequeue
        actual = deq_tmp.popleft()
        for i,w in Graph[actual]:
            deq.appendleft(i)
            deq_tmp.appendleft(i)

    while deq:
        actual = deq.popleft()
        F(Graph,f,g,actual)
        G(Graph,f,g,path,actual)

    return g[0], get_matches(Graph,path)


Graph = [
    [(1,100),(2,1)],
    [(4,1),(5,1),(6,1)],
    [(3,1),(9,1),(11,1)],
    [],
    [(10,1)],
    [(7,1),(8,1)],
    [],
    [],
    [],
    [(12,1)],
    [],
    [],
    []
    ]

print(max_matching(Graph))
