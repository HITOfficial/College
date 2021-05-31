# finding ending vertexes from diameter in graph
# Tree graph
# not weighted graph
# twice running DFS, looking like BFS, memorize max time vertexe, data reset and repeat once more

# complexity:
# -time O(V*V) -> matrix representation
# -memory O(V)


class Time:
    def __init__(self, time):
        self.time = time


def DFS(G,times,time, actual): # I could also do this on BFS, becouse im looking for shorest path to get into
    time.time += 1
    time_cp = time.time
    times[actual] = time.time
    for i in range(len(G)):
        if G[actual][i] != 0 and (times[i] is None or times[i] > time.time+1):
            DFS(G,times,time,i)
            time.time = time_cp
    time.time = time_cp
    

def max_time(times):
    max_time_id = 0
    for i in range(len(times)):
        if times[i] > times[max_time_id]:
            max_time_id = i
    return max_time_id


def diameter(G): # graph G in matrix representation of tree
    n = len(G)
    time = Time(-1)
    times = [None] * n
    DFS(G,times,time,0)
    vertex1 = max_time(times)
    times = [None] * n # reseting times and runing again DGS
    time = Time(-1)
    DFS(G,times,time,vertex1)
    vertex2 = max_time(times)
    return vertex1, vertex2 # returing ends vertexes of diameter


G = [
    [0,1,0,1,0,0,0],
    [1,0,1,0,0,1,0],
    [0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0],
    [0,0,0,0,0,1,0],
    [0,1,0,0,1,0,0],
    [0,0,1,0,0,0,0],
    ]


print(diameter(G))