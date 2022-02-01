import numpy as np
import matplotlib.pyplot as plt
import time

from src.mockChebyshev import MockChebyshev
from src.Parser import csv_data

xplt = {
    21: 169,
    31: 379,
    41: 667,
    51: 1035,
    61: 1487,
    71: 2015,
    81: 2625,
    91: 3325,
    101: 4099,
}

yplt_boyd = []
yplt_ibrahimoglu = []

for i in xplt:
    mockcheb = MockChebyshev(
        list(csv_data.clean_data["close"].head(xplt[i]).to_dict().keys()), i)

    start = time.time()
    boyd = mockcheb.boyd()
    end = time.time()

    yplt_boyd.append(end-start)

    start = time.time()
    boyd = mockcheb.ibrahimoglu()
    end = time.time()

    yplt_ibrahimoglu.append(end-start)

plt.title("Performance Difference")
plt.xlabel("Degree")
plt.ylabel("Time Took")

plt.xticks([i - 1 for i in list(xplt.keys())])
plt.plot([i - 1 for i in list(xplt.keys())], yplt_boyd, color="#E51A7C", label="Boyd's Algorithm")
plt.plot([i - 1 for i in list(xplt.keys())], yplt_ibrahimoglu, color="#0539f7", label="İbrahimoğlu's Algorithm")

plt.legend(loc="upper left")

plt.show()
