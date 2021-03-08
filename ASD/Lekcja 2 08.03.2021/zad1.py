# Proszę zaimplementować algorytm MergeSort sortujący tablicę, opierający się na złączaniu
# serii naturalnych.
class Node:
      def __init__(self):
        self.next = None
        self.value = None


def tab_to_list(T):
    L = Node() # wartownik
    first = L
    for el in T:
        L.next = Node()
        L.next.value = el
        L = L.next
    first = first.next
    return first


def show_nodes(L):
    while L is not None:
        print(L.value,'->',end=' ')
        L = L.next
    


def ascending_list(L): 
    h1 = L
    while L.next != None and L.next.value >= L.value:
        L = L.next # szuka pierwszy podciąg rosnący
    h2 = L.next
    L.next = None
    return h1, h2 # -> glowa aktualnego, i wyznacznik do pozostałych el.

def merge(L1,L2): # scalanie na listach
    if L1 == L2 == None:
        return None # puste node'y
    if L2 is not None and L2.value == None: # warunek bo porównuje z wartownikiem, który jest pusty
        return L1
    if L1 is not None and L1.value == None: # warunek bo porównuje z wartownikiem, który jest pusty
        return L2 

    S = Node() # wartownik do którego będę podpinał rosnący podciąg
    first = S # żeby potem móc łatwo odpiąć wartownika
    while L1 is not None and L2 is not None:
        if L1.value <= L2.value:
            S.next = L1
            L1 = L1.next
        else:
            S.next = L2
            L2 = L2.next
        S = S.next
    if L1 is None: # zabrakło elementów w 1wszej liście
        S.next = L2
    if L2 is None:
        S.next = L1
    return first.next # zwracam bez wartownika


def mergesort(L):
    S = Node() # posortowana lista
    if L is None:
        return None # wyskocze bo nie ma elementów w liście

    while True:
        H1,L = ascending_list(L)
        if L is None: # Nie posiada drugiego fragmentu
            S = merge(S, H1) # sortuje aktualne rosnące podzbiory
            break
        else:
            S = merge(S,H1)
    return S


from random import randint

# T = [1,2,4,-1,6,3]
T = [randint(-100,100) for _ in range(20)]


L = tab_to_list(T)
show_nodes(mergesort(L))


