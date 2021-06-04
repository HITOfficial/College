class BST_Node:
    def __init__(self,key,parent=None,left=None,right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


def find(actual,key):
    if actual is None:
        return None
    if actual.key == key:
        return actual
    elif actual.key > key:
        return find(actual.left, key)
    else:
        return find(actual.right, key)


def insert(actual,key):
    if actual.key == key: # duplicate
        return
    elif actual.key > key: # left child
        if actual.left is not None:
            insert(actual.left, key)
        else:
            actual.left = BST_Node(key,actual)
    else :
        if actual.right is not None:
            insert(actual.right, key) # right
        else:
            actual.right = BST_Node(key,actual)
    

def minimum(actual):
    if actual.left is not None:
        return minimum(actual.left)
    else:
        return actual


def maximum(actual):
    if actual.right is not None:
        return maximum(actual.right)
    else:
        return actual

def previous(actual,key):
    actual = find(actual,key)
    if actual is not None: # this element is in set
        if actual.left is not None:
            return maximum(actual.left)
        if actual.parent is not None:
            if actual.parent.right is actual: # right child -> returning parent
                return actual.parent
            while actual.parent is not None and not actual.parent.right is actual:
                actual = actual.parent
            if actual.parent:
                return actual.parent


def next(root, key): # root from tree, next element of key
    actual = find(root,key)
    if actual is not None: # key is in tree
        if actual.right is not None:
            return minimum(actual.right) # returning tulpe, object in memory, value 
        while actual.parent is not None and not actual.parent.left is actual: # right child, so move up until not being left children
            actual = actual.parent
        if actual.parent:
            return actual.parent


root = BST_Node(21)
insert(root,15)
insert(root,5)
insert(root,7)
insert(root,13)
insert(root,8)
insert(root,20)
insert(root,37)
insert(root,25)
insert(root,22)
insert(root,40)
insert(root,38)


print(previous(root,20).key)