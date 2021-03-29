from random import randint

def generate_word(n): # max_word len
    letters = "abcdefghijklmnouprstwyzx"
    word = ""
    for _ in range(randint(1,n)): # założenie, przynajmniej jedno wyrazowe słowo
        word += letters[randint(0,len(letters)-1)] # losuje index litery z alfabetu
    return word


def count_sort(Arr,k):
    count_Arr = [0]*26 # ord(z)-ord(a)+1
    for el in Arr:
        count_Arr[ord(el[k])-97] += 1 # -ord(a)
    for i in range(1,26):
        count_Arr[i] += count_Arr[i-1]
    sorted_Arr = [None] * len(Arr)
    for i in range(len(Arr)):
        sorted_Arr[count_Arr[ord(Arr[i][k])-97]-1] = Arr[i]
        count_Arr[ord(Arr[i][k])-97] -= 1
    return sorted_Arr
    # for i in range(len(Arr)):
    #     Arr[i] = sorted_Arr[i]


# def radix_sort(Arr,n): # kubełek, długość elementów w kubełku
#     for i in range(n-1,-1,-1):
#         count_sort(Arr,i)
    

# def bucket_sort(Arr):
#     n = len(Arr)
#     max_len = len(Arr[0])
#     min_len = len(Arr[0])
#     for el in Arr:
#         if len(el) > max_len:
#             max_len = len(el)
#         if len(el) < min_len:
#             min_len = len(el)
#     buckets = [list() for _ in range(max_len-min_len+2)]
#     for el in Arr: # wrzucam wyrazy do odpowiedniego kubełka względem długości
#         buckets[len(el)-1].append(el)
#     for i in range(len(buckets)): # sortuje wewnątrz każdy kubełek radix_sortem
#         radix_sort(buckets[i],i+1)
#     index = 0
#     for bucket in buckets:
#         for el in bucket:
#             Arr[index] = el
#             index += 1
#     return Arr


# print(bucket_sort(words))


# def sort_by_letter(index, words): # index litery na podstawie ktorej bedzie sortowane słowo
#     sorted_words = list()
#     while len(words) > 0:
#         lowest_id = 0 # index słowa pod którym stoi najmniejsza litera alfabetu
#         for i in range(1,len(words)):
#             if ord(words[i][index]) < ord(words[lowest_id][index]):
#                 lowest_id = i
#         sorted_words.append(words[lowest_id])
#         words.pop(lowest_id)
#     return sorted_words


# def lexicalsort(W,a=None,b=None): # words array, range: [a,b)
#     if a is None and b is None: # nie podano przedziału to 3ba go poszukać
#         a = b = 0
#         for word in W: # znajduje przedział długości słów
#             a = min(len(word),a)
#             b = max(len(word),b)

#     buckets = [list() for _ in range(b-a+1)] # tworze kubełki
#     for word in W: # kubełkuje słowa względem długości
#         buckets[len(word)-1].append(word)

#     sorted_W = [None for _ in range(len(W))]
#     j = len(sorted_W)-1 # będę wstawiał do posortowanej tablicy elementy od tylu,
#     n = len(sorted_W)
#     for b_id in range(len(buckets)-1,-2,-1):
#         ready_to_sort = False
#         for word in buckets[b_id]: # wstawiam elementy
#             ready_to_sort = True
#             sorted_W[j] = word
#             j -= 1
#         if ready_to_sort:
#             sorted_W[j+1:n] = sort_by_letter(b_id,sorted_W[j+1:n]) # index litery, tablica, przedział do posortowania
#     return sorted_W
        

# print(lexicalsort(words))


def lex_sort(Arr):
    n = len(Arr)
    max_len = len(Arr[0])
    for el in Arr:
        if len(el) > max_len:
            max_len = len(el)
    buckets = [list() for _ in range(max_len+1)]

    for el in Arr: # wrzucam wyrazy do odpowiedniego kubełka względem długości
        buckets[len(el)-1].append(el)

    buckets[max_len-1] = count_sort(buckets[max_len-1],max_len-1) # ostatni sortuje osobno
    for i in range(max_len-2,-1,-1):
        buckets[i] = count_sort([*buckets[i],*buckets[i+1]],i)

    for i in range(n):
        Arr[i] = buckets[0][i]
    return Arr

n=10
words = [generate_word(n) for _ in range(n)]
print(words)
print(lex_sort(words))