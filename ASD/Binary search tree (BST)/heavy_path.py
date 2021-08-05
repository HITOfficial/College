# Exercise in PL lang.
# Proszę zaimplementować funkcję heavy path(T), która na wejściu otrzymuje drzewo T z ważonymi krawędziami
# (wagi to liczby całkowite—mogą być zarówno dodatnie, ujemne, jak i o wartości zero) i zwraca długość (wagę)
#  najdłuższej ścieżki prostej w tym drzewie. Drzewo reprezentowane jest za pomocą obiektów typu Node:

class Node:
    def __init__(self):
        self.children = 0
        self.child = []

# complexity:
# - time O(N), where N is number of nodes in tree
# - space O(1), correctly, recursion stack


def heavy_path(node):
    best_total_first, longest_first = 0, 0
    best_total_second, longest_second = 0, 0
    # single leaf condition
    if node.children == 0:
        return 0, 1, 0, 1
    for child_node, w in node.child:
        # values: best total value using double branches and single with length of path, max single branch value and length of it
        two_branches_total, two_branches_longest, single_branch_total, single_branch_longest = heavy_path(
            child_node)
        # if two branches have equal weights, should take with longer path
        if best_total_first == two_branches_longest and longest_first < longest_second:
            longest_first = longest_second
        # actual branch is greater than actual first branch and actual first branch is greater than second
        if best_total_first < single_branch_total + w and best_total_second <= best_total_first:
            # using actual branch, is the best option to increse maximum total weight
            best_total_second, longest_second = best_total_first, longest_first
            best_total_first, longest_first = single_branch_total + w, single_branch_longest
            print(w)
        # calculating what total weight can be done using second branch in this level in tree
        elif best_total_second < single_branch_total + w:
            print(w)
            best_total_second, longest_second = single_branch_total + w, single_branch_longest
    # checking if on actual level found better double branch option
    if two_branches_total > best_total_first + best_total_second:
        # retuning total best combination using double branch, and best option using only single branch
        return two_branches_total, two_branches_longest, best_total_first, longest_first+1
    else:
        return best_total_first + best_total_second, longest_first + longest_second+1, best_total_first, longest_first+1


# Test:
c14 = Node()
c13 = Node()
c12 = Node()
c11 = Node()
c10 = Node()
c9 = Node()
c8 = Node()
c7 = Node()
c6 = Node()
c5 = Node()
c4 = Node()
c3 = Node()
c2 = Node()
c1 = Node()
c0 = Node()
c0.children = 3
c0.child.extend([(c11, 5), (c5, 3), (c1, 4)])
c1.children = 2
c1.child.extend([(c2, -10), (c3, 6)])
c3.children = 1
c3.child.extend([(c4, 7)])
c5.children = 2
c5.child.extend([(c6, -1), (c8, -12)])
c6.children = 1
c6.child.extend([(c7, -10)])
c8.children = 1
c8.child.extend([(c9, 8)])
c11.children = 4
c11.child.extend([(c10, 6), (c12, 9), (c13, 2), (c14, 0)])

print(heavy_path(c0))
