class MakeSet:
    def __init__(self, value, rank=0):
        self.value = value
        self.rank = rank
        self.parent = self


def make_set(value):
    return MakeSet(value)


def find(node): # finding first parent from tree, can create not equal two branches tree
    if node != node.parent:
        node.parent = find(node.parent)
    return node.parent


def union(tree1,tree2):
    tree1 = find(tree1)
    tree2 = find(tree2)
    if tree1 == tree2: # the same tree
        return
    
    if tree1.rank > tree2.rank: # first tree is higher
        tree1.rank += 1 # one more level of tree length
        tree2.parent = tree1
    elif tree1.rank == tree2.rank: # same level of trees
            tree2.parent = tree1
    else: # adding first tree to second one
        tree2.rank += 1
        tree1.parent = tree1


def union(tree1,tree2):
    tree1 = find(tree1)
    tree2 = find(tree2)
    if tree1 == tree2: # the same tree
        return False
    
    if tree1.rank > tree2.rank: # first tree is higher
        tree1.rank += 1 # one more level of tree length
        tree2.parent = tree1
    elif tree1.rank == tree2.rank: # same level of trees
            tree2.parent = tree1
    else: # adding first tree to second one
        tree2.rank += 1
        tree1.parent = tree1
    return True

