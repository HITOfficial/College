# Problem 8 Hetmanów (treść oczywista)
import time

# do n = 14 nie wyrzuca

n= 14
t = [[0 for _ in range(n)] for _ in range(n)]


def n_hetmans_problem(chess_list, new_hetman=(0,0), putted_hetmans=[]):
    flag = False
    if len(putted_hetmans) == len(chess_list):
        putted_hetmans
        flag = True
        return flag
    
    able_to_put_new = False # flaga czy moge nowego wstawić hetmana

    for new_j in range(new_hetman[1], len(chess_list)):
        new_hetman = (new_hetman[0], new_j)
        x = 0
        broke_for = False

        while x < len(chess_list)-1:

            for hetman in putted_hetmans:
                a = (new_hetman[0]+x, new_hetman[1]+x) # differences
                b = (new_hetman[0]-x, new_hetman[1]-x)
                c = (new_hetman[0]-x, new_hetman[1]+x)
                d = (new_hetman[0]+x, new_hetman[1]-x)

                if new_hetman[0] == hetman[0] or new_hetman[1] == hetman[1] or a == hetman or b == hetman or c == hetman or d == hetman:
                    broke_for = True
                    break

            if broke_for == True:
                break
            x += 1

        if broke_for == False:
            able_to_put_new = True
            break
    
    if able_to_put_new == True:
        flag = flag or n_hetmans_problem(chess_list, (new_hetman[0]+1, 0), [*putted_hetmans, new_hetman])
    else:
        new_hetman = putted_hetmans.pop()
        new_hetman = new_hetman[0], new_hetman[1]+1
        flag = flag or n_hetmans_problem(chess_list, (new_hetman), [*putted_hetmans])

    return flag

start = time.time()
print(n_hetmans_problem(t))
print(time.time() - start)
