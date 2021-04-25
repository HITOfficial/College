from collections import deque


# będę tworzył drzewo Huffmana na podstawie kopca min

class Huffman_symbol:
    def __init__(self, symbol="", amount=""): # symbol, ilość wystąpień, kod binarny, rodzic, dzieci
        self.childrens = []
        self.binary_digit = ""
        self.symbol = symbol
        self.amount = amount


def symbol_as_object(symbol, amount): # konwertuje każdy symbol wraz z jego wystąpieniem na obiekt
    return Huffman_symbol(symbol,amount)


def return_elements(parent, binary_code=""): # zwracam kompresje bitową każdego symbolu, wraz z ilością bitów potrzebnych na zapisanie ich wszystkich
    count_bits = 0
    if len(parent.childrens) == 0: 
        print(f"{parent.symbol} : {binary_code}{parent.binary_digit}")
        count_bits += parent.amount * len(binary_code+parent.symbol)
    else:
        for children in parent.childrens:
            count_bits += return_elements(children,binary_code+parent.binary_digit)
    return count_bits


def heapyfy(T,n,i): # table, len(T), index rodzica
    n = len(T)
    left = 2*i +1
    right = 2*i +2
    i_copy = i
    if left < n and T[left].amount < T[i_copy].amount: i_copy = left
    if right < n and T[right].amount < T[i_copy].amount: i_copy = right
    if i != i_copy: # znalezione dziecko z wartoscia mniejszą
        T[i], T[i_copy] = T[i_copy], T[i]
        heapyfy(T,len(T), i_copy) # szuka poddzieci do dzieci


def build_heap(T,n): # Tworzymy sens kopca -> każdy rodzic ma mniejsze dzieci
    for i in range(((n//2)-1),-1,-1): # budowa kopca
        heapyfy(T,n,i)


def create_branch(stack):
    heapyfy(stack,len(stack),0) # lewy bit
    left = stack.popleft()
    left.binary_digit = "0" # ustawiam bitowo znak symbolu

    heapyfy(stack,len(stack),0) # prawy bit
    right = stack.popleft()
    right.binary_digit = "1"

    parent = Huffman_symbol()
    parent.childrens.append(left)
    parent.childrens.append(right)
    parent.amount = left.amount+right.amount
    stack.append(parent) # usuwam dwójkę dzieci ze stosu i dodaję rodzica który będzie wskazywał na dzieci
    heapyfy(stack,len(stack),((len(stack)-1)//2)-1)


def branches_tree(stack): # Tworzę gałęzie, kopcem min znajduję dwa najmniejsze elementy dla których tworzę rodzica
    if len(stack)== 1:
        return stack[0]
    else:
        create_branch(stack)
        return branches_tree(stack)


def huffman(S,F):
    stack = deque([symbol_as_object(symbol, amount) for symbol, amount in zip(S,F)]) # Tworzę obiekty z każdego symbolu, oraz jego ilości wystąpień które będę przechowywał w minheap'ie i wyciągał po dwa elementy najmniejsze
    build_heap(stack, len(stack))
    # wyciągam dwa najmniejsze elementy z kopca -> tworzę rodzica, i wrzucam do niego te elementy jako dzieci, rodzic elementów defaultowo będzie miał symbol pustego stringa więc będzie wporządku do odtwarzania
    first = branches_tree(stack)
    return f"dlugosc napisu: {return_elements(first)}"


S = ["a", "b", "c" ,"d", "e", "f"]
F = [10 , 11 , 7 , 13, 1 , 20]

print(huffman(S,F))



    
    