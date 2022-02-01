import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline

from .Parser import data
from .Lagrange import Lagrange
from .mockChebyshev import mockcheb

# Visualize Lagrange
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
        y_axis = np.append(
            y_axis, lagrange.values[int(i)] - lagrange.polynomial(i))

    plt.xticks(xticks + 1)
    plt.bar(x_axis, y_axis, color="#E51A7C")
    plt.show()


def lagrange_mockcheb_graph():
    xplt = mockcheb.boyd()
    yplt = np.array([data.clean_data["Average Closing"][int(i)] for i in xplt])
    yplt_vals = np.array([], float)

    for i in xplt:
        yplt_vals = np.append(
            yplt_vals, lagrange.polynomial_mockcheb(i, xplt, yplt))

    xplt_new = xplt + 1
    xplt_smooth = np.linspace(xplt[0], xplt[-1], 300)
    splt = make_interp_spline(xplt, yplt_vals, k=3)
    yplt_smooth = splt(xplt_smooth)

    plt.title("Boyd's Method (n = 14)")
    plt.xlabel("Days")
    plt.ylabel("Average Closing")

    plt.bar(lagrange.keys + 1, lagrange.values, color="#1ae583")
    plt.bar(xplt + 1, yplt_vals, color="#FA491B")
    plt.xticks(xplt_new)
    plt.plot(xplt_smooth + 1, yplt_smooth, color="#E51A7C")
    plt.plot(xplt_new, yplt_vals, 'o', color="#0539f7")

    plt.show()


def lagrange_boyd_errors_graph():
    plt.title("Boyd's Method - Errors")
    plt.xlabel("Days")
    plt.ylabel("Error")

    xplt = mockcheb.boyd()
    yplt = np.array([data.clean_data["Average Closing"][int(i)] for i in xplt])

    x_axis = np.arange(lagrange.keys[0], lagrange.keys[-1] + 1)
    y_axis = np.array([], float)

    for i in x_axis:
        y_axis = np.append(y_axis, lagrange.values[int(
            i)] - lagrange.polynomial_mockcheb(i, xplt, yplt))

    plt.xticks(xplt + 1)
    plt.bar(x_axis + 1, np.round(y_axis)+0.05, color="#E51A7C")
    plt.show()


def lagrange_mockcheb_ibrahimoglu_graph():
    xplt = mockcheb.ibrahimoglu() - 1
    yplt = np.array([data.clean_data["Average Closing"][int(i)] for i in xplt])
    yplt_vals = np.array([], float)

    for i in xplt:
        yplt_vals = np.append(
            yplt_vals, lagrange.polynomial_mockcheb(i, xplt, yplt))
    xplt_new = xplt + 1
    xplt_smooth = np.linspace(xplt[0], xplt[-1], 300)
    splt = make_interp_spline(xplt, yplt_vals, k=3)
    yplt_smooth = splt(xplt_smooth)

    plt.title("İbrahimoğlu's Method (n = 14)")
    plt.xlabel("Days")
    plt.ylabel("Average Closing")

    plt.bar(lagrange.keys + 1, lagrange.values, color="#1ae583")
    plt.bar(xplt + 1, yplt_vals, color="#FA491B")
    plt.xticks(xplt_new)
    plt.plot(xplt_smooth + 1, yplt_smooth, color="#E51A7C")
    plt.plot(xplt_new, yplt_vals, 'o', color="#0539f7")

    plt.show()


def lagrange_ibrahimoglu_errors_graph():
    plt.title("İbrahimoğlu's Method - Errors")
    plt.xlabel("Days")
    plt.ylabel("Error")

    xplt = mockcheb.ibrahimoglu() - 1
    yplt = np.array([data.clean_data["Average Closing"][int(i)] for i in xplt])

    x_axis = np.arange(lagrange.keys[0], lagrange.keys[-1] + 1)
    y_axis = np.array([], float)

    for i in x_axis:
        y_axis = np.append(y_axis, lagrange.values[int(
            i)] - lagrange.polynomial_mockcheb(i, xplt, yplt))

    plt.xticks(xplt + 1)
    plt.bar(x_axis + 1, np.round(y_axis)+0.05, color="#E51A7C")
    plt.show()


lagrange_graph()
lagrange_errors_graph()
lagrange_mockcheb_graph()
lagrange_boyd_errors_graph()
lagrange_mockcheb_ibrahimoglu_graph()
lagrange_ibrahimoglu_errors_graph()
