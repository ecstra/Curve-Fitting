import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

class curve:
    n = int(input("Enter number of elements : "))
    x = list(map(float,input("\nEnter x : ").strip().split(",")))[:n]
    y = list(map(float,input("\nEnter y : ").strip().split(",")))[:n]
    X = [None] * len(x)
    for i in range(len(x)):
        X[i] = 1/x[i]
        X[i] = float("{:.2f}".format(X[i]))
    sX = sum(X)
    x2 = np.square(x)
    xy = np.multiply(x, y)
    sx = np.sum(x)
    sy = np.sum(y)
    sx2 = np.sum(x2)
    sxy = np.sum(xy)
    yx2 = np.multiply(y, x2)
    syx2 = np.sum(yx2)
    x3 = np.multiply(x, x2)
    sx3 = np.sum(x3)
    x4 = np.square(x2)
    sx4 = np.sum(x4)
    a, b, e, f, g, h, i = sp.symbols('a b e f g h i')
    eq1 = sp.Eq(n*a + b*sx, sy)
    eq2 = sp.Eq(a*sx + b*sx2, sxy)
    eq11 = sp.Eq(n*e + f*sx + g*sx2, sy)
    eq12 = sp.Eq(e*sx + f*sx2 + g*sx3, sxy)
    eq13 = sp.Eq(e*sx2 + f*sx3 + g*sx4, syx2)
    eq21 = sp.Eq(h*sX + i*sx, sy)
    eq22 = sp.Eq(h*n + i*sx2, sxy)
    sol1 = sp.solve((eq1, eq2),(a, b))
    sol2 = sp.solve((eq11, eq12, eq13),(e, f, g))
    sol3 = sp.solve((eq21, eq22),(h, i))
    print('y = %.5f + %.5f*x' % (sol1[a], sol1[b]))
    print('y = %.5f + %.5f*x + %.5f*x**2' % (sol2[e], sol2[f], sol2[g]))
    print('y = %.5f/x + %.5f*x' % (sol3[h], sol3[i]))
    def q1(x, a, b):
        return a + b*x
    def q2(x, e, f, g):
        return e + f*x + g*x**2
    def q3(x, h, i):
        return h/x + i*x
    plt.scatter(x, y)
    x_axis = np.arange(min(x), max(x), 0.01)
    y_axis1 = q1(x_axis, sol1[a], sol1[b])
    y_axis2 = q2(x_axis, sol2[e], sol2[f], sol2[g])
    y_axis3 = q3(x_axis, sol3[h], sol3[i])
    plt.plot(x_axis, y_axis1, '--', color='red')
    plt.plot(x_axis, y_axis2, '--', color='blue')
    plt.plot(x_axis, y_axis3, '--', color='black')
    plt.show()