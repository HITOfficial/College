from queue import PriorityQueue

# complexity O(d*Elog(V*d))

# -1 -> is not edge between a and b vertex
# there are no negative edges
G = [
    [-1,6,-1,5,2],
    [-1,-1,1,2,-1],
    [-1,-1,-1,-1,-1],
    [-1,-1,4,-1,-1],
    [-1,-1,8,-1,-1]
]

P = [0,1,3]


def get_path(paths,actual,fuel):
    path =[]
    index, fuel = paths[actual][fuel]
    if index is not None:
        path.append(index)
        path.extend(get_path(paths,index, fuel))
    return path


def relax(distances,tanked,paths,b,e,w,fuel,d,flag): # distances (2dim array), begin,end of vertex, actual edge weight, tank capacity, flag(to start vertex)
    if fuel < 0: # was not enought fuel to get into end vertex
        return False
    elif flag:
        for f in range(d+1): # filling starting vertex
            distances[b][f] = 0
        return True
    elif tanked is True: # tanked on actual station and distance is not to hight
        best_choice,index = distances[e][fuel] + 0, fuel+w # removing reference
        for i in range(fuel+w+1):
            if distances[b][i]+w < best_choice:
                best_choice = distances[b][i] + w
                index = i
        distances[e][fuel] = best_choice
        paths[e][fuel] = b, index
        return True
    elif distances[e][fuel] > distances[b][fuel+w] + w: # normal relaxing
        distances[e][fuel] = distances[b][fuel+w] + w
        paths[e][fuel] = b, fuel+w # to which corectly, parent fuel vertex should go, to recreate the path
        return True
    else:
        return False


def fueling_graph(G,P,d,a,b): # graph, fuel station, tank capacity, begin vertex, end vertex 
    # on start tank capacity is full, and on every station fueling to full
    n = len(G)
    p_queue = PriorityQueue()
    p_queue.put((0,a,a,d)) # edge weight, begin, end edge, remaining fuel
    flag = True
    ditances = [[float("inf")]*(d+1) for _ in range(n)]
    paths = [[(None,None)]*(d+1) for _ in range(n)]

    gas_station = [-1]*n
    for station in P: # I create 1 dim N table, to have O(1) acces to every station
        gas_station[station] = 1
    
    while not p_queue.empty():
        w, s, e, fuel = p_queue.get()
        tanked = False
        if gas_station[s] == 1: # there is an gas station
            fuel = d # fueling to max capacity
            tanked = True
        fuel -= w # need to reduce fuel remaing, to get into the vertex
        if relax(ditances,tanked,paths,s,e,w,fuel,d,flag):
            for ch in range(n):
                if ch != s and G[e][ch] != -1: # to do not backtrack to parent vertex, and is an edge between vertexes
                    p_queue.put((G[e][ch],e,ch,fuel))
        flag = False

    if min(ditances[b]) == float("inf"):
        return None # didnt find the path
    else:
        index, min_distance = None, float("inf")
        for vertex in range(d+1): # finding fuel vertex to start recreating the path
            if ditances[b][vertex] < min_distance:
                index = vertex
        path =  [b] + get_path(paths,b,index)
        path.reverse()
        return path

           
print(fueling_graph(G,P,5,0,2))




        
