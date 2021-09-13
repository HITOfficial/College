# Given is an array A referenced by n = len (A) of numerical numbers. Additionally, it is known that A in total
# contains k different numbers (assume k is much less than n). Please implement
# complete function (A, which returns the length of the longest k .in in a string of elements
# from array A where not all k numbers are. (It can be assumed that the given value of k is always correct.)

#  complexity:
# - time O(N^2*K) / O(N^2logK) -> I don't know way to copy full tree structure in O(1) -> than O(N*K), another O(NlogK) checking number of used times value in Balanced binary search
# - space O(N)


class Node:
    def __init__(self, val):
        self.val = val
        self.used = False
        self.left = None
        self.right = None


# Creating Balanced Binary search tree from sorted array (which will work like hash table) -> copied from templates
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


def tree_update_k(node, val):
    if node.val == val:
        if not node.used:
            # memorizing once more using
            node.used = True
            return True
        else:
            # used k times value in actual incomplete
            return False
    elif node.val > val:
        return tree_update_k(node.left, val)
    else:
        return tree_update_k(node.right, val)


# reseting booleans of every used element
def refresh_tree(node):
    if node is None:
        return
    refresh_tree(node.left)
    refresh_tree(node.right)
    node.used = False


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
    # creating balanced BST -> with counters to memorize if number was used
    K_tree = BBST_sorted_array(B)

    longest = 0
    # trying to find every longest subsequence starting from 0...n-1 element
    for i in range(n):
        K_tree = BBST_sorted_array(B)
        actual, actual_k = 0, 0
        for j in range(i, n):
            if tree_update_k(K_tree, A[j]):
                actual_k += 1
                if actual_k == k:
                    # reseting data and finding new longest subsequence, and adding actual element into new subsequence
                    actual, actual_k = 1, 1
                    refresh_tree(K_tree)
                    tree_update_k(K_tree, A[j])
                    continue
            actual += 1
            longest = max(actual, longest)
    return longest


A = [1, 100, 5, 100, 1, 5, 1, 5]
k = 3
print(longest_incomplete(A, k))
