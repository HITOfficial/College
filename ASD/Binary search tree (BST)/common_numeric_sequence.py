from math import log2, ceil

# complexity:
# - time O(logN) answer on one query / O(QlogN) / O(N) -> 4N, building a tree, Q, where q is a nuber of queries
# - space O(N) -> 4N, building a common range tree


def build_common_numeric_sequence_tree(subsequence, array, n, index, l, r):
    if l >= n:
        return
    # single leaf
    if l == r:
        subsequence[index] = array[l]
    else:
        m = (l+r)//2
        lch, rch = (2*index)+1, (2*index)+2
        # left child
        build_common_numeric_sequence_tree(subsequence, array, n, lch, l, m)
        # right child
        build_common_numeric_sequence_tree(subsequence, array, n, rch, m+1, r)
        # updating node value by min value of his children
        # condition if have common range
        if subsequence[lch][0] > subsequence[rch][1]:
            return
        elif subsequence[lch][1] < subsequence[rch][0]:
            return
        else:
            subsequence[index] = (max(subsequence[lch][0], subsequence[rch][0]), min(
                subsequence[lch][1], subsequence[rch][1]))


def query_common_numeric_sequence(subsequence, ql, qr, l, r, idx=0):
    if ql <= l and qr >= r:
        # range from query is greater or equal, so can use best value from indexes [l,r]
        return subsequence[idx]
        # out of range to look
    elif qr < l or ql > r:
        return None
    m = (l+r)//2
    lch, rch = (2*idx)+1, (2*idx)+2
    subsequence_left = query_common_numeric_sequence(
        subsequence, ql, qr, l, m, lch)
    subsequence_right = query_common_numeric_sequence(
        subsequence, ql, qr, m+1, r, rch)
    # condition hasn't common subsequence
    if subsequence_left is subsequence_right is None:
        return (-float("inf"), -float("inf"))
    elif subsequence_right is None:
        return subsequence_left
    elif subsequence_left is None:
        return subsequence_right
    else:
        # hasn't common part
        if subsequence_left[0] > subsequence_right[1] or subsequence_right[0] > subsequence_left[1]:
            return (-float("inf"), -float("inf"))
        else:
            return (max(subsequence_left[0], subsequence_right[0]), min(
                subsequence_left[1], subsequence_right[1]))


def common_subsequence(array, queries):
    n = len(array)
    subsequence = [(-float("inf"), -float("inf"))]*(4*n)
    # indexes starting from 0 from this reason right range -1
    idx, l, r = 0, 0, 2**ceil(log2(n))-1
    build_common_numeric_sequence_tree(subsequence, array, n, idx, l, r)
    ansers = []
    for ql, qr in queries:
        answer = query_common_numeric_sequence(subsequence, ql, qr, l, r)
        # hasn't common part
        if answer is not None and answer[0] == answer[1]:
            answer = None
        ansers.append(answer)
    return ansers


array = [(0, 4), (-1, 2), (1, 3), (1, 2), (0, 7), (3, 9), (5, 8)]
queries = [(1, 4), (4, 5), (6, 8)]

print(common_subsequence(array, queries))
