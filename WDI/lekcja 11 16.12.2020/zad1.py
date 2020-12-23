# Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
# struktury listy odsyłaczowej.
# - czy element należy do zbioru
# - wstawienie elementu do zbioru
# - usunięcie elementu ze zbioru

# zeby sie 3mac tendencji programowania obiektowego
class Node:
    def __init__(self, value=0, previous=None, next_one=None):
        self.value = value
        self.previous = previous
        self.next_one = next_one


def add_element(value, node): # wartosc do wstawienia, wezel
    first_node = node # defaultowo wynikiem funkcji bede zwracal pierwszy element z wezla
    node_previous = node # 3mam go, zeby przechowywac w nim wynik przed ostatniego przesuniecia w nodach
    while node.next_one != None and node.value < value: # lape element przed z wezlu
        node_previous = node
        node = node.next_one

    node = node_previous # zatrzymuje przed ostatnia iteracje z while, gdyby sie zmienila

    if node.next_one != None and node.next_one.value == value: # mam juz taka wartosc w wezle
        return node
    
    new_node = Node(value) # wezel ktory bede dodawal

    if node.previous == None and node.value > value: # dodaje na poczatek
        new_node.next_one = node
        node.previous = new_node
        return new_node # defaultowo bede zwracal pierwszy element ze zbioru

    if node.next_one == None: # dodaje na koniec wezla element
        new_node.previous = node
        node.next_one = new_node
        return first_node
    
    new_node.previous = node # dorzucam element pomiedzy dwa wezly
    new_node.next_one = node.next_one
    node.next_one.previous = new_node
    node.next_one = new_node

    return first_node
        
            
def show_nodes(node):
    print(node.value)
    while node.next_one != None:
        print(node.next_one.value)
        node = node.next_one

# show_nodes(node)