# 1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
# struktury listy odsyłaczowej.
# - czy element należy do zbioru
# - wstawienie elementu do zbioru
# - usunięcie elementu ze zbioru

# zrobione na podstawie imitacji stosu
class Node: # węzeł jednostronny
    def __init__(self, prev_node=None, value=0):
        self.prev_node = prev_node
        self.value = value


node = Node()


def element_in_node(node, searching_val):
    if node.prev_node != None:
        if node.value == searching_val:
            return True
        return element_in_node(node.prev_node, searching_val)
    return False


def add_element_to_node(node, value): # dodaje na początek węzłu 
    if node.prev_node == None:
        node.prev_node = Node(None, value) # tworzę nowy element węzłu na początku i dodaję w nim wartość 
    else:
        add_element_to_node(node.prev_node, value)


def remove_first_element_from_node(node, preview= None): # usuwa element z początku węzła 
    if node.prev_node == None:
        preview.prev_node = None # zakańczam węzeł na przedostatnim elemencie z początku
    else:
        remove_first_element_from_node(node.prev_node, node)


