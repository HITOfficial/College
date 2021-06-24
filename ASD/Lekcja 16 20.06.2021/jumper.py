from queue import PriorityQueue

# matrix adjacency of weighted undirected graph

# complexity:
# -time O(V^3logV)
# -memory O(V) -> 4*V

def get_path(paths,actual,way,between):
    path = []
    # inserting vertex between double edge
    if between is not None:
        path.append(between)
    if actual is not None:
        path.append(actual)
        new_actual, new_way, new_between = paths[actual][way]
        path.extend(get_path(paths,new_actual,new_way,new_between))
    return path


# function to insert edges to queue distanced apart 2 edges
def insert_neighbours(graph,n,p_queue,prev,b):
    for e in range(n):
        if graph[b][e] != 0 and e != prev:
            p_queue.put((max(graph[prev][b],graph[b][e]),prev,e,b,1))


def jumper(G, s, w):
    n = len(G)
    # creating extra connections of weight max from two edges and marking up them
    # two ways of distance, first ended on single step second from extra edge
    graph = G
    # distance: single edge (lowest distance, number of used edges), double edge (lowest distance, number of used edges)
    distances = [[(float("inf"),float("inf")),(float("inf"),float("inf"))] for _ in range(n)]
    # to recreate path, need to have fields previus vertex, which case, extra vertex between on bouble edges
    paths = [[(None,None,None),(None,None,None)] for _ in range(n)]
    # two flags as 4th parameter: 0 previous jump was by 1 edge, 1 previous jump by 2 edges jumps
    p_queue = PriorityQueue()
    distances[s] = ((0,0),(0,0))
    # instering neigbours of starting vertex, and vertices which are neighbours, of neigbour
    for i in range(n):
        # finding edge between vertices
        if graph[s][i] != 0:
            # weight of edge, begin, end of edge, vertex between apart 2 edges distances, last jump flag
            d = graph[s][i]
            p_queue.put((graph[s][i],s,i,i,0))
            # inserting vertices, apart 2 edges distance
            insert_neighbours(graph,n,p_queue,s,i)

    while not p_queue.empty():
        d,b,e,between,flag = p_queue.get()

        # single edge relax
        if flag == 0:
            # relaxing edge: one step previus lower distance or less used edges
            if distances[e][0][0] > distances[b][0][0]+d or (distances[e][0][0] == distances[b][0][0]+d and distances[e][0][1] > distances[b][0][1]+1):
                distances[e][0] = distances[b][0][0]+d, distances[b][0][1]+1
                # single edge
                paths[e][0] = b,0,None
                # inserting double edge vertexes to priority queue
                for end in range(n):
                    if graph[e][end] != 0 and end != b:
                        p_queue.put((graph[e][end],e,end,b,0))
                        insert_neighbours(graph,n,p_queue,e,end)
                        
            # relaxing edge: relaxing using 2 edges step on previous
            if distances[e][0][0] > distances[b][1][0]+d or (distances[e][0][0] == distances[b][1][0]+d and distances[e][0][1] > distances[b][1][1]+1):
                distances[e][0] = distances[b][1][0]+d, distances[b][1][1]+1
                # on path need to look on double edge parent
                paths[e][0] = b,1,None
                for end in range(n):
                    if graph[e][end] != 0 and end != b:
                        p_queue.put((graph[e][end],e,end,b,0))
                        insert_neighbours(graph,n,p_queue,e,end)

        # relaxing double edge
        else:
            if distances[e][1][0] > distances[b][0][0]+d or (distances[e][1][0] == distances[b][0][0]+d and distances[e][0][1] > distances[b][0][1]+2):
                distances[e][1] = distances[b][0][0]+d, distances[b][0][1]+2
                # need to memorize vertex between double edge
                paths[e][1] = b,0,between
                for end in range(n):
                    # inserting single edges to queue
                    if graph[e][end] != 0 and end != b:
                        p_queue.put((graph[e][end],e,end,b,0))

    # taking best option to get into ending vertex in path
    distance, edges_number = distances[w][0]
    actual,way,between = paths[w][0]
    # checking if better option is taking taking double edge to get into ending edge - lower distance, or less used edges
    if distances[w][1][0] < distance or (distances[w][1][0] == distance and distances[w][1][1] < edges_number):
        actual,way,between = paths[w][1]
        distance, edges_number = distances[w][1]
        
    path = list(reversed(get_path(paths,actual,way,between)))
    path.append(w)
    # returning distance to vertex, number of edges, path to get into
    return distance,edges_number, path


graph = [
    [0,1,0,0,0,0],
    [1,0,1,0,0,0],
    [0,1,0,7,0,0],
    [0,0,7,0,8,0],
    [0,0,0,8,0,16],
    [0,0,0,0,16,0],
]

g = [[0, 51, 168, 199, 66, 230, 182, 133, 158, 128, 57, 283, 313, 395, 186, 137, 71, 168, 95, 192],
    [51, 0, 194, 57, 254, 133, 216, 5, 201, 76, 230, 207, 217, 121, 230, 4, 351, 230, 286, 84] ,
    [168, 194, 0, 24, 151, 292, 304, 103, 246, 253, 9, 326, 309, 191, 0, 375, 92, 352, 286, 281] ,
    [199, 57, 24, 0, 88, 46, 103, 184, 392, 263, 400, 216, 232, 214, 87, 124, 234, 122, 81, 107] ,
    [66, 254, 151, 88, 0, 101, 373, 301, 324, 254, 223, 263, 145, 250, 27, 25, 206, 74, 117, 169] ,
    [230, 133, 292, 46, 101, 0, 24, 371, 117, 295, 46, 213, 75, 69, 334, 216, 270, 208, 130, 177] ,
    [182, 216, 304, 103, 373, 24, 0, 46, 41, 244, 114, 24, 298, 115, 328, 33, 368, 295, 342, 103] ,
    [133, 5, 103, 184, 301, 371, 46, 0, 287, 225, 14, 194, 304, 145, 353, 71, 119, 130, 40, 268] ,
    [158, 201, 246, 392, 324, 117, 41, 287, 0, 152, 364, 44, 121, 64, 363, 305, 14, 365, 237, 136] ,
    [128, 76, 253, 263, 254, 295, 244, 225, 152, 0, 277, 75, 314, 247, 124, 206, 320, 281, 157, 289] ,
    [57, 230, 9, 400, 223, 46, 114, 14, 364, 277, 0, 88, 163, 280, 145, 273, 81, 75, 400, 108] ,
    [283, 207, 326, 216, 263, 213, 24, 194, 44, 75, 88, 0, 36, 286, 109, 122, 339, 333, 50, 16] ,
    [313, 217, 309, 232, 145, 75, 298, 304, 121, 314, 163, 36, 0, 146, 107, 116, 324, 228, 316, 85] ,
    [395, 121, 191, 214, 250, 69, 115, 145, 64, 247, 280, 286, 146, 0, 162, 289, 328, 324, 46, 151] ,
    [186, 230, 0, 87, 27, 334, 328, 353, 363, 124, 145, 109, 107, 162, 0, 346, 178, 43, 117, 114] ,
    [137, 4, 375, 124, 25, 216, 33, 71, 305, 206, 273, 122, 116, 289, 346, 0, 44, 175, 72, 44] ,
    [71, 351, 92, 234, 206, 270, 368, 119, 14, 320, 81, 339, 324, 328, 178, 44, 0, 327, 256, 78] ,
    [168, 230, 352, 122, 74, 208, 295, 130, 365, 281, 75, 333, 228, 324, 43, 175, 327, 0, 121, 182] ,
    [95, 286, 286, 81, 117, 130, 342, 40, 237, 157, 400, 50, 316, 46, 117, 72, 256, 121, 0, 321] ,
    [192, 84, 281, 107, 169, 177, 103, 268, 136, 289, 108, 16, 85, 151, 114, 44, 78, 182, 321, 0] 
]

print(jumper(g,0,19))
print(jumper(graph,0,5))
