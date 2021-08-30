# In the forest are tree in the same  row. Each tree has a value that
# should be treated as a profit after it is trimmed. We cannot cut down more than two trees in a row.
# Please implement the center function you want to cut the tree, profit
# it was like living

# bottom up alg.
# two functions:
# F(x) vaule with cutting x tree
# G(x) value without x tree

# complexity: Time / Space -> O(N)

def F(x, f, g, T):
    f[x] = max(f[x+1], g[x+1]+T[x])


def G(x, f, g):
    g[x] = max(g[x+1], f[x+1])


def cut_trees(T):
    n = len(T)
    f = [0]*n
    g = [0]*n
    # auto updating last value to not add conditions to F/G function
    f[-1] = T[-1]
    for x in range(n-2, -1, -1):
        G(x, f, g), F(x, f, g, T)
    return max(f[0], g[0])


T = [3, 4, 5, 1, 9]

print(cut_trees(T))
