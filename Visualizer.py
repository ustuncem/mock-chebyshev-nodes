from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import numpy as np
from Parser import data
from Lagrange import Lagrange

#Visualize Lagrange
lagrange = Lagrange(data.clean_data["Average Closing"].to_dict())

xplt = np.arange(lagrange.keys[0], lagrange.keys[-1] + 1, step=6)

yplt = np.array([], float)

for i in xplt:
    yplt = np.append(yplt, lagrange.polynomial(i))

plt.title("Lagrange Interpolation")
plt.xlabel("Days")
plt.ylabel("Average Closing")
plt.xticks(xplt + 1)
plt.bar(lagrange.keys, lagrange.values, color="#1ae583")
plt.plot(xplt, yplt, 's-', color="#1ae583")
plt.plot(xplt, yplt, 's-', color="#E51A7C")

plt.show()

#Visualize mock-Chebyshev