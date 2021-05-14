# ALGORITHM https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9

# Cersei i Jaime mają 3 - letniego syna. Przygotowali listę N aktywności podanych jako pary,
# reprezentujące czas rozpoczęcia i zakończenia danej aktywności. Zaimplementuj algorytm,
# który przyporządkuje każdej aktywności literę C lub J, oznaczającą, że daną aktywność z synem wykona
# odpowiednio Cersei lub Jaime, w taki sposób, że żaden rodzic nie wykonuje pokrywających się czasowo aktywności. Jeżeli takie przyporządkowanie nie istnieje, to algorytm zwraca “IMPOSSIBLE”, a jeśli istnieje, to zwraca odpowiedniego stringa.
from queue import Queue

t_impossible = [(99,150),(1,100),(2,3),(100,301),(2,5),(150,250)]
t_possible = [(99,150),(1,100),(100,301),(2,5),(150,250)]

def childcare(times): # greedy method algorithm
    # sort times by duty start
    times.sort(key=lambda item: item[0])

    result = str()
    C = [(-float("inf"),-float("inf")), "C"] 
    J = [(-float("inf"),-float("inf")), "D"] 
    queue = Queue()
    for el in times: # becouse pop() on normal array takes(O(n)), i'll work on queue to take O(1), to take item
        queue.put(el)
    
    while not queue.empty():
        duty = queue.get()
        if C[0][1] <= duty[0]:
            result += C[1] # duty to Cersei
            C = [duty ,C[1]]
        elif J[0][1] <= duty[0]:
            result += J[1] # duty to Cersei
            J = [duty ,J[1]]
        else:
            return "IMPOSSIBLE"
    
    return result


print(childcare(t_possible))
print(childcare(t_impossible))
