# Exercise in PL lang.
# Dostajemy na wejściu listę krawędzi drzewa (niekoniecznie binarnego!) oraz wyróżniony wierzchołek - korzeń.
# Każdy wierzchołek tworzy swoje własne poddrzewo. Dla każdego wierzchołka, wyznacz ilość wierzchołków w jego poddrzewie.

# complexity:
# -time O(N)
# -memory O(N)


# recursive finding all subtrees
def find_subtree(graph,sizes,actual):
    for children in graph[actual]:
        find_subtree(graph,sizes,children)
        sizes[actual] += sizes[children]


def subtree_size(graph,beginning=0):
    n = len(graph)
    sizes = [1] * n
    find_subtree(graph,sizes,beginning)
    return sizes


graph = [
    [2,3],
    [],
    [5,8,12],
    [4,6],
    [],
    [1,10],
    [7],
    [11,9],
    [],
    [],
    [],
    [],
    []
]

print(subtree_size(graph,0))