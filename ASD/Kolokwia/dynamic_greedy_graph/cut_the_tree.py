from zad2testy import runtests

class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def cut(actual):
    # single leaf
    if actual.left is None and actual.right is None:
        return float("inf")
    # actual Node has single child
    elif actual.left is not None and actual.right is None:
        return min(actual.value,cut(actual.left))
    elif actual.right is not None and actual.left is None:
        return min(actual.value,cut(actual.right))
    # two children on actual level
    else:
        return min(actual.value,cut(actual.left)+ cut(actual.right))


def cutthetree(T):
    # cannot use root value so, i made another recustion function to calculate best option
    return cut(T.left) + cut(T.right)

    
runtests(cutthetree)


