# 2/2 points exercise 1.

# complexity:
# time: O(N)
# memory: O(N)


class Node:
    def __init__( self ):
        self.left    = None
        self.right   = None
        self.parent  = None
        self.value   = None


def minimum(actual):
    if actual.left is not None:
        return minimum(actual.left)
    else:
        return actual
        

def next(actual):
    if actual.right is not None:
        return minimum(actual.right)
    while actual.parent is not None and not actual.parent.left is actual:
        actual = actual.parent
    if actual.parent:
        return actual.parent


def ConvertTree(p):
    p = minimum(p)
    stack = []
    while p is not None:
        stack.append(p)
        p = next(p)

    n = len(stack)
    for i in range((n+2)//2):
        left = 2*i+1
        right = 2*i+2
        if left < n:
            stack[i].left = stack[left]
            stack[left].parent =stack[i]
            stack[left].left = None
            stack[left].right = None
        if right < n:
            stack[i].right = stack[right]
            stack[right].parent =stack[i]
            stack[right].left = None
            stack[right].right = None
    return stack[0]