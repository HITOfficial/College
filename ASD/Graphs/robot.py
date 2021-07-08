# content of exercisse in PL. lang. -> robot_content.png

from queue import PriorityQueue


# complexity:
# -time O(n*m*log(n*m))
# -space O(n*m)

# robot has 4 types of directions
#  up = 0
#  right = 1
#  down = 2
#  left = 3 

# two type of rotations
# left = 0 <- 60s
# right = 1 <- 60s

#                 move number: 0      1      2      3
# moves in the same direction 60s -> 40s -> 30s -> 30s ... 

def direction(i,j,k,l):
    if i == k:
        # from left -> right
        if j < l:
            return 1
        # right -> left
        else:
            return 3
    # up -> down
    elif i < k:
        return 2
    else:
        return 0


# calculating distance of edge -> returning edge weight, and moves
def calcuate_weight(direction, moves=0, last_direction=None):
        # checking how many moves made in the same direction
        if direction == last_direction:
            if moves > 1:
                return 30, moves+1
            elif moves == 1:
                return 40, 2
            else:
                return 60, 1
        # need to rotate and then move
        else:
            # array cost of edge to move with including rotation
            rotation_with_move = [
                [60,105,150,105],
                [105,60,105,150],
                [150,105,60,105],
                [105,150,105,60]
                ]
            return rotation_with_move[last_direction][direction], 1


# recreating a path to ending point
def get_path(parents,distance,actual,n,m):
    path = [(actual%m, actual//m, distance[actual])]
    if parents[actual] is not None:
        path.extend(get_path(parents, distance, parents[actual], n, m))
    return path


def relax(distance,parents,b,e,w):
    if distance[b] + w < distance[e]:
        distance[e] = distance[b] + w
        parents[e] = b
        return True
    else:
        return False


def robot_Dijkstra(graph,A,n,m):
    # on start rotated in the right side (direction number 1.)
    a,b = A[0], A[1]
    # index of begining vertex
    index = b*m+a
    distance = [float("inf")]*(n*m)
    parents = [None]*(n*m)
    # changing distance to begining vertex on 0 
    distance[index] = 0
    p_queue = PriorityQueue()
    # pushing neighbours of starting vertex
    for e,d in graph[index]:
        # edge weight, direction number, moves in a row  in same direction, vertices: begining, end
        edge_weight, moves = calcuate_weight(d, 0, 1)
        p_queue.put((edge_weight, d, moves,index, e))

    while not p_queue.empty():
        w,d,m,b,e = p_queue.get()
        if relax(distance,parents, b, e, w):
            # found better distance to vertex
            for neighbour,new_direction in graph[e]:
                # without returning to parent
                if neighbour != b:
                    edge_weight, moves = calcuate_weight(new_direction, m, d)
                    p_queue.put((edge_weight, new_direction, moves, e, neighbour))

    # returning array of distances and array to recreate path
    return distance, parents


def robot(L,A,B):
    n, m = len(L), len(L[0])
    moves = [(-1,0),(0,1),(1,0),(0,-1)]
    graph = [list() for _ in range(n*m)]

    for i in range(n):
        for j in range(m):
            if L[i][j] == " ":
                for row, col in moves:
                    new_row = i + row
                    new_col = j + col
                    # condition inside array
                    if new_row >= 0 and new_row < n and new_col >= 0 and new_col < m and L[new_row][new_col] == " ":
                        # adding typical weight of edge without rotation / second / third edg etc.
                        direction_number = direction(i, j, new_row, new_col)
                        index = i*m+j
                        neighbour_index = new_row*m+new_col
                        graph[index].append((neighbour_index, direction_number))
                        
    distance, parents = robot_Dijkstra(graph, A, n, m)
    # index of ending vertex
    # 
    index = B[1]*m+B[0]
    if distance[index] == float("inf"):
        # cannot reach to the destination
        return None
    else:
        # total distance, path -> (from, to, currently distance)
        return distance[index], list(reversed(get_path(parents,distance,index,n,m)))

    
        # 0123456789
L1 = [ 
        "XXXXXXXXXX", # 0
        "X X      X", # 1
        "X XXXXXX X", # 2
        "X        X", # 3
        "XXXXXXXXXX"  # 4
] 
A1 = (1,1)
B1 = (8,3)

        #111111111122222222223333333333
        #0123456789012345678901234567890123456789
L2 = [ 
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", # 0
        "X                                      X", # 1
        "X                                      X", # 2
        "XXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", # 3
        "X                                      X", # 4
        "X                                      X", # 5
        "XXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX XX", # 6
        "X                                      X", # 7
        "X                                      X", # 8
        "XXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", # 9
        "X                                      X", # 10
        "X                                      X", # 11
        "X        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", # 12
        "X                                      X", # 13
        "X                                      X", # 14
        "X                                      X", # 15
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   X", # 16
        "X                                      X", # 17
        "X                                      X", # 18
        "X                                      X", # 19
        "X                                      X", # 20
        "X                                      X", # 21
        "X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", # 22
        "X                                      X", # 23
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   X", # 24
        "X                                      X", # 25
        "X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", # 26
        "X                                      X", # 27
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # 28
]
A2 = (1,27)
B2 = (38,1)


print(robot(L1,A1,B1))
print("")
print(robot(L2,A2,B2))

