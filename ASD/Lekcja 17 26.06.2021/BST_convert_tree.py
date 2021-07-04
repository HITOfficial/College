# zadanie nr 1. z kolokwium: 1/2 pkt

# złożoność:
# obliczeniowa: O(NlogN) <- wyszukiwanie minumum w drzewie
# pamięciowa: O(N) <- stworzenie stosu


class Node:
    def __init__( self ):
        self.left    = None  # lewe podrzewo
        self.right   = None  # prawe poddrzewo
        self.parent  = None  # rodzic drzewa jesli istnieje
        self.value   = None  # przechowywana wartosc


def minimum(actual):
    if actual.left is not None:
        return minimum(actual.left)
    else:
        return actual


# otrzymujemy wskaznik na kozen w drzewie
def convert_tree(p):
    # n razy wyszukuje minimum w drzewie, 
    # biore najmniejszy element z drzewa i bedzie on kozeniem w nowym drzewie
    root = minimum(p)
    
    p = delete(p,root)
    # dodałem gdy usuwam roota
    root.parent = None
    root.left = None
    root.right = None
    stack = [root]
    # dopoki nie jest pojedynczym lisciem
    # poprawka OR, posiada conajmniej 1 dziecko to sie jeszcze wykonuje
    while p is not None and (not p.left is None or not p.right is None):
        actual = minimum(p)
        p = delete(p,actual)
        # odpinam dzieci gdyby istnialy
        actual.parent = None
        actual.left = None
        actual.right = None
        # dorzucam do stosu element
        stack.append(actual)

    # dorzucam pojedynczy lisc, ktory pozostal (maxymalny element w drzewie)
    stack.append(p)
    # zachowuje jak w min cheap podpinanie galezie jak dzieci

    n = len(stack)
    # nie jestem pewien indexu wiec dorzuce ifa w for loopie' zeby nie wyleciec poza zakres tablicy
    for i in range((n+2)//2):
        left = 2*i+1
        right = 2*i+2
        # tworze polaczenia miedzy dziecki a rodzicami w drzewie
        if left < n:
            stack[i].left = stack[left]
            stack[left].parent =stack[i]
        if right < n:
            stack[i].right = stack[right]
            stack[right].parent =stack[i]

    # zwracam wskaznik na roota w nowym drzewie
    return stack[0]


def minimum(actual):
    if actual.left is not None:
        return minimum(actual.left)
    else:
        return actual


def delete(root,actual): # usuwam calego noda, nie tylko przepinam wartosci
    if not actual.left and not actual.right: # pojedynczy lisc
        if actual.parent is not None:
            if actual.parent.left is actual:
                actual.parent.left = None 
            else:
                actual.parent.right = None
        return root # empty tree

    elif actual.left and not actual.right: # node has only left branch
        if actual.parent is not None:
            actual.left.parent = actual.parent
            if actual.parent.left is actual:
                actual.parent.left = actual.left
            else:
                actual.parent.right = actual.left
        else: # removing root
            actual.left.parent = None
        if actual is root:
            return actual.left
        else:
            return root

    elif actual.right and not actual.left: # only right branch
        if actual.parent is not None:
            actual.right.parent = actual.parent
            if actual.parent.left is actual: # element to remove is a left branch of parent
                actual.parent.left = actual.right
                return root
            else:
                actual.parent.right = actual.right
                return root
        else:
            actual.right.parent = None # removing root element
        if actual is root:
            return actual.right
        else:
            return root

    else: # actual element has two two branches
        new = next(actual,actual.key) # searching for next value element in tree
        parent = actual.parent
        if actual.parent is not None: # not single element in branch
            if parent.left is actual: # element to remove is a left children
                parent.left = new
            else:
                parent.right = new

            new.left = actual.left # replacing branches from actual to new node
            if actual.right is not new: # element with next value in BST was not from single leaf
                new.parent.left = None # removing previous parent from next elemnt in BST
                new.right = actual.right
                actual.right.parent = new
            new.parent = actual.parent # new parents
            return root

        else: # deleting element is a root in BST
            # replacing  new node to be a root of BST
            new.left = actual.left # connecting left node
            new.left.parent = new
            if actual.right is not new: # right node
                new.right = actual.right
                new.parent.left = None
            new.parent = None
            return new 


root = Node()
root.value = 11

l1 = Node()
l1.parent = root
l1.value = 3
root.left = l1

r1 = Node()
r1.parent = Node()
r1.value = 13
root.right = r1

l2 = Node()
l2.parent = l1
l2.value = 2
l1.left = l2

r2 = Node()
r2.parent = l1
r2.value = 7
l1.right = r2

l3 = Node()
l3.parent = r2
l3.value = 5
r2.left = l3


print(convert_tree(root))
