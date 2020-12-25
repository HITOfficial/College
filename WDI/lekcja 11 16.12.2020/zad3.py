# Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna.


# moga sie elementy powtarzac wzajemnie w tych listach

class Node:
    def __init__(self, next_node, value):
        self.next_node = next_node
        self.value = value


def show_nodes(node):
    print(node.value)
    while node.next_node != None:
        print(node.next_node.value)
        node = node.next_node

# gdy dwa elementy beda mialy ta sama wartosc, to biore element z pierwszej listy

# mam elementy z 2 roznych list i porownuje z nich wartosci pod 


# iteracyjnie
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

