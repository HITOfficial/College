# complexity:
# -time O(k!), where k is number of equal digits -> 256*k!
# -memory O(k) -> 256*k

# extra element- Class to stop permutations if found correct combine
class Flag():
    def __init__(self,flag=False):
        self.flag = flag


# modyfied heap alg from: https://www.geeksforgeeks.org/heaps-algorithm-for-generating-permutations/
def heap_permutation(x_indexes,array,size,t,ClassFlag):
    # flag to do not create next permutations, becouse found correctly
    if ClassFlag.flag is True:
        return
    if size == 1:
        flag = True
        for i in range(len(array)):
            # checking if this permutation is correctly
            if abs(x_indexes[i]-array[i]) > t:
                flag = False
                break
        if flag is True:
            ClassFlag.flag = True
            return

    for i in range(size):
        heap_permutation(x_indexes,array,size-1,t,ClassFlag)
        if size & 1:
            array[0], array[size-1] = array[size-1], array[0]
        else:
            array[i], array[size-1] = array[size-1], array[i]


def memorize_positions(array,word):
    for letter,index in zip(word,range(len(word))):
        # memorizing positions of letters, and flag to check if used letter
        array[ord(letter)].append(index)


x = "kotomysz"
y = "tokmysoz"


def tanagram(x, y, t):
    # return False
    # cannot be anagrams if have different lengths
    if len(x) != len(y):
        return False
    # ASCI code  array to memorize indexes of letters 
    x_positions = [[] for _ in range(256)]
    y_positions = [[] for _ in range(256)]
    # memorizing positions of letters
    memorize_positions(x_positions,x)
    memorize_positions(y_positions,y)
    # finding all used elements from ASCI coding
    for letter_code in range(256):
        number_of_letter = len(x_positions[letter_code])
        if number_of_letter > 0:
            ClassFlag = Flag()
            # if words are anagrams, first condition is to have the same number of equal letters
            if number_of_letter == len(y_positions[letter_code]):
                heap_permutation(x_positions[letter_code],y_positions[letter_code],number_of_letter,t,ClassFlag)
                # checking if found correctly permutation
                if ClassFlag.flag is True:
                    continue
                else:
                    return False
            else:
                return False
    return True

x3 = "abaabababaaaababaaaaabaabba"
y3 = "baaaababbaaaaabbaaaabaabaab"
r3 = 1

x5 = "sloniatko"
y5 = "oktainols"
r5 = 8

x6 = "darjeeling"
y6 = "darjeeling"
r6 = 0

print(tanagram(x3,y3,r3))
print(tanagram(x5,y5,r5))
print(tanagram(x6,y6,r6))