# Rozwiazanie polega na znalezieniu wszystkich najdłuższych podciągów, i markowaniu ich w osobnej tablicy -> O(n^2)
# następnie przy użyciu stosów odtwarzam najdłuższe ciągi
A =[2,1,4,3,5,2,6]

Paths_Stack = list() # w zmiennej globalnej będę zapisywał odtwarzane ścieżki

def LIS(Arr,Pull,Path,index,maximum):
    if maximum == 1: # utworzyło już wszystkie możliwe podciągi o maxymalnej długości
        Paths_Stack.append([*Path]) # ponieważ cały czas działam na referencji do tej samej tablicy, potrzebuje kopiować ich aktualny stan
        return 0

    counter = 0
    Stack = list()
    new_Path = False # żeby parę razy nie uwzgędniać aktualnie zwracanej ścieżki, używam flagi aby to rozpoznać

    for i in range(index-1,-1,-1):
        if Arr[i]<Arr[index] and Pull[i] >= maximum-1: # skladam na stos kolejne podciagi, ktore bede odtwarzal       >= <- ponieważ dla aktualnie odtwarzanego podciągu może być to ostatni elemenet, a w innym może być wcześniejszym 
            Stack.append(i)
            if new_Path is True:
                counter += 1 # znalazlo kolejne podciągi konczace sie na tym elemencie
            new_Path = True
    Path[0:maximum-1] = [None]* (maximum-1)
    for k in Stack:
        Path[maximum-2] = Arr[k]
        counter += LIS(Arr,Pull,Path,k,maximum-1)
    return counter


def printAllLIS(A):
    Arr = A # na referencji operuje na zmiennej Arr, bo sie do niej przyzwyczailem
    n = len(Arr)
    Pull = [1]* n # dlugosci, poszczegolnych sciezek
    for i in range(n):
        longest = Pull[i];
        for j in range(0,i):
            if Arr[j] < Arr[i] and Pull[j]+1 > longest:
                longest = Pull[j] + 1
        Pull[i] = longest
    maximum = max(Pull)
    counter = 0 # licznik znalezionych podciągów

    for index in range(n):
        if Pull[index] == maximum: # na tym elemencie konczy sie najdluzszy podciag
            counter += 1
            Path = [None]*maximum
            Path[maximum-1]= Arr[index] # wrzucam ostatni element jako koniec LIS'a
            counter += LIS(Arr,Pull,Path,index,maximum)

    for i in range(len(Paths_Stack)-1,-1,-1): # zwracam najdłuższe ciągi
        print(Paths_Stack[i])
    return counter


print(printAllLIS(A))