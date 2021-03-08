class Node:
  def __init__(self):
    self.next = None
    self.value = None

# Insert to node List node (first element is an sentinel)
def insert_to_node(node, L):
    start = L
    while L.next is not None and L.next.value > node.value:
        L = L.next
    node.next = L.next
    L.next = node
    return start


# lowest index of value in Table
def binary_search(T, b=0, e=None, val=None): # table, begin, end, value to search
    if e == None:
        e = len(T)-1
    if b > e:
        return None
    half = (e+b)//2
    if T[half] == val:
        ret = binary_search(T, b, half-1, val)
        if ret == None:
            return half # we'll waiting for smallest index
    if T[half] > val:
        return binary_search(T,b, half-1, val)
    else:
        return binary_search(T,half+1, e, val)

T = [1,2,3,4,5,6,7]

print(binary_search(T,0, len(T)-1, 5))


