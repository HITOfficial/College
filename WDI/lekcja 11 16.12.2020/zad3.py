# Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna.

class Node:
    def __init__(self, next_node, value):
        self.next_node = next_node
        self.value = value


def combine_nodes(node1, node2):
    combined_node = None

    if node1.value > node2.value:
        combined_node = node2
        node2 = node2.next_node
    else:
        combined_node = node1
        node1 = node1.next_node

    first_element = combined_node

    flag = False

    while True:
        if flag:
            combined_node = combined_node.next_node # przy kazdym kolejnym wejsciu przekierowywuje na kolejny element z wezla

        # warunki zeby nie leciec po dwuch wezlach na raz
        if node1 == None and node2 == None:
            break
        
        if node1 == None:
            combined_node.next_node = node2
            node2 = node2.next_node
            flag = True
            continue
        
        if node2 == None:
            combined_node.next_node = node1
            node1 = node1.next_node
            flag = True
            continue

        # iterowanie po ktoryms z 2 wezlow
        if node1.value == node2.value:
            combined_node.next_node = node1
            node1 = node1.next_node # dubluja sie wartosci wiec kieruje na jeden wyznacznik wezel, i przesuwam w obydwuch na kolejny element
            node2 = node2.next_node
            flag = True


        elif node1.value < node2.value:
            combined_node.next_node = node1
            node1 = node1.next_node
            flag = True
        
        else:
            combined_node.next_node = node2
            node2 = node2.next_node
            flag = True

    return first_element

# modele testowe
# node1 = Node(Node(None,14), 1)
# node2 = Node(Node(Node(None,12),11), 7)
# print(show_nodes(combine_nodes(node1, node2)))


# College
class Node:
    def init(self, value, next_one):
        self.value = value
        self.next = None

#Iteration

def concatenate(f1,f2): # wskaznik1, wskaznik2
    f = None

    if f1.value < f2.value:
        f = f1
        f1 = f1.next
    else:
        f = f2
        f1 = f1.next # przeskakuje na kolejny element z listy wskaznikowej

    first_element = f

    while f1 != None and f2 != None:
        if f1.value < f2.value:
            f = f1
            f1 = f1.next

        else:
            f = f2
            f2 = f2.next # przeskakuje na kolejny element z listy wskaznikowej

        f = f.next
    # jedna z wezlow sie skonczyl
    
    if f1 != None:
        f = f1
    else:
        f = f1

    return first_element    


#Recursion

def concatenate_rec(l1, l2): # wezel1, wezel2
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    
    if l1.value < l2:
        res = l1
        res.next = concatenate_rec(l1.next, l2)
    else:
        res = l1
        res.next = concatenate_rec(l1.next, l2)
        
    return res