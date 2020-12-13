import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt
 

t = [3,4,5]


def zip_with(func, list1, list2):
    if not list1 or not list2:
        return []
    last1 = list1.pop()
    last2 = list2.pop()
    # [1+3,2+4]
    result = zip_with(func, list1, list2)
    result.append(func(last1, last2))
    return result
    




if __name__ == "__main__":

    functions = [lambda x,y: sqrt(x*x +y*y),
                lambda x,y: x+y,
                lambda x,y: 4,
                ]
    
    fig = plt.figure()
    ax = Axes3D(fig)
 
    xs = [i/3 for j in range(-10, 11) for i in range(-10, 11)]
    ys = [i/3 for i in range(-10, 11) for j in range(-10, 11)]
    
    zs = zip_with(functions[0], xs.copy(), ys.copy())
    print(len(xs), len(ys), len(zs))
    ax.scatter(xs, ys, zs)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    fig.add_axes(ax)
    plt.show()

