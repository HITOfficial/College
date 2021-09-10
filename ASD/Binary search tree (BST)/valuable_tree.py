# A bine T tree is given, where each edge has a value. Please implement
# function which note the value of k edges T students subtree.
# The feature should be as fast as possible. Please estimate the time and memory complexity of the algorithm system.

# complexity:
# - time O(N*K)
# - space O(K) -> stack size in recursion

class Node:
    def __init__(self):
        self.left = None
        self.leftval = 0
        self.right = None
        self.rightval = 0
        self.X = None


# recursive with backtracking, and without memorizing
def rec_k_sum(node, k):
    if k == 0 or (node.left and node.right is None):
        return 0
    i = 0
    total_sum = -float("inf")
    while i <= k:
        left_sum = 0
        right_sum = 0
        # i from left branch k-i from right branch
        if node.left is not None and i >= 1:
            left_sum += rec_k_sum(node.left, i-1) + node.leftval
        if node.right is not None and k-i >= 1:
            right_sum += rec_k_sum(node.right, k-i-1) + node.rightval
        total_sum = max(total_sum, left_sum+right_sum)
        i += 1
    return total_sum


def valuable_sum(node, k):
    if node is None:
        return 0
    total_sum = -float("inf")
    # bottom up finding best sum
    if node is not None:
        total_sum = max(rec_k_sum(node, k), total_sum, valuable_sum(
            node.left, k), valuable_sum(node.right, k))
    return total_sum


A, B, C, D, E, F, G = Node(),  Node(), Node(), Node(), Node(),  Node(),  Node()
A.left, A.right, A.leftval, A.rightval = B, E, 1, 5
B.left, B.right, B.leftval, B.rightval = D, C, 6, 2
C.left, C.right, C.leftval, C.rightval = F, G, 8, 10

print(valuable_sum(A, 3))
