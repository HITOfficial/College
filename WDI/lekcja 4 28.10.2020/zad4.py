# Napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e = 1/0! + 1/1! +
# 1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).

# pierwszy pomysł to obliczę liczbę jaka wychodzi dokładnie do 1000 miejsca po przecinku
# osobno zrobie funkcje liczącą sinią i potem będę ją wrzucał do list comprachention
def factorial(n):
    multiply_factioral = 1 # bo 1 jest liczbą neutralną silni
    
    for i in range(0,n): # lecę z zasięgiem do n+1 bo wtedy zakres wynosi => (1,n)
        if i == 0: 
            multiply_factioral *= 1 # nie można dzielić przez 0 więc zrobiłem osobno
        else:
            multiply_factioral *= i
    
    return multiply_factioral


def list_of_e_seq(n):
    list_of_e = [1/factorial(i) for i in range(1, n)]
    print(list_of_e)
    print(sum(list_of_e))


print(list_of_e_seq(230))
