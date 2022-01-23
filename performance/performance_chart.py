import numpy as np
import matplotlib.pyplot as plt
import time

from src.mockChebyshev import MockChebyshev
from src.Parser import csv_data

xplt = {
    10: 42,
    20: 170,
    50: 1020,
    100: 4099
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

plt.xticks(list(xplt.keys()))
plt.plot(list(xplt.keys()), yplt_boyd, color="#E51A7C")
plt.plot(list(xplt.keys()), yplt_ibrahimoglu, color="#0539f7")

plt.show()
