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


def delete(root,key): # deleting node, not replecing values
    actual = find(root,key)
    if not actual.left and not actual.right: # single leaf
        if actual.parent is not None:
            if actual.parent.left is actual:
                actual.parent.left = None 
            else:
                actual.parent.right = None
        return None # empty tree

    elif actual.left and not actual.right: # node has only left branch
        if actual.parent is not None:
            actual.left.parent = actual.parent
            if actual.parent.left is actual:
                actual.parent.left = actual.left
            else:
                actual.parent.right = actual.left
        else: # removing root
            actual.left.parent = None
        return actual.left

    elif actual.right and not actual.left: # only right branch
        if actual.parent is not None:
            actual.right.parent = actual.parent
            if actual.parent.left is actual: # element to remove is a left branch of parent
                actual.parent.left = actual.right
            else:
                actual.parent.right = actual.right
        else:
            actual.right.parent = None # removing root element
        return actual.right

    else: # actual element has two two branches
        new = next(actual,actual.key) # searching for next value element in tree
        parent = actual.parent
        if actual.parent is not None: # not single element in branch
            if parent.left is actual: # element to remove is a left children
                parent.left = new
            else:
                parent.right = new

            new.left = actual.left # replacing branches from actual to new node
            if actual.right is not new: # element with next value in BST was not from single leaf
                new.parent.left = None # removing previous parent from next elemnt in BST
                new.right = actual.right
                actual.right.parent = new
            new.parent = actual.parent # new parent
            return root

        else: # deleting element is a root in BST
            new.parent.left = None
            new.left = actual.left
            new.right = actual.right
            return new 


def BST_keys(actual):
    if actual is None:
        return []
    else:
        array = [actual.key]
        array.extend(BST_keys(actual.left))
        array.extend(BST_keys(actual.right))
        return array


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
insert(root,28)

root = delete(root,21)
x = find(root,37)

print(BST_keys(root))
print(BST_keys(x))