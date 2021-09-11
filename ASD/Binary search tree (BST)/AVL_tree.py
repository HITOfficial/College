# inspirations:
#  https://www.youtube.com/watch?v=jDM6_TnYIqE
#  https://www.programiz.com/dsa/avl-tree


# struckture has not a delete function

class Node():
    def __init__(self, value=None, height=0, l_child=None, r_child=None):
        self.value = value
        self.height = height
        self.l_child = l_child
        self.r_child = r_child


def LL_rotation(root, a):
    # checking if rotating root element
    flag = False
    if root == a:
        flag = True
    b, c = a.l_child, a.r_child
    d, e = b.l_child, b.r_child
    b.l_child, b.r_child = d, a
    a.l_child, a.r_child = e, c
    # updating height after rotations
    update_height(a), update_height(b)
    if flag:
        return b
    else:
        return root


def LR_rotation(root, a):
    # checking if rotating root element
    flag = False
    if root == a:
        flag = True
    b, c = a.l_child, a.r_child
    d, e = b.l_child, b.r_child
    f, g = e.l_child, e.r_child
    e.l_child, e.r_child = b, a
    b.l_child, b.r_child = d, f
    a.l_child, a.r_child = g, c
    update_height(b), update_height(a), update_height(e)
    if flag:
        return e
    else:
        return root


def RR_rotation(root, a):
    # checking if rotating root element
    flag = False
    if root == a:
        flag = True
    b, c = a.l_child, a.r_child
    d, e = c.l_child, c.r_child
    a.l_child, a.r_child = b, d
    c.l_child, c.r_child = a, e
    update_height(a), update_height(c)
    if flag:
        return c
    else:
        return root


def RL_rotation(root, a):
    # checking if rotating root element
    flag = False
    if root == a:
        flag = True
    b, c = a.l_child, a.r_child
    d, e = c.l_child, c.r_child
    f, g = d.l_child, d.r_child
    a.l_child, a.r_child = b, f
    c.l_child, c.r_child = g, e
    d.l_child, d.r_child = a, c
    update_height(a), update_height(c), update_height(d)
    if flag:
        return d
    else:
        return root


def find(actual, pivot):
    if actual is None:
        return False
    elif actual.value == pivot:
        return True
    elif actual.value > pivot:
        return find(actual.l_child, pivot)
    else:
        return find(actual.r_child, pivot)


def insert(root=None, node=None, value=None):
    # inserting to AVL tree only unique values
    if node is None:
        return Node(value)
    if root is node:
        if find(root, value):
            # this value is already in AVL tree
            return node
    # finding place to insert element O(logN)
    if node.value > value:
        if node.l_child is None:
            node.l_child = Node(value)
        else:
            insert(root, node.l_child, value)
    else:
        if node.r_child is None:
            node.r_child = Node(value)
        else:
            insert(root, node.r_child, value)
    # updating height of every bactracking level, and checking if is AVL tree
    update_height(node)
    return balance(root, node)


def update_height(node):
    l_height = abs(get_height(node.l_child))+1
    r_height = get_height(node.r_child)
    # from right child height need to be negative
    if r_height > 0:
        r_height *= (-1)
        r_height -= 1
    if l_height == abs(r_height):
        node.height = 0
    elif l_height > abs(r_height):
        node.height = l_height-r_height
    else:
        node.height = r_height+l_height


def get_height(node):
    if node is None:
        return 0
    else:
        return node.height


def balance(root, node):
    # balance factor
    bf = node.height
    # after some updates, this node subtree has still AVL structure
    if abs(bf) <= 1:
        return root

    if bf >= 2:
        if node.l_child.height >= 1:
            # left left rotation
            root = LL_rotation(root, node)
        else:
            # left right rotation
            root = LR_rotation(root, node)
    else:
        if node.r_child.height <= -1:
            root = RR_rotation(root, node)
        else:
            root = RL_rotation(root, node)
    return root


def create_AVL_tree(array):
    node = None
    for pivot in array:
        node = insert(node, node, pivot)
    return node


array = [20, 15, 25, 10, 18, -10]

print(create_AVL_tree(array))
