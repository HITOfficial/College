from math import sqrt, acos


def facenorm(A, B, C):
    a = (B[0] - A[0], B[1] - A[1])
    b = (C[0] - A[0], C[1] - A[1])
    # cross product of (AB, AC)
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]) 

def vecang(A, B):
    # arccos(dot_product(A,B) / (length(A) * length(B))) converted do deg
    return acos(A[0] * B[0] + A[1] * B[1] + A[2] * B[2] / sqrt(A[0] * A[0] + A[1] * A[1]) * sqrt(B[0] * B[0] + B[1] * B[1])) * 57.2957795
