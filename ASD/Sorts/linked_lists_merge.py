# Given is a structure implementing a one-way list:
# Please write a function that has a chance to enter the place of the sorted lists thus realized, merging them
# into one sorted list (consisting of the same elements).
# An example of an array [[0,1,2,4,5], [0,10,20], [5,15,25]] - after transforming its elements
# from Python list to one-way lists - temperature should be a one-way list that
# after converting it to a Python list, it will take the form [0,0,1,2,4,5,5,10,15,20,25].


# complexity:
# - time O(K*(N+M)), K is number of lists to merge, N, M are lists length to merge
# - space O(1) without including extra lists


class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = val


def list_to_linked_list(A):
    sentinel = Node()
    p = sentinel
    for val in A:
        p.next = Node(val)
        p = p.next
    # taking of sentinel
    return sentinel.next


def linked_list_to_list(p):
    A = []
    while p is not None:
        A.append(p.val)
        p = p.next
    return A


def merge(a, b):
    sentinel = Node()
    p = sentinel
    while a is not None and b is not None:
        if a.val < b.val:
            p.next = a
            a = a.next
            p = p.next
        else:
            p.next = b
            b = b.next
            p = p.next
    if a is None:
        p.next = b
    else:
        p.next = a
    return sentinel.next


def linked_lists_merge(T):
    k = len(T)
    for i in range(k):
        T[i] = list_to_linked_list(T[i])
    a = T[0]
    for b in range(1, k):
        a = merge(a, T[b])
    return a


A = [[0, 1, 2, 4, 5], [0, 10, 20], [5, 15, 25]]

node = linked_lists_merge(A)
print(linked_list_to_list(node))
