# Zbigniew the frog jumps on the number line. It is supposed to get from zero to n - 1 by jumping the cart towards
# the whole number. A jump from i to j (j> i) costs Zbigniew j - i units of energy, and his
# energy can never drop below zero. At the beginning, Zbigniew has 0 energy units, but on
# Fortunately, some numbers — also zero — are nutritional choices
# (the value of the snack is added to the current energy of Zbigniew).
# Please implement the function zbigniew (A), which receives the array A length as input
# len (A = n, each energy value) field contains the corresponding value. We need a hassle to zero to
# n-1 or -1 if this is not possible.


# pseudo max fuel capacity will be 100, to create dynamic_array

# complexity:
# - time O(N*2) -> N x N x C
# - space O(N) -> N x C, where C is capacity


def Zbigniew_the_frog(A, c=100):
    c += 1
    n = len(A)
    jumps = [[float("inf")]*c for _ in range(n)]
    jumps[0][0] = 0
    # updating data using only first beggining element
    for dist in range(n):
        # in this field is fuel
        if A[dist] > 0:
            for beginning_energy in range(c):
                if jumps[dist][beginning_energy] != float("inf"):
                    # sum of energy remaining in this field + energy in this field
                    energy_total = beginning_energy + A[dist]
                    for dist_update in range(dist+1, min(dist+1+energy_total, n)):
                        energy_remaining = energy_total-(dist_update-dist)
                        jumps[dist_update][energy_remaining] = min(
                            jumps[dist_update][energy_remaining], jumps[dist][beginning_energy]+1)
    return min(jumps[-1])


A1 = [2, 2, 1, 0, 0, 0]
A2 = [4, 5, 2, 4, 1, 2, 1, 0]

print(Zbigniew_the_frog(A1), ",", Zbigniew_the_frog(A2))
