from math import floor
from random import random


class Node():
    def __init__(self):
        self.next = None
        self.value = None


def sort_list(L): # porównuje wartość każdego wyznacznika z każdym, zwracam wskaznik na 1wszy i ostatni element po posortowaniu
    if L == None: # brak elementów w liście
        return None, None
    if L.next == None: # 1 element w liście
        return L, L
    sentinel = Node()
    sorted_list = sentinel # sorted list
    while L is not None:
        lowest_node = node_prev = L
        node = L.next
        while node is not None:
            if lowest_node.value > node.value:
                lowest_node = node
                if node_prev.next is not None: # jeśli istnieja jeszcz kolejny węzeł przepinam na niego
                    node_prev.next = node.next
                    node = node.next
                    continue
            node_prev = node
            node = node.next
        if L == lowest_node: # pierwszy element z listy jest najmniejszy wiec ja przesuwam w kolejnej iteracji
            L = L.next
        sorted_list.next = lowest_node
        sorted_list = sorted_list.next
    sort_list.next = None # odpinam ostatnie wskazanie, żeby wykluczyć infinity loop
    return sentinel.next, sort_list # odpinam wartownika i dodatkowo zwracam ogon


def bucketsort_nodelist(L,a=0,b=1,n=None): # node list, przedzial [a,b), ilosc elementow
    if n is None:
        n = L # policze ile jest elementów w liscie
        count = 1
        while n.next is not None:
            count += 1
            n = n.next
        n = count

    T = [[Node(),None] for _ in range(n)] # tworze n wartowników każdy 2 elementowej tablic(zamiast tupli bo są imutable), żeby potem mieć do nich dostęp
    while L is not None: # wrzucam do kubełków elementy
        index = floor(((L.value-a)/(a+b))*n)
        sentinel = T[index][0] # wskaznik na wartownika
        last_node = T[index][1]
        if sentinel.next is None: # na razie pusty wartownik tylko w tym przedziale
            sentinel.next = L
            T[index][1] = L # pierwszy element w danym przedziale, nie liczac wartownika
        else:
            last_node.next = L
            last_node = last_node.next
        L = L.next

    first = Node()
    sorted_list = first
    sorted_part_tail = None
    for i in range(n):
        if T[i][1] is not None: # istnieja elementy w tym przedziale
            sorted_list.next, sorted_part_tail = sort_list(T[i][0].next)
            sorted_list = sorted_part_tail
    return first.next


def print_nodes(L,a=None): # sztczyny drugi parametr bo zwracam tupla w sorcie
    while L is not None:
        print(L.value, end="->")
        L = L.next


def nodes(n):
    first = Node()
    node = first
    for _ in range(n):
        node.next = Node()
        node = node.next
        node.value = random()
    return first.next


# czasami istnieje bug, i się zapętli w infinity loop'a
x = nodes(10)
print_nodes(x)
print("\n")
print_nodes(bucketsort_nodelist(x))