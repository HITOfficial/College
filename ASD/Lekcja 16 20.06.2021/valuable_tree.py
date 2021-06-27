from queue import Queue

# complexity:
# -time O(N*K) N- number of nodes, K- number of edges
# -memory O(N)


class Node():
    def __init__(self):
        self.left = None
        self.leftval = 0
        self.right = None
        self.rightval = 0
        self.X = None


# every next node I'm looking on lower levels of root node
def maximum(actual,k):
    # cannot take more elements, or it is leaf
    if actual is None or k == 0:
        return 0
    else:
        # can take 2 edges
        tmp = -float("inf")
        if k >= 2 and actual.left != 0 and actual.right != 0:
          tmp = max(actual.leftval + actual.rightval + maximum(actual.left,k-2),actual.leftval + actual.rightval + maximum(actual.right,k-2))
        # taking only one edge on this level
        return max(tmp,actual.leftval + maximum(actual.left,k-1), actual.rightval + maximum(actual.right,k-1))


def valuable_tree(A,k):
    max_value = -float("inf")
    queue_tmp = Queue()
    queue = Queue()
    queue_tmp.put(A)
    queue.put(A)
    # queue adding all possible starting nodes
    while not queue_tmp.empty():
        actual = queue_tmp.get()
        # inserting to queue left branch node
        if actual.left is not None:
            queue_tmp.put(actual.left)
            queue.put(actual.left)
        # right branch node
        if actual.right is not None:
            queue_tmp.put(actual.right)
            queue.put(actual.right)

    # in queue, now i have all posible starts of Nodes
    while not queue.empty():
        actual = queue.get()
        tmp = maximum(actual,k)
        # print(actual.leftval, actual.rightval)
        # print(tmp, actual.leftval, actual.rightval)
        if tmp > max_value:
              # print(tmp, actual.leftval, actual.rightval)
              max_value = tmp
        # max_value = max(max_value,maximum(actual,k))
    return max_value


def make_tree_1():
    A = Node()
    B = Node()
    C = Node()
    D = Node()
    E = Node()
    F = Node()
    G = Node()
    A.left = B
    A.right = E
    B.left = D
    B.right = C
    C.left = F
    C.right = G
    A.leftval = 1
    A.rightval = 5
    B.leftval = 6
    B.rightval = 2
    C.leftval = 8
    C.rightval = 10
    return A, 3


t1,k = make_tree_1()
print(valuable_tree(t1,k))


