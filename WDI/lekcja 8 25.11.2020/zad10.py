# Rekurencyjne obliczanie wyznacznika z macierzy (treść oczywista)

# detA = suma <0->n) (-1)^i+j a(i,j)M(i,j)
from copy import deepcopy

t = [
    [1,2,3],
    [6,5,4],
    [3,7,2]
]


def matrix_minor(matrix, i,j):
    # usuwam altualny wiersz i kolumnę z listy
    for row in range(len(matrix)):
        del matrix[row][j] # kolumna 
    del matrix[i] # wiersz

    return matrix


def det(matrix):
    if len(matrix[0]) != len(matrix):
        return ('macierz nie kwadratowa')
    elif len(matrix) == 1:
        return matrix[0][0]
    else:
        s = 0
        for j in range(len(matrix)):
            s += ((-1)**(0+j))*matrix[0][j] * det(matrix_minor(deepcopy(matrix),0,j))
        return s
                
print(det(t))




    