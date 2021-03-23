T = [1,1,2,2,3,1,1,0,0,2]

def missing_element(Arr_to_find):
    for i in range(len(Arr_to_find)):
        if Arr_to_find[i] == 0:
            return i # zwracam index pod którym nie ma elementu
    return False


def find_smallest_range(Arr,k): # elementy w tablicy [0,k)
    n = len(Arr)
    Arr_to_find = [0]* k
    i = j = 0;
    Arr_to_find[Arr[i]] += 1

    while missing_element(Arr_to_find) is not False:
        j += 1;
        if j == n:
            exit(print("nie ma wszystkich el w tablicy"))
        Arr_to_find[Arr[j]] += 1
    smallest = j-i+1 # najmniejszy przedział
    missing_index = None
    i -= 1

    while missing_index is None and j < n-1:
        while i < n-1 and missing_index is None: # skracam przedział
            i += 1
            Arr_to_find[Arr[i]] -= 1
            if Arr_to_find[Arr[i]] == 0:
                missing_index = Arr_to_find[Arr[i]]
            else:
                smallest = min(j-i,smallest)

        while j < n-1 and missing_index is not None: # wydłurzam przedział
            j += 1;
            Arr_to_find[Arr[j]] += 1
            if Arr_to_find[missing_index] != 0:
                smallest = min(j-i,smallest)
                missing_index = None

    return smallest


print(find_smallest_range(T,4))