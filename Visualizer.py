import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline

from Parser import data
from Lagrange import Lagrange
from mockChebyshev import mockcheb

#Visualize Lagrange
lagrange = Lagrange(data.clean_data["Average Closing"].to_dict())

# Smooth Curve
def lagrange_graph(): 
    xplt = np.arange(lagrange.keys[0], lagrange.keys[-1] + 1, step=6)
    yplt = np.array([], float)

    xplt_test = np.arange(lagrange.keys[0], lagrange.keys[-1] + 1, step=3)
    yplt_test = np.array([], float)

    for i in xplt:
        yplt = np.append(yplt, lagrange.polynomial(i))

    for i in xplt_test:
        yplt_test = np.append(yplt_test, lagrange.polynomial(i))

    xplt_new = xplt + 1
    xplt_test = xplt_test + 1
    xplt_smooth = np.linspace(xplt_test[0], xplt_test[-1], 300)
    splt = make_interp_spline(xplt_test, yplt_test, k=3)
    yplt_smooth = splt(xplt_smooth) 

    plt.title("Lagrange Interpolation")
    plt.xlabel("Days")
    plt.ylabel("Average Closing")

    plt.bar(lagrange.keys + 1, lagrange.values, color="#1ae583")
    plt.xticks(xplt_new) 
    plt.plot(xplt_smooth, yplt_smooth, color="#E51A7C")

    plt.show()

def lagrange_errors_graph(): 
    plt.title("Lagrange Interpolation Errors ")
    plt.xlabel("Days")
    plt.ylabel("Error")

    xticks = np.arange(lagrange.keys[0], lagrange.keys[-1] + 1, step=6)

    x_axis = np.arange(lagrange.keys[0], lagrange.keys[-1] + 1)
    y_axis = np.array([], float)
    
    for i in x_axis:
        print(lagrange.values[int(i)], lagrange.polynomial(i), lagrange.values[int(i)] - lagrange.polynomial(i))
        y_axis = np.append(y_axis, lagrange.values[int(i)] - lagrange.polynomial(i))

    # plt.xticks(xticks + 1)
    # plt.bar(x_axis, y_axis, color="#E51A7C")
    # plt.show()

def lagrange_mockcheb_graph(): 
    xplt = mockcheb.boyd(15, len(data.clean_data["Average Closing"]))
    yplt = np.array([data.clean_data["Average Closing"][int(i)] for i in xplt])

    xplt_test = np.arange(lagrange.keys[0], lagrange.keys[-1] + 1, step=3)
    yplt_test = np.array([], float)

    for i in xplt:
        yplt = np.append(yplt, lagrange.polynomial_mockcheb(i, xplt, yplt))

    for i in xplt_test:
        yplt_test = np.append(yplt_test, lagrange.polynomial_mockcheb(i, xplt, yplt))

    xplt_new = xplt + 1
    xplt_test = xplt_test + 1
    xplt_smooth = np.linspace(xplt_test[0], xplt_test[-1], 300)
    splt = make_interp_spline(xplt_test, yplt_test, k=3)
    yplt_smooth = splt(xplt_smooth) 

    plt.title("mock-Chebyshev Polynomial Interpolation")
    plt.xlabel("Days")
    plt.ylabel("Average Closing")

    plt.bar(lagrange.keys + 1, lagrange.values, color="#1ae583")
    plt.xticks(xplt_new) 
    plt.plot(xplt_smooth, yplt_smooth, color="#E51A7C")

    plt.show()

def lagrange_mockcheb_ibrahimoglu_graph(): 
    xplt = mockcheb.ibrahimoglu(15) - 1
    yplt = np.array([data.clean_data["Average Closing"][int(i)] for i in xplt])

    xplt_test = np.arange(lagrange.keys[0], lagrange.keys[-1] + 1, step=3)
    yplt_test = np.array([], float)

    for i in xplt:
        yplt = np.append(yplt, lagrange.polynomial_mockcheb(i, xplt, yplt))

    for i in xplt_test:
        yplt_test = np.append(yplt_test, lagrange.polynomial_mockcheb(i, xplt, yplt))

    xplt_new = xplt + 1
    xplt_test = xplt_test + 1
    xplt_smooth = np.linspace(xplt_test[0], xplt_test[-1], 300)
    splt = make_interp_spline(xplt_test, yplt_test, k=3)
    yplt_smooth = splt(xplt_smooth) 

    plt.title("mock-Chebyshev Polynomial Interpolation")
    plt.xlabel("Days")
    plt.ylabel("Average Closing")

    plt.bar(lagrange.keys + 1, lagrange.values, color="#1ae583")
    plt.xticks(xplt_new) 
    plt.plot(xplt_smooth, yplt_smooth, color="#E51A7C")

    plt.show()

lagrange_mockcheb_ibrahimoglu_graph()