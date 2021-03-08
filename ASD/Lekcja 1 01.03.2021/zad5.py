#(odwracanie listy) Proszę zaimplementować funkcję odwracającą listę jednokierunkową.

class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next


def reverse_node(L): # lista od razu z wartownikiem
    first = L # pobieram tego samego wartownika
    L = L.next # przeskakuje poza wartownika
    a = None # zakończenie wskaznika
    while L is not None:
        L_next = L.next
        L.next = a
        a = L
        L = L_next
    first.next = a
    return first


def show_nodes(L):
    while L is not None:
        if L.value is not None:
            print(L.value)   
        L = L.next

        
a1 = Node(5)
a2 = Node(4,a1)
a3 = Node(3,a2)
a4 = Node(2,a3)
a5 = Node(1,a4)
a6 = Node(0,a5)
a7 = Node(-1,a6)
a8 =Node(None, a7)


print(show_nodes(reverse_node(a8)))

