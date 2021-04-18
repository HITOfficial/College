class Node:
    def __init__(self,value):
        self.childrens = []
        self.without = -float("inf") # a graph without this element 
        self.within = -float("inf") # a graph within this element
        self.value = value


def within(parent): # including actual element
    if parent.within != -float("inf"):
        return parent.within
    within_parent = parent.value
    for children in parent.childrens:
        children.without = without(children) # eventualy it will firstly modify children
        within_parent += children.without
    else:
        parent.within = within_parent # last element in node
            
    return max(within_parent,without(parent))

def without(parent):
    if parent.without != -float("inf"):
        return parent.within
    without_parent = 0 # without including parent
    for children in parent.childrens:
        children.within = within(children)
        without_parent += children.within
    else:
        parent.without = 0 # last element in node

    return without_parent #better result 


def independet_set(node):
    return max(without(node),within(node))


# test paths
w = Node(60)
y = Node(17)
y.childrens = [w]
x = Node(13)
b = Node(13)
b.childrens = [x,y]
z = Node(19)
c = Node(5)
c.childrens = [z]
u = Node(23)
v = Node(29)
d = Node(11)
d.childrens = [u,v]
a = Node(16)
a.childrens = [b,c,d]

print(independet_set(a))
