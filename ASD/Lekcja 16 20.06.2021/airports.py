# Exercise in Pl lang.
# Dostajemy na wejściu listę trójek (miastoA, miastoB, koszt). Każda z nich oznacza, że możemy zbudować drogę między miastem A i B za podany koszt. Ponadto, w dowolnym mieście możemy zbudować lotnisko za koszt K, niezależny od miasta. Na początku w żadnym mieście nie ma lotniska, podobnie między żadnymi dwoma miastami nie ma wybudowanej drogi.
# Naszym celem jest zbudować lotniska i drogi za minimalny łączny koszt, tak aby każde miasto miało dostęp do lotniska.
# Miasto ma dostęp do lotniska, jeśli:
# jest w nim lotnisko, lub
# można z niego dojechać do innego miasta, w którym jest lotnisko
# Jeżeli istnieje więcej niż jedno rozwiązanie o minimalnym koszcie, należy wybrać to z największą ilością lotnisk.
from queue import Queue

# Mix of Kruskal MST, on every vertex, and trying to create connection with other city, if the cost between is less than k

# complexity:
# -time O(ElogV)
# -memory O(V)


# make set structure
class MakeSet:
    def __init__(self, value, rank=0):
        self.value = value
        self.rank = rank
        self.parent = self


def make_set(value):
    return MakeSet(value)


def find(node):
    if node != node.parent:
        node.parent = find(node.parent)
    return node.parent


def union(tree1,tree2):
    tree1 = find(tree1)
    tree2 = find(tree2)
    if tree1 == tree2:
        return False
    
    if tree1.rank > tree2.rank:
        tree1.rank += 1
        tree2.parent = tree1
    elif tree1.rank == tree2.rank:
            tree2.parent = tree1
    else:
        tree2.rank += 1
        tree1.parent = tree1
    return True


def get_max(edges):
    max_id = -float("inf")
    for a,b,_ in edges:
        max_id = max(max_id,a,b)
    return max_id


def airports(edges,k):
    max_id = get_max(edges)
    n = max_id+1
    trees = [make_set(i) for i in range(max_id)]
    # to do not modify priority queue, preference, weight will be as a first element of tuple
    edges = [(w,a,b) for a,b,w in edges]
    # sorting by edge weight
    edges.sort()
    airports = [True]*n
    queue = Queue()
    for edge in edges:
        queue.put(edge)

    while not queue.empty():
        w,b,e = queue.get()
        if w < k:
            # checking up if is allready connected
            if union(trees[b],trees[e]) == False: # found an cycle
                continue
            else:
                if trees[b].parent != trees[b]:
                    airports[b] = False
                if trees[e].parent != trees[e]:
                    airports[e] = False 

    counter = 0        
    for boolean in airports:
        if boolean:
            counter += 1
    return counter


edges = [(0,1,10),(1,2,3),(2,3,2),(3,4,1),(4,5,6),(4,6,4),(5,0,4),(2,7,6),(0,7,7)]

print(airports(edges,5))