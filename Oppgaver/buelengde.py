
import matplotlib.pyplot as plt
from numpy import linspace
import math


def f(x):
    return x**2


def g(x):
    return 2/3*(x**2-1)^(3/2)


def get_dist(x, y):

    l = [[x[i], y[i]] for i in range(len(x))]
    print("l", l)

    total_dist = 0
    for i in range(len(l)-1):
        x, y = l[i][0], l[i][1]
        nx, ny = l[i+1][0], l[i+1][1]
        dist = math.sqrt((nx-x)**2 + (ny-y)**2)
        print("dist", x, nx, y, ny, dist)
        total_dist += dist

    return total_dist


def buelengde(f, a, b, n, m):
    """
        f: function 
        [a, b]: interval
        n: number of calculated f(x) values
        m: number of points calculated for arc length

    """
    x_f_values = [x for x in linspace(a, b, n)]
    f_values = [f(x) for x in x_f_values]

    x_arc_values = [x for x in linspace(a, b, m)]
    arc_values = [f(x) for x in x_arc_values]

    dist = get_dist(x_arc_values, arc_values)
    print(f"Buelengde fra {a} til {b} for f(x): {dist}")

    plt.plot(x_f_values, f_values)
    plt.plot(x_arc_values, arc_values)
    plt.show()


buelengde(f, 1, 10, 1000, 10)
