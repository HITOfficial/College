# minimalizing difference of total edges weights between two subtrees after removing one edge

# complexity:
# - time O(N)
# - space O(N), in every node extra data -> subtree sum

class Node:
    def __init__(self):
        self.edges = []
        self.weights = []
        self.ids = []
        self.subtreeSum = 0

    def addEdge(self, x, w, id):
        self.edges.append(x)
        self.weights.append(w)
        self.ids.append(id)

    def updateSubtreeSum(self):
        for e, w in zip(self.edges, self.weights):
            self.subtreeSum += w + e.subtreeSum


def update_subtree_sum(T):
    for n in T.edges:
        update_subtree_sum(n)
    T.updateSubtreeSum()


# bottom up finding edge -> minimalizing difference between two subtrees after removing only one edge
def balance_edge(node, root):
    difference, idx = float("inf"), None
    for e, w, i in zip(node.edges, node.weights, node.ids):
        # bottom -> up
        tmp_difference, tmp_idx = balance_edge(e, root)
        if tmp_difference < difference:
            difference, idx = tmp_difference, tmp_idx
        # difference with removing actual edge
        subtree_root, subtree_child = root.subtreeSum - e.subtreeSum - w, e.subtreeSum
        if abs(subtree_root - subtree_child) < difference:
            difference, idx, = abs(subtree_root - subtree_child), i
    return difference, idx


def balance(T):
    # updating hight of every tree
    update_subtree_sum(T)
    _, idx = balance_edge(T, T)
    return idx


A, B, C, D, E = Node(), Node(), Node(), Node(), Node()
A.addEdge(B, 6, 1), A.addEdge(C, 10, 2), B.addEdge(D, 5, 3), B.addEdge(E, 4, 4)

print(balance(A))
