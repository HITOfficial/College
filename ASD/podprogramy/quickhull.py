from random import randint


def NWD(a, b):
    while b != 0:
        b, a = a % b, b
    return a        


def triangle_area(a,b,c):
    # (bx-ax)*(cy-ay) - (by-ay)*(cx-ax)
    bx_ax = b[0][0]*a[0][1] - a[0][0]*b[0][1],b[0][1]*a[0][1]
    cy_ay = c[1][0]*a[1][1] - a[1][0]*c[1][1],c[1][1]*a[1][1]
    by_ay = b[1][0]*a[1][1] - a[1][0]*b[1][1],b[1][1]*a[1][1]
    cx_ax = c[0][0]*a[0][1] - a[0][0]*c[0][1],c[0][1]*a[0][1]
    bx_ax_cy_ay = bx_ax[0]*cy_ay[0], bx_ax[1]*cy_ay[1]
    by_ay_cx_ax = by_ay[0]*cx_ax[0], by_ay[1]*cx_ax[1]
    area  = bx_ax_cy_ay[0]*by_ay_cx_ax[1] - by_ay_cx_ax[0]*bx_ax_cy_ay[1], bx_ax_cy_ay[1]*by_ay_cx_ax[1]*2
    if area[0] < 0:
        area =  area[0]*(-1), area[1]
    if area[1] < 0:
        area =  area[0], area[1]*(-1)
    area_NWD = NWD(area[0],area[1])
    return area[0]//area_NWD,  area[1]// area_NWD


def quick_hull(Arr):
    if len(Arr) < 5: # mniej niż 3 punkty    
        return Arr
    hulls = list()
    y_min = y_max = x_min = x_max = Arr[0]
    for el in Arr: # szukam min/max
        if el[0][0]/el[0][1] < x_min[0][0]/x_min[0][1]:
            x_min = el
        if el[0][0]/el[0][1] > x_max[0][0]/x_min[0][1]:
            x_max = el
        if el[1][0]/el[1][1] < y_min[1][0]/x_min[1][1]:
            y_min = el
        if el[1][0]/el[1][1] > y_max[1][0]/x_min[1][1]:
            y_max = el
    # jeśli pole jest równe -> pop element
    # del usuwa
    left_triangle = right_triangle = None
    if x_max != y_min != y_max:
        left_triangle = triangle_area(y_min,y_max,x_min)
    if x_min != y_min != y_max:
        right_triangle = triangle_area(y_min,y_max,x_max)

    if left_triangle is not None:
        for i in range(len(Arr)):
            if i < len(Arr):
                if Arr[i] != x_max != y_min != y_max:
                    a1 = triangle_area(Arr[i],x_max,y_min)
                    a2 = triangle_area(Arr[i],x_max,y_max)
                    a3 = triangle_area(Arr[i],y_max,y_min)
                    result = a1[0]*a2[1]*a3[1] + a1[1]*a2[0]*a3[1] * a1[1]*a2[1]*a3[0], a1[1]*a2[1]*a3[1]
                    result_NWD = NWD(result[0], result[1])
                    result = result[0]//result_NWD, result[1]//result_NWD
                    if left_triangle[0] == result[0] and left_triangle[1] == result[1]:
                        del Arr[i] # pole te same, więc pkt znajduje się wewnątrz
    
    if right_triangle is not None:
        for i in range(len(Arr)):
            if i < len(Arr):
                if Arr[i] != x_min != y_min != y_max:
                    a1 = triangle_area(Arr[i],x_min,y_min)
                    a2 = triangle_area(Arr[i],x_min,y_max)
                    a3 = triangle_area(Arr[i],y_max,y_min)
                    result = a1[0]*a2[1]*a3[1] + a1[1]*a2[0]*a3[1] * a1[1]*a2[1]*a3[0], a1[1]*a2[1]*a3[1]
                    result_NWD = NWD(result[0], result[1])
                    result = result[0]//result_NWD, result[1]//result_NWD
                    if right_triangle[0] == result[0] and right_triangle[1] == result[1]:
                        del Arr[i] # pole te same, więc pkt znajduje się wewnątrz

    for i in range(len(Arr)):
        if i > len(Arr)-1:
            break
        if Arr[i] == y_min or Arr[i] == y_max or Arr[i] == x_min or Arr[i] == x_max:
            del Arr[i]

    tmp = quick_hull(Arr)
    return [*hulls,*tmp]

            
n = 100
Arr = [[[randint(1,15),randint(1,15)], [randint(1,15),randint(1,15)]] for _ in range(n)]

print(quick_hull(Arr))