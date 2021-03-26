# 7.Dane są trzy zbiory reprezentowane przez tablice: A, B i C. Napisz algorytm, który powie,
# czy istnieje taka trójka a, b, c z odpowiednio A, B, i C, że a + b = c.  Nie wolno korzystać ze słowników!
from random import randint


def is_three(A,B,C):
    A_len, B_len, C_len= len(A), len(B), len(C)
    A.sort(), B.sort()
    A_index, B_index, C_index = 0, B_len-1, 0
    while A_index < A_len and C_index < C_len and B_index < B_len:
        A_el, B_el, C_el = A[A_index], B[B_index], C[C_index]
        if A_el + B_el < C_el:
            A_index += 1
            continue
        if A_el + B_el == C_el:
            C_index += 1
            A_index, B_index = 0, B_len-1
            continue
        while B_index < B_len and B_index > -1:
            B_el = B[B_index]
            if A_el + B_el > C_el:
                B_index -= 1
                continue
            if A_el + B_el == C_el:
                C_index += 1
                A_index, B_index = 0, B_len-1
            break
        else:
            break
    if C_index == C_len:
        return True 
    else:
        return False



A= [randint(1,1000) for _ in range(100)]
B= [randint(-50,1000) for _ in range(1000)]
C= [randint(-10,1000) for _ in range(70000)]
print(is_three(A,B,C))