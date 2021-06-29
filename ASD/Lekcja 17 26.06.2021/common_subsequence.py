# complexity:
# -time: O(N1*N2), where N1, N2 are lenght's of the word
# -memory: O(N1*N2)


def common_subsequence(a,b):
    n1 = len(a)
    n2 = len(b)
    common = [[0]*(n2+1) for _ in range(n1+1)]
    for row in range(1,n1+1):
        for column in range(1,n2+1):
            # checking if have same character
            if a[row-1] == b[column-1]:
                common[row][column] = common[row-1][column] + common[row][column-1] +1
            else:
                common[row][column] = common[row-1][column] + common[row][column-1] - common[row-1][column-1]
    return common[n1][n2]


a = "figlksaf"
b = "lefgkas"

print(common_subsequence(a,b))