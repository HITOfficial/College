# BST exercise 1

from BST_tree_with_size import *
# this algorithm is using functions from same directory in BST_tree_with_size.py 

# complexity: H, where H is hight of tree

# actual element index in root = left.children+1
# if algorithm will go to the right, then, need to reduce index value by left children.size value
def find_key_index(actual,index,flag=False): # index remaing to find, actual node element
    if flag is False: # added flag to check out if it is start of the algorithm becouse: indexes start from 0,1,2..., and size of tree from 1,2,3...
        index += 1
    if index > actual.size: # there is not enought elements in binary search tree
        return False

    actual_index = 1
    if actual.left is not None:
        actual_index = actual.left.size + 1

    if actual_index == index:
        return actual # found element
    elif index > actual_index:
        return find_key_index(actual.right, index-actual_index, True)
    else:
        return find_key_index(actual.left, index, True)


root = BSTNode(21)
insert(root,17)
insert(root,29)
insert(root,28)
insert(root,25)
insert(root,31)
insert(root,30)
insert(root,37)
insert(root,18)
insert(root,20)
insert(root,19)

print(find_key_index(root,1).key)


