# A data set of N rectangles with sides parallel to the axis of the system is given.
# Please implement the function: which will indicate who should protect to pierce, as it has placed area.
# Each rectangle specifies the four numbers (x1, y1, x2, y2) that give the coordinates the lower left and upper right corners of the rectangle.
# The guide function is a list of such fours and it should return smallest number of the rectangle to be folded.
# The feature should be as fast as possible. Please estimate the time and memory complexity algorithm of the algorithm used

# complexity:
# - time O(N)
# - space O(1), single variables


# X bottom -> max, X top -> min
# Y bottom -> max, Y top -> min


def calculate_area(D, n):
    x_bottom, x_top = -float("inf"), float("inf")
    y_bottom, y_top = -float("inf"), float("inf")
    for i in range(n-1):
        x_bottom = max(x_bottom, D[i][0])
        x_top = min(x_top, D[i][2])
        y_bottom = max(y_bottom, D[i][1])
        y_top = min(y_top, D[i][3])
    return (x_top - x_bottom) * (y_top-y_bottom)


def bottom_max(a, b, idx, idx_new):
    if b > a:
        return b, idx_new
    else:
        return a, idx


def top_min(a, b, idx, idx_new):
    if b < a:
        return b, idx_new
    else:
        return a, idx


def rect(D):
    n = len(D)
    # need to calculate maximal area after removing only one square
    x_bottom, x_bottom_idx = -float("inf"), 0
    x_top, x_top_idx = float("inf"), 0
    y_bottom, y_bottom_idx = -float("inf"), 0
    y_top, y_top_idx = float("inf"), 0
    for i in range(n):
        x_bottom, x_bottom_idx = bottom_max(
            x_bottom, D[i][0], x_bottom_idx, i)
        y_bottom, y_bottom_idx = bottom_max(
            y_bottom, D[i][1], y_bottom_idx, i)
        x_top, x_top_idx = top_min(
            x_top, D[i][2], x_top_idx, i)
        y_top, y_top_idx = top_min(
            y_top, D[i][3], y_top_idx, i)
    # removing x min
    tmp = D.pop(x_bottom_idx)
    x_bottom_area = calculate_area(D, n)
    D.insert(x_bottom_idx, tmp)
    # removing y min
    tmp = D.pop(y_bottom_idx)
    y_bottom_area = calculate_area(D, n)
    D.insert(y_bottom_area, tmp)
    # removing x max
    tmp = D.pop(x_top_idx)
    x_top_area = calculate_area(D, n)
    D.insert(x_top_idx, tmp)
    # removing y max
    tmp = D.pop(y_top_idx)
    y_top_area = calculate_area(D, n)
    D.insert(y_top_idx, tmp)
    # returning idx, of element, to remove to maximalize area
    return max((x_bottom_idx, x_bottom_area), (y_bottom_idx, y_bottom_area), (x_top_idx, x_top_area), (y_top_idx, y_top_area), key=lambda x: x[1])[0]


D = [(2, 3, 10, 6), (3, 1, 8, 8), (5, 4, 9, 7)]

print(rect(D))
