# Otrzymujemy na wejściu listę par ludzi, które się wzajemnie znają. Osoby są reprezentowane przez liczby od 0 do n - 1.
# Dnia pierwszego osoba 0 przekazuje pewną wiadomość wszystkim swoim znajomym. Dnia drugiego każdy ze znajomych przekazuje tę wiadomość wszystkim swoim znajomym, którzy jej jeszcze nie znali, i tak dalej.
# Napisz algorytm, który zwróci dzień, w którym najwięcej osób poznało wiadomość oraz ilość osób, które tego dnia ją otrzymały.

from queue import Queue # last in first out queue

g = [
    [1,7],
    [2,3,7],
    [1,4],
    [1,4],
    [2,3,5],
    [6,4],
    [5],
    [0,1]
]

# I'll solve its using BFS alghoritm
def bfs_messages(graph,vertex):
    got_msg = [False] * len(graph) # I'll mark used vertex
    best_day = -1
    day = -1
    queue = Queue()
    queue.put(vertex)
    max_msg = 0
    people = []

    while queue.qsize() > 0:
        day += 1
        count_msg = 0
        next_queue = Queue()
        tmp_people = [] # in this stack i'll merorize actual messages
        while queue.qsize() > 0: # for actual day I need to unzip all childrens
            actual_vertex = queue.get()
            if got_msg[actual_vertex]:
                continue
            else:
                count_msg += 1 # he did not recive message
                got_msg[actual_vertex] = True
                tmp_people.append(actual_vertex)
                for v in graph[actual_vertex]:
                    if got_msg[v] is False:
                        next_queue.put(v)
        queue = next_queue

        if max_msg < count_msg:
            max_msg = count_msg
            people = tmp_people.copy()
            best_day = day

    return f"Messages: {max_msg}, People: {people}, Day: {best_day}"


print(bfs_messages(g,0))

