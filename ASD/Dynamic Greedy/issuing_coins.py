# We have a table with the denominations of coins used in some strange country and the amount T. Please enter an algorithm that calculates the minimum amount of coins needed to spend
# T amounts (the greedy algorithm that spends the largest coin first does not work: for coins 1, 5, 8, it will spend
# number 15 as 8 + 5 + 1 + 1 instead of 5 + 5 + 5).


# complexity:
# - time O(N*W) , where n is total numer of coins, and w is weight to find number of coins
# - space O(N*W)


def used_coins(solutions, C, coin, cost):
    coins = []
    if coin-1 >= 0:
        # that means algorithm used this coin to create solution
        if solutions[coin][cost] < solutions[coin-1][cost]:
            coins.append(C[coin])
            coins.extend(used_coins(solutions, C, coin-1, cost-C[coin]))
        else:
            coins.extend(used_coins(solutions, C, coin-1, cost))
    return coins


def issuing_coins(C, w):
    n = len(C)
    solutions = [[float("inf")]*(w+1) for _ in range(n)]
    # total weight 0 -> 0 coins used
    for i in range(n):
        solutions[i][0] = 0
    # using only first element
    solutions[0][C[0]] = 1
    for coin in range(1, n):
        for cost in range(w+1):
            solutions[coin][cost] = solutions[coin-1][cost]
            if cost - C[coin] >= 0:
                solutions[coin][cost] = min(
                    solutions[coin][cost], solutions[coin-1][cost-C[coin]]+1)
    if solutions[-1][-1] == float("inf"):
        return False
    else:
        return solutions[-1][-1], used_coins(solutions, C, n-1, w)


C = [1, 2, 3, 4, 5, 6, 7, 11, 19]
w = 12

print(issuing_coins(C, w))
