class BSTNode():
    def __init__(self,key,parent=None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None
        self.size = 1


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
            actual.left = BSTNode(key,actual)
            update_size(actual) # updating all parents
    else :
        if actual.right is not None:
            insert(actual.right, key) # right
        else:
            actual.right = BSTNode(key,actual)
            # while will insert new element should everty time update size of parent node
            update_size(actual) # updating all parents


def update_size(actual): # after insert element updating all parents size by 1
if actual is not None:
    actual.size += 1
    update_size(actual.parent)

   
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
    if actual is None: # element to remove wasn't in tree
        return
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
        if actual is root:
            return actual.left
        else:
            return root

    elif actual.right and not actual.left: # only right branch
        if actual.parent is not None:
            actual.right.parent = actual.parent
            if actual.parent.left is actual: # element to remove is a left branch of parent
                actual.parent.left = actual.right
            else:
                actual.parent.right = actual.right
        else:
            actual.right.parent = None # removing root element
        if actual is root:
            return actual.right
        else:
            return root

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
            new.parent = actual.parent # new parents
            return root

        else: # deleting element is a root in BST
            # replacing  new node to be a root of BST
            new.left = actual.left # connecting left node
            new.left.parent = new
            if actual.right is not new: # right node
                new.right = actual.right
                new.parent.left = None
            new.parent = None
            return new
