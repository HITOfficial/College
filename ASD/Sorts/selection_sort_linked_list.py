# insertion sort algorithm on linked list

# complexity:
# - time O(n^2)
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


def selection_sort_linked_list(head):
    sentinel = Node()
    # sorted linked list
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
    # taking off sentinel
    head = sentinel.next_node
    # taking off sentinel and returning head of sorted linked list
    return head


array = [9, 1, 8, 7, 5, 3, 4, 5, 17, 2]

node = array_to_linded_list(array)
print_linked_list(selection_sort_linked_list(node))
