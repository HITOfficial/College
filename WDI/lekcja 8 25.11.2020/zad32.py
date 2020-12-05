T=[2,2,3,3,4,4]

target = 3

def subset(t, k=0,j=0, k_sum=0, j_sum=0, i=0, taken= False): # robię dwie sumy, i sprawdzam czy są równe 
    if i == len(t):
        return False
    if k_sum == j_sum and k == target and i != 0 and taken:
        return True
    return (
            subset(t, k+1, j, k_sum+T[i], j_sum, i+1, True)
            or subset(t, k, j+1, k_sum, j_sum+T[i], i+1, True)
            or subset(t, k, j, k_sum, j_sum, i+1, taken)
    )

print(subset(T))