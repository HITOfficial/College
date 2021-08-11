from math import ceil, log2


# complexity:
# - time O(logN) answer on one query / O(QlogN) -> answer on Q queries / O(N) -> 4N, building a tree
# - space O(N) -> 4N, building a segment tree


def build_sum_tree(tree, array, n, index,  l, r):
    if l >= n:
        return
    elif l == r:
        tree[index] = array[l]
    else:
        m = (l+r)//2
        l_child = (2*index)+1
        r_child = (2*index)+2
        build_sum_tree(tree, array, n, l_child, l, m)
        build_sum_tree(tree, array, n, r_child, m+1, r)
        tree[index] = tree[l_child] + tree[r_child]


def query_sum(tree, query_l, query_r, l, r, index=0):
    if query_l <= l and query_r >= r:
        return tree[index]
    elif query_r < l or query_l > r:
        return 0
    else:
        m = (l+r)//2
        sum_left = query_sum(tree, query_l, query_r, l, m, 2*index+1)
        sum_right = query_sum(tree, query_l, query_r, m+1, r, 2*index+2)
    return sum_left + sum_right


def sum_segment_tree(array, queries):
    n = len(array)
    tree = [0]*(4*n)
    # while alg, build tree number of nodes: single leafs need to be ceil to nearlest power of 2
    l, r = 0, (2**ceil(log2(n)))-1
    build_sum_tree(tree, array, n, 0, l, r)
    for b, e in queries:
        print(query_sum(tree, b, e, l, r))


array = [8, 2, 5, 1, 4, 5, 3, 9, 6, 10]
# sum of elements from range [l,r] in array
queries = [(1, 3), (0, 6), (2, 4), (14, 15)]

print(sum_segment_tree(array, queries))
