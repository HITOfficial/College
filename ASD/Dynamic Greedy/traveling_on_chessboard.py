# Given is a chessboard A with dimensions n × n. A chessboard
# contains rational numbers. One should go from (0, 0) to the (n-1,n-1) go through n fields, "down"
# and "right". Entering a given field costs as much as there are numbers. Please select an algorithm
# tour time with combined cost.
from queue import PriorityQueue

# complexity:
# - time: NlogN <- similar algroithm to Dijkstra shortest path
# - space: N^2 -> space for priority queue


def moves(n, r, c):
    array = [(0, 1), (1, 0)]
    steps = []
    for row, col in array:
        new_row, new_col = row+r, col+c
        if new_row < n and new_col < n:
            steps.append((new_row, new_col))
    return steps


def traveling_on_chessboard(chessboard):
    n = len(chessboard)
    weights = [[float("inf")]*n for _ in range(n)]
    p_queue = PriorityQueue()
    # tuple in priority queue: total weight, row, col
    p_queue.put((0, 0, 0))
    while not p_queue.empty():
        w, r, c = p_queue.get()
        if weights[r][c] > w:
            weights[r][c] = w
            for new_row, new_col in moves(n, r, c):
                new_w = w + chessboard[new_row][new_col]
                p_queue.put((new_w, new_row, new_col))

    return weights[-1][-1]


chessboard = [
    [0, 1, 2, 3, 4, 19, 20, 5],
    [3, 8, 7, 6, 10, 6, 4, 1],
    [4, 15, 16, 21, 9, 5, 6, 2],
    [9, 8, 13, 19, 19, 18, 4, 1],
    [8, 5, 4, 4, 3, 9, 12, 100],
    [19, 20, 9, 11, 12, 42, 57, 41],
    [1, 26, 9, 17, 4, 9, 19, 17],
    [1, 1, 19, 29, 23, 24, 16, 16],
]

print(traveling_on_chessboard(chessboard))
