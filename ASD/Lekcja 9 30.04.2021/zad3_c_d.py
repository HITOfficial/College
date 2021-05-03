# c) Zakładając, że pola o indeksach [0][0] i [n-1][n-1] są lądem, sprawdź czy da się przejść drogą lądową z pola [0][0] do pola [n-1][n-1]. Można chodzić tylko na boki, nie na ukos.
# d) Znajdź najkrótszą ścieżkę między tymi punktami. Wypisz po kolei indeksy pól w tej ścieżce
from queue import Queue
# I'll use BFS method

 # 1- land
 # 0 - water
G = [
    [1,0,1,1,1,1,1,1],
    [1,0,1,0,0,1,1,1],
    [1,1,1,0,0,1,0,1],
    [1,0,0,0,0,1,0,1],
    [1,1,0,0,1,1,1,1],
    [1,0,1,1,1,1,0,0],
    [0,0,1,0,0,1,0,1],
    [1,1,1,0,1,1,1,1]
]


def find_lands(graph,i,j):
    lands = []
    if i-1 >= 0:
        lands.append([i-1,j])
    if i+1 < len(graph):
        lands.append([i+1,j])
    if j-1 >= 0:
        lands.append([i,j-1])
    if j+1 < len(graph):
        lands.append([i,j+1])
    return lands


def print_path(mark_route,i,j,value_before,start_i,start_j):
    if i == start_i and j == start_j:
        pass
    else:
        for route in find_lands(mark_route,i,j):
            tmp_route_value = mark_route[route[0]][route[1]]
            if tmp_route_value < value_before:
                print_path(mark_route,route[0],route[1],tmp_route_value,start_i,start_j)
    print((i,j),end ="->")


def bfs_c_d(graph,start_i=0,start_j=0,end_i=None,end_j=None): # graph, path start, path end
    if end_i == None:
        end_i = len(graph)-1
    if end_j == None:
        end_j = len(graph)-1

    if len(find_lands(graph,start_i,start_j)) == 0 or len(find_lands(graph,end_i,end_j)) == 0 and not(start_i == end_i and start_j == end_j):
        return False

    mark_route = [[float("inf")] * len(graph) for _ in range(len(graph))]
    queue = Queue()
    step = -1
    queue.put([start_i,start_j])
    while not queue.empty():
        step += 1
        new_queue = Queue() # it will search for new fields to next Queue
        while not queue.empty():
            coord = queue.get()
            if mark_route[coord[0]][coord[1]] == float("inf") and graph[coord[0]][coord[1]] == 1: # it is a water and was noot seen before
                mark_route[coord[0]][coord[1]] = step
                for new_coord in find_lands(graph,coord[0],coord[1]):
                    new_queue.put(new_coord)
        queue = new_queue
    end_land_value = mark_route[end_i][end_j]
    if end_land_value != float("inf"): # algorithm found the path, so now can print it
        print_path(mark_route, end_i, end_j, end_land_value, start_i, start_j)
    return ""

    
print(bfs_c_d(G,0,0,6,7))