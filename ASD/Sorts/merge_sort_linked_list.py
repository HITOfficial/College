# merge sort algorithm on Linked List
# complexity:
# - time O(nlogn)
# - space O(1)


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


def mid_node(head):
    if head is None:
        return None
    # in while loop p moves only once, and q moves twice
    mid, end = head, head
    while end.next_node is not None and end.next_node.next_node is not None:
        mid = mid.next_node
        end = end.next_node.next_node
    return mid


def merge(l, r):
    sentinel = Node()
    p = sentinel
    l_next, r_next = l.next_node, r.next_node
    while l is not None and r is not None:
        if l.value <= r.value:
            p.next_node = l
            l = l.next_node
            p = p.next_node
            p.next_node = None
            if l_next is not None:
                l_next = l_next.next_node
        else:
            p.next_node = r
            r = r.next_node
            p = p.next_node
            p.next_node = None
            if r_next is not None:
                r_next = r_next.next_node
    if r is not None:
        # taking all remaining nodes i right side
        p.next_node = r
    if l is not None:
        p.next_node = l
    # returning sorted part of linked list
    return sentinel.next_node


def merge_sort_linked_list(head):
    # empty part of linked list or single node
    if head is None or head.next_node is None:
        return head

    # partition full node into two parts:
    # - nodes from head to middle element (with middle)
    # - from middle to last node ( without middle)
    mid = mid_node(head)
    l = head
    r = mid.next_node
    mid.next_node = None
    l_part = merge_sort_linked_list(l)
    r_part = merge_sort_linked_list(r)
    return merge(l_part, r_part)


array = [9, 1, 8, 7, 5, 3, 4, 5, 17, 2]
# converting python list into linked list
linked_list = array_to_linded_list(array)
print_linked_list(merge_sort_linked_list(linked_list))
