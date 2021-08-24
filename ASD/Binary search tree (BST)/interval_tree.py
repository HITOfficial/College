# interval tree, common sequence if has at lest endings the same

# simple interval tree structure on  balanced bfs tree
# returning common intervals arrays, for every interval

# complexity:
# - time O(NlogN) / O(H-L), where H is the highest number in range array, and L lowest
# space O(H-L)


class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.intervals = []
        self.min = val
        self.max = val


def unique_array(array):
    min_el, max_el = float("inf"), -float("inf")
    for b, e in array:
        if b < min_el:
            min_el = b
        if e > max_el:
            max_el = e
    range_array = [False]*(max_el-min_el+2)
    for b, e in array:
        range_array[b-min_el] = True
        range_array[e-min_el] = True
    unique = []
    for val in range(max_el-min_el+2):
        if range_array[val]:
            unique.append(val+min_el)
    return unique


def create_BBST(array, l, r, parent=None):
    if l > r:
        return None
    m = (l+r)//2
    p = Node(array[m])
    p.left = create_BBST(array, l, m-1, p)
    p.right = create_BBST(array, m+1, r, p)
    if parent is not None:
        # parent is has lower value
        if parent.val < p.val:
            p.min = parent.val
            if p.right is not None:
                p.max = p.right.max
        # parent has greater
        else:
            p.max = parent.val
            if p.left is not None:
                p.min = p.left.min
    # root element
    else:
        if p.left is not None:
            p.min = p.left.min
        if p.right is not None:
            p.max = p.right.max
    return p


def BBST_sorted_ranges_array(array):
    l = 0
    r = len(array)-1
    root = create_BBST(array, l, r)
    return root


def add_interval(node, l, r):
    flag = False
    if node is not None:
        if r < node.min or l > node.max:
            return False
        flag1 = add_interval(node.left, l, r)
        flag2 = add_interval(node.right, l, r)
        flag = flag1 or flag2
        if flag is False and node.min >= l and node.max <= r:
            node.intervals.append((l, r))
            flag = True
    return flag


def update_max(node, val):
    if node is not None:
        if node.right is not None:
            update_max(node.right, val)
        else:
            node.max = val


def update_min(node, val):
    if node is not None:
        if node.left is not None:
            update_min(node.left, val)
        else:
            node.min = val


# creating fake leafs on all leafs in Balanced BST, without:
# - left fake leaf in min value leaf
# - right fake leaf in max value leaf
def fake_leafs(node):
    if node is None:
        return
    fake_leafs(node.left)
    fake_leafs(node.right)
    # left fake leaf
    if node.left is None and node.min != node.val:
        p = Node()
        p.min = node.min
        p.max = node.val
        node.left = p
    # right fake leaf
    if node.right is None and node.val != node.max:
        p = Node()
        p.min = node.val
        p.max = node.max
        node.right = p


def interval_tree(array):
    root = BBST_sorted_ranges_array(unique_array(array))
    # alg. doesn't correctly update root previous node max value and root next node min value
    update_max(root.left, root.val)
    update_min(root.right, root.val)
    # addding two fake leafs to every leaf in actual structure
    fake_leafs(root)
    # adding all intervals into structure
    for l, r in array:
        add_interval(root, l, r)
    return root


def common_interval(node, l, r):
    intervals = []
    if node is not None:
        if r < node.min or l > node.max:
            return []
        left_intervals = common_interval(node.left, l, r)
        right_intervals = common_interval(node.right, l, r)
        if node.left is None and node.right is None:
            intervals = node.intervals
        intervals += left_intervals + right_intervals
    return intervals


def remove_duplicates(array):
    # duplicate array
    n = len(array)
    duplicate = [False]*len(array)
    for i in range(n-1):
        for j in range(i+1, n):
            if array[j] == array[i]:
                duplicate[j] = True
    unique = [array[i] for i in range(n) if not duplicate[i]]
    return unique


def common_intervals(array):
    # creating interval tree structure
    tree = interval_tree(array)
    intervals = []
    for l, r in array:
        intervals.append(common_interval(tree, l, r))
    unique_intervals = []
    for i, intervals_array in enumerate(intervals):
        # removing all duplicates in O(K^2), where k is an number of intervals with duplicates
        unique_intervals.append(remove_duplicates(intervals_array))
        unique_intervals[i].remove(array[i])
        # removing element for whose alg. found common intervals
    return unique_intervals


array = [(15, 20), (5, 20), (17, 19), (12, 15), (30, 40)]
array = [(0, 10), (5, 20), (7, 12), (10, 15), (15, 20)]


print(common_intervals(array))
