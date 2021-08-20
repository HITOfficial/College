# Zbigniew the frog jumps on the number line. It is supposed to get from zero to n - 1 by jumping the cart towards
# the whole number. A jump from i to j (j> i) costs Zbigniew j - i units of energy, and his
# energy can never drop below zero. At the beginning, Zbigniew has 0 energy units, but on
# Fortunately, some numbers — also zero — are nutritional choices
# (the value of the snack is added to the current energy of Zbigniew).
# Please implement the function zbigniew (A), which receives the array A length as input
# len (A = n, each energy value) field contains the corresponding value. We need a hassle to zero to
# n-1 or -1 if this is not possible.

from queue import PriorityQueue

# complexity:
# - time O(NKlogN)
# - space O(N)


def Zbigniew_the_frog(A):
    n = len(A)
    jumps = 1
    # tuple in priority queue: done distance + energy, energy
    p_queue = PriorityQueue()
    p_queue.put((-1*A[0], A[0]))
    while not p_queue.empty():
        next_p_queue = PriorityQueue()
        while not p_queue.empty():
            dist_with_energy, energy = p_queue.get()
            # highest priority has lowest numbers
            dist_with_energy *= -1
            # found best option
            if dist_with_energy >= n-1:
                return jumps
            dist = dist_with_energy-energy
            for d in range(dist+1, dist_with_energy+1):
                # in this distance can recive energy
                if A[d] > 0:
                    remaining_energy = energy - (d-dist) + A[d]
                    next_p_queue.put(
                        (-1*(d+remaining_energy), remaining_energy))
        jumps += 1
        p_queue = next_p_queue
    return -1


A1 = [2, 2, 1, 0, 0, 0]
A2 = [4, 5, 2, 4, 1, 2, 1, 0]

print(Zbigniew_the_frog(A1))
print(Zbigniew_the_frog(A2))
