# Rozwiazanie polega na znalezieniu wszystkich najdłuższych podciągów, i markowaniu ich w osobnej tablicy -> O(n^2)
# liniowo szukam tych podciągów -> rozpakowywuje pierwszy znaleziony, zakończony na danym indexie, pozostałe zapamiętuje i zapisuje na stosie, który w indentyczny sposob odtwarzam 
# Wydaje mi się że złożoność ALGO to O(n^2) -> wytlumaczylem w lini 49

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
            pivot = Arr[index]
            j = maximum-2 # odtwarzam sciezke, nadpisujac elementy od konca
            Stack = list() # robie stos aby zapamietac, kolejne podciagi spełniajace warunku
            for i in range(index-1,-1,-1):
                if Arr[i]<pivot and Pull[i] == j+1:
                    pivot = Arr[i]
                    Path[j] = Arr[i]
                    j -= 1
                elif Arr[i]<Arr[index] and Pull[i] == maximum-1: # skladam na stos kolejne podciagi, ktore bede odtwarzal
                    Stack.append(i)
                    counter += 1 # znalazlo kolejne podciągi konczace sie na tym elemencie
            print(Path)

            for k in Stack: # wypakowywuje stos (odtwarzam podciagi)
                Path = [None]*maximum
                Path[maximum-1]= Arr[index]
                Path[maximum-2] = Arr[k]
                pivot = Arr[k]
                j = maximum-3
                for i in range(k-1,-1,-1):
                    if Arr[i]<pivot and Pull[i] == j+1:
                        pivot = Arr[i]
                        Path[j] = Arr[i]
                        j -= 1 
                    if j == -1: # gdy stack będzie O(n) to ścieżki będą max: O(2) -> więc nadrobi straty w złożoności nadmieniając O(n^3) -> O(n^2)
                        break
                print(Path)

    return counter
