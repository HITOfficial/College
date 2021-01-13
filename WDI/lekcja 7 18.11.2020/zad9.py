class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

a = Node(9,None, None)
b = Node(9,None, None)
c = Node(9,None, None)
a.next = b
b.next = c
b.prev = a
c.prev = b

def print_nodes(node):
    while node != None:
        print(node.value, end='')
        node = node.next
    return '' # zeby nie zwracalo None na końcu



def node_plus_one(node): # node
    first = node
    while node.next != None: # dochodzę do ostatniego elementu
        node = node.next

    if node.value != 9: # dodaję na koniec
        node.value += 1
        return first

    while node.value == 9 and node.prev != None:
        node = node.prev

    # nie doszło do pierwszego elementu
    if node.prev != None:
        node.value += 1
        return first
    elif node.value != 9: # pierwszy element mniejszy niz 9
        node.value += 1
        return node
    else: # pierwszy element 9
        first = Node(1,node,None)
        node.prev = first
        return first


print(print_nodes(node_plus_one(a)))

