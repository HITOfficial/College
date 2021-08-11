# inspirations:
# https://www.youtube.com/watch?v=-dUiRtJ8ot0
# https://medium.com/nybles/understanding-range-queries-and-updates-segment-tree-lazy-propagation-and-mos-algorithm-d2cd2f6586d8
# https://cp-algorithms.com/data_structures/segment_tree.html

from math import ceil, log2

# complexity:
# - time O(logN) answer on one query / O(QlogN) / O(N) -> 4N, building a tree, Q, where q is a nuber of queries
# - space O(N) -> 4N, building a segment tree


# segment tree on normal python list not on a Node list
# bottom up -> updating data, during creating tree
def build_min_tree(tree, array, n, index,  l, r):
    # out of range to take single leaf
    if l >= n:
        return
    # single leaf
    elif l == r:
        tree[index] = array[l]
    else:
        m = (l+r)//2
        l_child = (2*index)+1
        r_child = (2*index)+2
        # left child
        build_min_tree(tree, array, n, l_child, l, m)
        # right child
        build_min_tree(tree, array, n, r_child, m+1, r)
        # updating node value by min value of his children
        tree[index] = min(tree[l_child], tree[r_child])


def query_min(tree, query_l, query_r, l, r, index=0):
    # node 0 in tree contains min value from range [0,n-1]
    # left child [0,(n-1)//2]
    # right child [(n-1)//2+1,n-1] etc...
    # actual range is inside query range
    if query_l <= l and query_r >= r:
        # range from query is greater or equal, so can use best value from indexes [l,r]
        return tree[index]
        # out of range to look
    elif query_r < l or query_l > r:
        return float("inf")
    else:
        m = (l+r)//2
        min_left = query_min(tree, query_l, query_r, l, m, 2*index+1)
        min_right = query_min(tree, query_l, query_r, m+1, r, 2*index+2)
    return min(min_left, min_right)


def min_segment_tree(array, queries):
    n = len(array)
    tree = [float("inf")]*(4*n)
    # while alg, build tree number of nodes need to be ceil to nearlest power of 2
    l, r = 0, (2**ceil(log2(n)))-1
    build_min_tree(tree, array, n, 0, l, r)
    for b, e in queries:
        print(query_min(tree, b, e, l, r))


array = [8, 2, 5, 1, 4, 5, 3, 9, 6, 10]
queries = [(1, 3), (0, 6), (2, 4), (14, 15)]

print(min_segment_tree(array, queries))
