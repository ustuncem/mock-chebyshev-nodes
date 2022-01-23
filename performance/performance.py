import time
import numpy as np

from mockChebyshev import MockChebyshev
from Parser import csv_data
# Measure elapsed time

# Init
mockcheb = MockChebyshev(
    list(csv_data.clean_data["close"].to_dict().keys()), 101)

# Boyd
start = time.time()
boyd = mockcheb.boyd()
end = time.time()

print("Boyd's algorithm, elapsed time: %s" % (end - start))

# İbrahimoğlu
start = time.time()
ibrahimoglu = mockcheb.ibrahimoglu()
end = time.time()

print("Ibrahimoglu's algorithm, elapsed time: %s" % (end - start))
