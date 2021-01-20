class Node:
    def __init__(self, value, next):
            self.value = value
            self.next = next


el5 = Node('w', None)
el4 = Node('o', el5)
el3 = Node('m', el4)
el2 = Node('c', el3)
el1 = Node('b', el2)


def updated_set(n, word):
    updated= False
    for single_letter in word:
        node = n
        while node is not None:
            if ascii(node.value) == ascii(single_letter):
                break
            elif ascii(node.value) < ascii(single_letter) and ascii(node.next.value) > ascii(single_letter): # wryraz pośrodku
                node.next = Node(single_letter, node.next) # tworzę nowy element w węźle
                updated = True
            elif node.next is None and ascii(node.value) < ascii(single_letter): # dodaje na koniec
                node.next=  Node(single_letter, None)
                updated = True
            elif ascii(node.value) > ascii(word): # wstawiam na sam początek
                n = Node(single_letter, n)
                updated = True
                break
            node = node.next

    return updated


print(updated_set(el1,'testoweslowo'))
