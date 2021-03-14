from random import randint, seed


class Node:
    def __init__(self):
        self.next = None
        self.value = None

       
def add_node(node, L=None):
    if L is None:
        return L
    else:
        L.next = node
        L = L.next
        return L


def create_sentinel():
    sentinel = Node()
    return sentinel


def tail(L):
    while L.next is not None:
        L = L.next
    return L


def partition(N):
    L = create_sentinel() # mniejsze
    E = N # równe
    H = create_sentinel() # większe
    L_tail, E_tail, H_tail = L, E, H

    pivot = N.value # pivot jako pierwszy
    N = N.next
    while N is not None:
        if N.value < pivot:
            L_tail.next = N
            L_tail = L_tail.next
        elif N.value == pivot:
            E_tail.next = N
            E_tail = E_tail.next
        else:
            H_tail.next = N
            H_tail = H_tail.next
        N = N.next

    L_tail.next = H_tail.next = E_tail.next = None # odpinam końcówki wskazników
    L, H = L.next, H.next # odpinam wartowniki
    return L, E, H # Głowy: mniejszych, takich samych, większych


# nie potrzebuję znać zakończeń węzłów, ponieważ defaultowo będę je zakańczał None'm (żeby wykluczyć przypadek zapętlenia się)
def quick_sort(L):
    L_head, E_head, H_head = partition(L)
    left = E_head
    right = tail(E_head)
    if L_head is not None: # istnieją mniejsze elementy
        left, right = quick_sort(L_head)
        right.next = E_head
        right = tail(E_head)
    if H_head is not None:
        tail(E_head).next, right = quick_sort(H_head) # dopinam posortowane większe el
    return left, right


def tab2list( A ):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next
    
    
def print_list( L ):
    while L != None:
        print( L.value, "->", end=" ")
        L = L.next
    print("|")
      

seed(42)

n = 10
T = [ randint(0,10) for i in range(n) ]
L = tab2list( T )

print("przed sortowaniem: L =", end=" ")
print_list(L) 
L, y = quick_sort(L)
print("po sortowaniu: L =", end=" ")
print_list(L)

if L == None:
    print("List jest pusta, a nie powinna!")
    exit(0)

P = L
while P.next != None:
    if P.value > P.next.value:
        print("Błąd sortowania")
        exit(0)
    P = P.next
        
print("OK")
