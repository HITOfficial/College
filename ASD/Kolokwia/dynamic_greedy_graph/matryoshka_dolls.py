# Sasza kolekcjonuje rosyjskie lalki - matrioszki. Każda z nich ma określoną wysokość X i szerokość Y,
# dane liczbami naturalnymi dodatnimi. Jedną matrioszkę można włożyć do drugiej,jeżeli ma od niej mniejszą zarówno wysokość, jak i szerokość.
# Sasza zastanawia się, jaki jest najdłuższy ciąg matrioszek, które może powkładać w siebie po kolei. Pomóż mu znaleźć odpowiedź na to pytanie.


# directed graph


dolls = [(1,10),(3,15),(4,14),(7,17),(5,50),(6,60)]


def is_edge(a,b):
    if a[0] > b[0] and a[1] > b[1]:
        return True
    else:
        return False

# complexity

# O(n^2) <- creating all edges in directed graph
# O(n*e) <- dfs algorithm


def dfs_LIS(graph,LIS,vertex,time=1):
    LIS[vertex] = max(LIS[vertex],time)
    for children in graph[vertex]:
        LIS[vertex] = max(LIS[vertex],dfs_LIS(graph,LIS,children,time))
    return LIS[vertex]+1



def matryoshka_dolls(dolls):

    n = len(dolls)
    graph = [[ b for b in range(n) if is_edge(dolls[a],dolls[b]) and a != b] for a in range(n)]
    print(graph)

    LIS = [0] * n # longest increasing subsequence nuber ending on every vertex

    for vertex in range(n):
        dfs_LIS(graph,LIS,vertex)

    return max(LIS)

    
print(matryoshka_dolls(dolls))