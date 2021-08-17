# 2 dim knapsack problem:  item x weight x height

# complexity:
# - time O(N*W*H), where N: number of items, W: max weight, H max height
# - space O(N*W*H)


def get_path2d(array, P, item, weight, height):
    path = []
    _, h, w = P[item+1]
    if item >= 0:
        if array[item][weight][height] < array[item+1][weight][height]:
            path.append(item+1)
            path.extend(get_path2d(array, P, item-1, weight-w, height-h))
        else:
            path.extend(get_path2d(array, P, item-1, weight, height))
    return path


def knapsack2d(P, max_w, max_h):
    # tuples in P(value,height,weight)
    n = len(P)
    array = [[[0]*(max_h+1) for _ in range(max_w+1)] for _ in range(n)]
    # filling data using only first item
    for weight in range(P[0][2], max_w+1):
        for height in range(P[0][1], max_h+1):
            array[0][weight][height] = P[0][0]

    for item in range(1, n):
        for weight in range(max_w+1):
            for height in range(max_h+1):
                # updating data with previous item
                array[item][weight][height] = array[item-1][weight][height]
                v, h, w = P[item]
                # condition: item in correctly range
                if h <= height and w <= weight:
                    array[item][weight][height] = max(
                        array[item][weight][height], array[item][weight-w][height-h] + v)
    return array[-1][-1][-1], [P[idx] for idx in get_path2d(array, P, n-2, weight, height)]


P1 = [(1, 2, 2), (4, 3, 3), (5, 5, 5), (7, 7, 7),
      (2, 4, 4), (3, 2, 1), (1, 2, 3)]

P2 = [(5, 10, 3), (7, 8, 12), (2, 7, 3)]

print(knapsack2d(P1, 10, 5))
print(knapsack2d(P2, 16, 15))
