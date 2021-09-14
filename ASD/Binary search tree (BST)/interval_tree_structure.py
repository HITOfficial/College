# complexity:
# - creating tree O(NlogN)
# - answering on eqery query:  KlogN
# - adding single interval O(logN)
# - removing single interval O(logN)
# - space: O(N*L) where L is a number of queries

class Node:
    def __init__(self):
        self.mid = None
        self.left = None
        self.right = None
        self.intervals = []
        self.lchild = None
        self.rchild = None
        self.leaf = False


def remove_duplicates(A):
    A_tuple_upacked = []
    for a, b in A:
        A_tuple_upacked.append(a)
        A_tuple_upacked.append(b)
    A_tuple_upacked.sort()
    A_removed_duplicates = [A_tuple_upacked[0]]
    idx = 0
    for val in A_tuple_upacked:
        if val == A_removed_duplicates[idx]:
            continue
        else:
            A_removed_duplicates.append(val)
            idx += 1
    return A_removed_duplicates


def build_tree(A, i, j, left, right):
    node = Node()
    node.left = left
    node.right = right
    # leaf
    if (i > j):
        node.mid = -1
        node.leaf = True
    else:
        # build internal node
        m = (i+j)//2
        node.mid = A[m]
        node.lchild = build_tree(A, i, m - 1, left, A[m])
        node.rchild = build_tree(A, m + 1, j, A[m], right)
    return node


# intervals which have common point
def intervals_common_point(node, point, flag_left=False, flag_right=False):
    # intervals with common point are in two subtrees:
    if node.mid == point:
        return node.intervals[:]
    elif node.mid > point:
        return node.intervals[:] + intervals_common_point(node.lchild, point)
    elif node.mid < point:
        return node.intervals[:] + intervals_common_point(node.rchild, point)
    else:
        return node.intervals


def insert_interval(node, interval):
    l, r = interval
    # node interval range is lower, so this interval can be in him
    if node.left >= l and node.right <= r:
        node.intervals.append(interval)
        return
    # part of interval will be append into left side
    if l < node.mid:
        insert_interval(node.lchild, interval)
    if r > node.mid:
        insert_interval(node.rchild, interval)


def remove_interval(node, interval):
    l, r = interval
    # node interval range is lower, so this interval can be in him
    if node.left >= l and node.right <= r:
        node.intervals.remove(interval)
        return
    # part of interval to remove is in the left children
    if l < node.mid:
        insert_interval(node.lchild, interval)
    # part of interval to remove is in the right children
    if r > node.mid:
        insert_interval(node.rchild, interval)


def interval_tree(A, queries):
    A_without_duplicates = remove_duplicates(A)
    # creating tree with interval [min-1,max+1]
    tree = build_tree(A_without_duplicates, 0, len(A_without_duplicates)-1,
                      min(A_without_duplicates)-1, max(A_without_duplicates)+1)
    # adding intervals into built tree
    for interval in A:
        insert_interval(tree, interval)
    # to answer on questions: all intervals (a,b) which contains p point:
    ans = []
    for k in queries:
        ans.append(intervals_common_point(tree, k))

    return ans


A = [(1, 3), (5, 6), (4, 7), (6, 9), (3, 5)]
# points in querry must be between min and max from points in A array
query = [1, 5, 6]
print(interval_tree(A, query))
