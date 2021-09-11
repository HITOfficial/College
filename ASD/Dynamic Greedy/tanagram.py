# Consider the word x[0] x[1] x[n - 1] and y[0] y[1] weigh lowercase letters of the Latin alphabet. These two words are a t-anagram(for t ∈ {0, .., N - 1}) if each letter is
# the first words can be put on the same letter that are on different positions
# each at the current t, so that the letter of the second word is assigned one letter of the word the first.
# Please implement the function: which checks if words and y are the bells and returns True yes and False if and then.
# The feature should be as fast as possible. Please estimate the time complexity and the memory algorithm used.

from queue import PriorityQueue

# complexity:
# - time O(NKlogK), where K is a number of same letters
# - space O(1) -> 26, creating array of latino letters


def tanagram(x, y, t):
    # only lower latino letters
    # 26 priority queues -> a: 97, z: 122
    A = [PriorityQueue() for _ in range(26)]
    # adding every number into
    for idx, letter in enumerate(x):
        A[ord(letter)-97].put(idx)
    for idx, letter in enumerate(y):
        # empty queue
        if A[ord(letter)-97].empty():
            return False
        x_idx = A[ord(letter)-97].get()
        if t < abs(idx-x_idx):
            return False
    return True


print(ord("z"))


x = "kotomysz"
y = "tokmysoz"
print(tanagram(x, y, 3))
print(tanagram(x, y, 2))
