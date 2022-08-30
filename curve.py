import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import numpy as np
class curves():
    def q1(x, a, b):
        return a + b*x
    def q2(x, e, f, g):
        return e + f*x + g*x**2
    def q3(x, h, i):
        return h/x + i*x
    x, y =[1.01,1.27,1.85,2.38,2.83,3.13,3.96,4.91], [0,0.19,0.58,0.96,1.26,1.47,2.07,2.75]
    par1, _ = curve_fit(q1, x, y)
    par2, _ = curve_fit(q2, x, y)
    par3, _ = curve_fit(q3, x, y)
    a, b = par1
    print('y = %.5f + %.5f*x' % (a, b))
    e, f, g = par2
    print('y = %.5f + %.5f*x + %.5f*x**2' % (e, f, g))
    h, i = par3
    print('y = %.5f/x + %.5f*x' % (h, i))   
    plt.scatter(x, y)
    x_axis = np.arange(min(x), max(x), 0.01)
    y_axis1 = q1(x_axis, a, b)
    y_axis2 = q2(x_axis, e, f, g)
    y_axis3 = q3(x_axis, h, i)
    plt.plot(x_axis, y_axis1, '--', color='red')
    plt.plot(x_axis, y_axis2, '--', color='blue')
    plt.plot(x_axis, y_axis3, '--', color='black')
    plt.show()
