#Exercise in PL lang.
# Na tablicach w kantorze wisi lista trójek (waluta1, waluta2, kurs). Każda z takich trójek oznacza, że kantor kupi n waluty2 za kurs*n waluty1.
# 1. Znajdź najkorzystniejszą sekwencję wymiany waluty A na walutę B
# 2. Czy istnieje taka sekwencja wymiany walut, która zaczyna się i kończy w tej samej walucie i kończymy z większą ilością pieniędzy niż zaczynaliśmy?

# 1. maximum multiply if weights of edges on path in graph from vertices A -> B: Belman Ford algorithm negative edges
# 2. n times Bellman Ford algorithm, to for all combinations

# complexity:
# -time O(V^3*E) # Bellman-Ford on all vertices 
# -memory O(V)


def get_path(paths, actual):
    path = []
    if paths[actual] is not None:
        path.append(actual)
        path.extend(get_path(paths,paths[actual]))
    return path


# Using Bellman-Ford algorithm
def Bellman_Ford_exchange(edges,A,B,n):
    weights = [float("inf")] * n
    parent = [None] * n
    weights[A] = 1
    for _ in range(n):
        for b,e,p in edges:
            if weights[e] > weights[b] * round(1/p,2): # relaxing
                weights[e] = weights[b] * round(1/p,2)
                parent[e] = b

    # detecting negative cycle
    for b,e,p in edges:
        if weights[e] > weights[b] * round(1/p,2):
            return False
    
    path = get_path(parent,B)
    path.append(A)
    path.reverse()
    return path


def money_exchange(edges,A,B): # list of tuples (currency1, currency2, price of exchange per 1 unit),
    n = max(max([(a,b) for a,b,_ in edges]))+1 # finding amount of currencies twice max, becouse after 1st I'll get max tuple
    A_B_exchanges_path = []
    flag = False
    for i in range(n-1):
        if flag:
            break
        for j in range(i+1,n):
            path =  Bellman_Ford_exchange(edges,A,B,n)
            if A == i and B == j: # memorizing 1st part of exercise (Best value exchanges path from A to B)
                A_B_exchanges_path = path
            if path is False: # found negative cycle
                if A_B_exchanges_path is not False and len(A_B_exchanges_path) == 0: # if found negative cycle then, just finding the best exchanges path from A->B
                    A_B_exchanges_path = Bellman_Ford_exchange(edges,A,B,n)
                    break

    return A_B_exchanges_path, flag


exchanges = [
    [0,1,4.50],
    [0,2,4.00],
    [1,2,0.25],
    [1,3,0.75],
    [3,2,100],
    [0,3,0.40]
]


print(money_exchange(exchanges,0,2))
