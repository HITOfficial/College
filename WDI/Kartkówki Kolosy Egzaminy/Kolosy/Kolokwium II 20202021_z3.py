class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next

# Lista zawierała wartości stanowiące kolejne wyrazy ciągu arytmetycznego. Z wnętrza listy usunięto
# pewną liczbę elementów. Proszę napisać funkcję repair(p), (p wskazuje na pierwszy element listy) która
# uzupełnia listę elementami, tak aby ponownie zawierała kolejne wyrazy ciągu arytmetycznego. Funkcja
# powinna zwrócić liczbę wstawionych elementów

# na początku przelecę po wszystkich elementach mierząc poprzedni i następny i na tej podstawie, oszaczuję najmniejszą różnicę, <- i będzie to ta szukana różnica arytmetyczna

def show_values(node):
    while node is not None:
        print(node.val)
        node = node.next


def repair(p):
    difference = 1_000 # zakładam że znaleziona róznica w ciągu będzie mniejsza
    first_node = p

    while p.next is not None:
        difference = min(difference, abs(p.val - p.next.val)) # szukam najmniejszej różnicy
        p = p.next

    p = first_node # przerzucam z powrotem wskaznik na 1wszy el
    next_node = p.next
    while next_node is not None:
        if p.val < next_node.val: # ciąg arytm. rosnący
            while p.val + difference is not next_node.val: # dokładam elementy do ciągu
                node_to_insert = Node(p.val+difference, next_node) # tworzę nowy element do podciągu
                p.next = node_to_insert
                p = node_to_insert
        if p.val > next_node.val: # ciąg arytm. malejacy
            while p.val - difference is not next_node.val: # dokładam elementy do ciągu
                node_to_insert = Node(p.val-difference, next_node)
                p.next = node_to_insert
                p = node_to_insert

        next_node = next_node.next # tutaj juz mam dopełniony ciąg arytm, więc przerzuca się na wypełnianie kolejnych miejsc 
    
    return first_node
        

# el testowe na rosnacy
el5 = Node(31,None)
el4 = Node(15,el5)
el3 = Node(7,el4)
el2 = Node(5,el3)
el1 = Node(1,el2)
# el testowe na malejacy
al5 = Node(3,None)
al4 = Node(6,al5)
al3 = Node(9,al4)
al2 = Node(21,al3)
al1 = Node(24,al2)


print(show_values(repair(el1)))
print(show_values(repair(al1)))