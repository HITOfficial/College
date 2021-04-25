from collections import deque


# zamysł: Tworzę drzewo Huffmana i na podstawie kopca minimum, zaimplementowanego na stosie, wyciągam po dwa najmniejsze elementy które scalam, i nakierowywuje na nie tymczasowego rodzica, następnie znaczę dzieci bitowo 0/1 i wykonuję tą samą operację aż pozostanie mi ostatni element na stosie
# po zaznaczeniu bitowym wszystkich elementów odtwarzam wszystkie gałęzie drzewa, gromadząc  bity z gałęzi potrzebne na zapisanie każdego słowa
# złożoność pamięciowa O(n) -> tworze dwie tablicę jedną do zbudowania gałęzi w drzewie Huffmana, drugą jako odtworzenie ścieżki
# zlozoność obliczeniowa O(nlog(n)) -> budowa całego drzewa, aż do korzenia, wbudowany sort, przy odtwarzaniu ścieżki

# zaimplementowałem własną PriorityQueue a kożystam tylko z wbudowanej ogólnej koleiki

class Huffman_symbol:
    def __init__(self, symbol="", amount="", main_index=0): # symbol, ilość wystąpień, index w tablicy wejściowej
        self.main_index = main_index
        self.childrens = []
        self.binary_digit = ""
        self.symbol = symbol
        self.amount = amount


def symbol_as_object(symbol, amount,index): # konwertuje każdy symbol wraz z jego wystąpieniem na obiekt
    return Huffman_symbol(symbol,amount, index)


def return_elements(parent, binary_code=""): # zwracam kompresje bitową każdego symbolu, wraz z ilością bitów potrzebnych na zapisanie ich wszystkich
    count_bits = 0 # zbieram ilość bitów potrzebną na zapisanie słowa
    indexes_array = []
    if len(parent.childrens) == 0: # dochodzi do liścia z danej gałęzi
        indexes_array.append([binary_code+parent.binary_digit, parent.main_index]) # wkładam element na stos, który następnie odtworzy ścieżkę, w kolejności danych na wejściu
        count_bits += parent.amount * len(binary_code+parent.symbol) # zliczam bity potrzebne na zapisanie wszystkich tych samych symboli
    else:
        for children in parent.childrens:
            bits, indexes = return_elements(children,binary_code+parent.binary_digit)
            count_bits += bits
            indexes_array += indexes
    return count_bits, indexes_array


def heapyfy(T,i): # table, len(T), index rodzica
    n = len(T)
    left = 2*i +1
    right = 2*i +2
    i_copy = i
    if left < n and T[left].amount < T[i_copy].amount: i_copy = left
    if right < n and T[right].amount < T[i_copy].amount: i_copy = right
    if i != i_copy: # znalezione dziecko z wartoscia mniejszą
        T[i], T[i_copy] = T[i_copy], T[i]
        heapyfy(T, i_copy) # szuka poddzieci do dzieci


def build_heap(T,n): # Tworzymy sens kopca minimum -> każdy rodzic ma większe dzieci
    for i in range(((n//2)-1),-1,-1): # budowa kopca
        heapyfy(T,i)


def create_branch(stack):
    heapyfy(stack,0) # lewy bit
    left = stack.popleft()
    left.binary_digit = "1" # ustawiam bitowo znak symbolu

    heapyfy(stack,0) # prawy bit
    right = stack.popleft()
    right.binary_digit = "0"

    parent = Huffman_symbol()
    parent.childrens.append(left) # dodaję dzieci
    parent.childrens.append(right)
    parent.amount = left.amount+right.amount
    stack.append(parent) # usuwam dwójkę dzieci ze stosu i dodaję rodzica który będzie wskazywał na dzieci
    build_heap(stack,len(stack)) # ponieważ dodaje element na koniec, musiał bym iteracyjnie przelecieć po wszystkich rodzicach, więc korzystam juz z zaimplementowanej budowy kopca


def branches_tree(stack): # Tworzę gałęzie, kopcem min znajduję dwa najmniejsze elementy dla których tworzę rodzica
    if len(stack)== 1:
        return stack[0]
    else:
        create_branch(stack)
        return branches_tree(stack)


def huffman(S,F):
    stack = deque([symbol_as_object(symbol, amount, index) for symbol, amount, index in zip(S,F,range(len(S)))]) # Tworzę obiekty z każdego symbolu, oraz jego ilości wystąpień które będę przechowywał w minheap'ie i wyciągał po dwa elementy najmniejsze
    build_heap(stack, len(stack)) # tworze kopiec min
    first = branches_tree(stack) # wyciągam dwa najmniejsze elementy z kopca -> tworzę rodzica, i wrzucam do niego te elementy jako dzieci, rodzic elementów defaultowo będzie miał symbol pustego stringa
    bits_sum, binary_code_arr = return_elements(first) # odtwarzam ścieżkę, i zbieram bity potrzebne na zapisanie danych
    binary_code_arr.sort(key=lambda item: item[1]) # sortuje po indexach zeby odtworzyć w wejsciowej kolejnosci
    for item in binary_code_arr:
        print(f"{S[item[1]]} : {item[0]}")
        
    print(f"dlugosc napisu : {bits_sum}")
    return ""


S = ["a", "b", "c" ,"d", "e", "f"]
F = [10 , 11 , 7 , 13, 1 , 20]

print(huffman(S,F))



    
    