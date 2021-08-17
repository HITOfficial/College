#  chessboard with dimensions n × n is given. Each field (i, j) has a cost (a number from the set {1,..., 5}))
# in table A (in field A [j] [i]). In the author's position of the figure of the estimator (at position 0)
# is to go to the lower right, men in fields with a total cost (if the king
# stands in the square (i, j) to pay the cost of A [j] [i]; thus each route includes the cost of A [0] [0] and A [n - 1] [n - 1]). Please
# implement the kings path (A) function that computes the cost of a king path. The function should be possible
# as soon as possible (we still expect the complexity of O(n^2)

# complexity:
# - time O(N^2) -> 4N^2
# - space O(N^2)


def avaiable_moves(n, r, c):
    moves = [(-1, 0), (0, 1),
             (1, 0), (0, -1)]
    possible_moves = []
    for row, col in moves:
        new_row, new_col = row+r, col+c
        if new_row >= 0 and new_row < n and new_col >= 0 and new_col < n:
            possible_moves.append((new_row, new_col))
    return possible_moves


def kings_path(A):
    n = len(A)
    # linear 2 dim array
    distances = [float("inf")]*(n**2)
    distances[0] = A[0][0]
    for i in range(n):
        for j in range(n):
            for r, c in avaiable_moves(n, i, j):
                distances[r*n+c] = min(
                    distances[r*n+c], distances[i*n+j]+A[r][c])
    return distances[-1]


A = [
    [1, 1, 2],
    [5, 1, 3],
    [4, 1, 1]
]

print(kings_path(A))
