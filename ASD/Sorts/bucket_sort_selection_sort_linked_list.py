# bucket sort on linked list using selection sort algorithm to sort nodes inside every nodes

# complexity:
# - time O(N+K) / O(N^2) <- in worts case: all elements in the same bucket
# - space O(N)


class Node():
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


def array_to_linded_list(array):
    n = len(array)
    # condition if array is not empty
    if n == 0:
        return None
    else:
        head = Node(array[0])
        p = head
        for i in range(1, n):
            actual = Node(array[i])
            p.next_node = actual
            p = actual
        return head


def print_linked_list(node):
    while node is not None:
        print(node.value, end="->")
        node = node.next_node


def selection_sort_linked_list(head):
    # taking of sentinel from not sorted linked list
    head = head.next_node
    sentinel = Node()
    p = sentinel
    q = head
    pivot = q
    while q is not None:
        s_prev, s = q, q.next_node
        prev_pivot, pivot = Node(), q
        while s is not None:
            if s.value < pivot.value:
                prev_pivot, pivot = s_prev, s
            s_prev, s = s, s.next_node
        # node with lowest value is a first element in linked list
        if prev_pivot.value is None:
            q = pivot.next_node
            p.next_node = pivot
            pivot.next_node = None
        # lowest value node is not a first node in linked list to sort
        else:
            prev_pivot.next_node = pivot.next_node
            p.next_node = pivot
            pivot.next_node = None
        # moving to tail in sorted linked list
        p = p.next_node
    tail = sentinel
    while tail.next_node is not None:
        tail = tail.next_node
    # returning sentilen and tail of sorted part linked list
    return sentinel, tail


def bucket_sort_linked_list(head):
    n = 0
    p = head
    # sentinel to sorted linked list
    s = Node()
    min_value = float("inf")
    max_value = -float("inf")
    # counting number of nodes in linked list
    while p is not None:
        min_value = min(min_value, p.value)
        max_value = max(max_value, p.value)
        n += 1
        p = p.next_node
    # single node in linked list, or empty linked list
    if n == 0 or n == 1:
        return head
    # creating buckets, and adding tuple head, tail of every bucket
    buckets = []
    n += 1
    for _ in range(n+1):
        sentinel = Node()
        tail = sentinel
        buckets.append((sentinel, tail))
    p = head
    # adding nodes into correctly bucket
    while p is not None:
        # integer number -> int(number)
        index = int(((p.value-min_value)/(max_value-min_value))*n)
        # head and tail of bucket
        h, t = buckets[index]
        # adding into linked list new node
        t.next_node = p
        p = p.next_node
        t = t.next_node
        t.next_node = None
        buckets[index] = h, t
    # sorting every bucket
    for i, bucket in zip(range(n), buckets):
        buckets[i] = selection_sort_linked_list(bucket[0])
    # zip into one linked list all buckets
    sentinel = Node()
    tail = sentinel
    for h, t in buckets:
        # this bucket has nodes
        if h.next_node is not None:
            # taking of sentinel
            h = h.next_node
            tail.next_node = h
            # taking tail from bucket
            tail = t
    return sentinel.next_node


array = [1, 0, 2, 5, 6, 87, 0, 3, 3465, 0, 3, 2, 4, 6, 2, 7, 8, 0, 34, 53, 4]

node = array_to_linded_list(array)
linked_list = bucket_sort_linked_list(node)
print_linked_list(linked_list)
