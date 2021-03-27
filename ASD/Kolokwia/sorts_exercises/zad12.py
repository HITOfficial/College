# wstawianie dowolnego elementu do kopca binarnego

# Kopiec Maxymalny:

def heap_desc(Arr,i,n):
    left = 2*i + 1
    right = 2*i + 2
    lowest = i
    if left < n and Arr[left] > Arr[lowest]:
        lowest = left
    if right < n and Arr[right] > Arr[lowest]:
        lowest = right
    if Arr[i] != Arr[lowest]:
        Arr[i], Arr[lowest] = Arr[lowest], Arr[i]
        heap_desc(Arr,lowest,n)


def max_heap(Arr,n):
    for i in range((n-1)//2,-1,-1): # Tworzę kopiec malejący
        heap_desc(Arr,i,n)
    for i in range(n-1,-1,-1):
        Arr[0], Arr[i] = Arr[i], Arr[0]
        heap_desc(Arr,0,i)


def add_to_heap(Arr,n,value):
    Arr[n] = value
    n += 1
    max_heap(Arr,n)



from random import randint
n = 10
Arr =[randint(1,100) for _ in range(n)]
for i in range(n): # operuję na defaultowej tablicy nie na liście
    Arr.append(None)



max_heap(Arr,10)
print(Arr)
add_to_heap(Arr,n,15)
print(Arr)