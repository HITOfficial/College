# # Zastosowanie listy odsyłaczowej do implementacji
# # tablicy rzadkiej. Proszę napisać trzy funkcje:
# # – inicjalizującą tablicę,
# # – zwracającą wartość elementu o indeksie n,
# # – podstawiającą wartość value pod indeks n.

class Node:
    def __init__(self, next_one=None, value=0, index=0):
        self.next_one = next_one    
        self.value = value    
        self.index = index



def value_under_index(node, index):
    while node != None:
        if node.index == index:
            return node.value

        node = node.next_one

    return -1 # zwracam wartosc -1 jesli nie znajdzie takiego indexu


def adding_value_under_index(node, value, index):
    while node != None:
        if node.index == index:
            node.value = value
            return
            
        node = node.next_one

    return -1 # gdy nie znajdzie elementu pod takim indexem