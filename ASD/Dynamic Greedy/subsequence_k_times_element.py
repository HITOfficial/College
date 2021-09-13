# Problem: longest subsequence -> in which every elements can be maximal K-1 times

#  complexity:
# - time O(N*K) / O(NlogK) -> I don't know way to copy full tree structure in O(1) -> than O(N*K), another O(NlogK) checking number of used times value in Balanced binary search
# - space O(N)


class Node:
    def __init__(self, val):
        self.val = val
        self.k = 0
        self.left = None
        self.right = None


def create_BBST(array, l, r):
    if l > r:
        return None
    m = (l+r)//2
    p = Node(array[m])
    p.left = create_BBST(array, l, m-1)
    p.right = create_BBST(array, m+1, r)
    return p


def BBST_sorted_array(array):
    l = 0
    r = len(array)-1
    root = create_BBST(array, l, r)
    return root


def tree_update_k(node, k, val):
    if node.val == val:
        if node.k+1 < k:
            # memorizing once more using
            node.k += 1
            return True
        else:
            # used k times value in actual incomplete
            return False
    elif node.val > val:
        return tree_update_k(node.left, k, val)
    else:
        return tree_update_k(node.right, k, val)


def reset_K(node):
    if node is None:
        return
    reset_K(node.left)
    reset_K(node.right)
    node.k = 0


def longest_incomplete(A, k):
    n = len(A)
    A_sorted = list(sorted(A))
    # creating array with elements from A array, but without duplicates in O(N)
    B = [A_sorted[0]]
    idx = 0
    for val in A_sorted:
        if B[idx] == val:
            continue
        else:
            B.append(val)
            idx += 1
    # creating balanced BST -> with counters to memorize number of elements used
    K_tree = BBST_sorted_array(B)

    longest, actual = 0, 0
    for i in range(n):
        if tree_update_k(K_tree, k, A[i]):
            actual += 1
            longest = max(actual, longest)
        else:
            actual = 0
            reset_K(K_tree)
    return longest


A = [1, 100, 5, 100, 1, 5, 1, 5]
k = 3
print(longest_incomplete(A, k))
