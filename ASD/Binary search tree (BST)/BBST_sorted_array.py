# balanced BST from sorted array

# complexity:
# - time O(N)
# - space O(N) -> stack size


class Node:
    def __init__(self, val):
        self.val = val
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


array = [0, 5, 7, 10, 11, 12, 15, 20]

print(BBST_sorted_array(array))
