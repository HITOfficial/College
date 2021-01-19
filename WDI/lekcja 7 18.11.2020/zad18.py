# Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy
# unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy.

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


# jeżeli istnieje juz taki element w węźle to usuwam wszystkie elementy włącznie z pierwszym

el5 = Node(2, None)
el4 = Node(3, el5)
el3 = Node(2, el4)
el2 = Node(4, el3)
el1 = Node(2, el2)


def print_vals(node):
    while node != None:
        print(node.value)
        node = node.next

# print_vals(el1)

def unique_node(node):
    if node == None:
        return None
    if node.next == None: # nie ma elementów
        return node

    first = node
    a = node
    a_prev = None
    n = a.next
    n_prev = a

    while a is not None:
        n_prev = a # ustaiwam na nowo wskazniki
        n = a.next
        flag = False # oflaguje jesli bede musiał wyrzucić aktualny el z listy

        while n is not None:
            if n.value == a.value:
                flag = True
                n = n.next
                if n is None: # sprawdzam dodatkowo, czy to nie był to czasem ostatni element w liście
                    n_prev.next = None
            else:
                n_prev.next = n
                n_prev = n_prev.next
                n = n.next

        if flag: # wartosc sie powtorzyla
            a = a.next
            if a_prev is None: # musze actual odlaczyc od listy ale stal on na pierwszym miejscu w liscie
                first = a

        else: # przesuwam poprzedni wskaznik na aktualnie sprawdzane a
            if a_prev is None: # nie było poprzedniego wskaznika więc teraz dopiero po raz pierwszy go ustawiam
                a_prev = a
            else:
                a_prev.next = a
                a_prev = a_prev.next # przesuwam się poprzednim znacznikiem
            a = a.next
            
        
    return first


print_vals(unique_node(el1))
        
            
    

            


