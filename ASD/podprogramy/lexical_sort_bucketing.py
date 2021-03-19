from random import randint

def generate_word(n): # max_word len
    letters = "abcdefghijklmnouprstwyzx"
    word = ""
    for _ in range(randint(1,n)): # założenie, przynajmniej jedno wyrazowe słowo
        word += letters[randint(0,len(letters)-1)] # losuje index litery z alfabetu
    return word


def sort_by_letter(index, words): # index litery na podstawie ktorej bedzie sortowane słowo
    sorted_words = list()
    while len(words) > 0:
        lowest_id = 0 # index słowa pod którym stoi najmniejsza litera alfabetu
        for i in range(1,len(words)):
            if ord(words[i][index]) < ord(words[lowest_id][index]):
                lowest_id = i
        sorted_words.append(words[lowest_id])
        words.pop(lowest_id)
    return sorted_words


def lexicalsort(W,a=None,b=None): # words array, range: [a,b)
    if a is None and b is None: # nie podano przedziału to 3ba go poszukać
        a = b = 0
        for word in W: # znajduje przedział długości słów
            a = min(len(word),a)
            b = max(len(word),b)

    buckets = [list() for _ in range(b-a+1)] # tworze kubełki
    for word in W: # kubełkuje słowa względem długości
        buckets[len(word)-1].append(word)

    sorted_W = [None for _ in range(len(W))]
    j = len(sorted_W)-1 # będę wstawiał do posortowanej tablicy elementy od tylu,
    n = len(sorted_W)
    for b_id in range(len(buckets)-1,-2,-1):
        ready_to_sort = False
        for word in buckets[b_id]: # wstawiam elementy
            ready_to_sort = True
            sorted_W[j] = word
            j -= 1
        if ready_to_sort:
            sorted_W[j+1:n] = sort_by_letter(b_id,sorted_W[j+1:n]) # index litery, tablica, przedział do posortowania
    return sorted_W
        

n=10
words = [generate_word(n) for _ in range(n)]
print(lexicalsort(words))