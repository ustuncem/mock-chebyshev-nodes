import time
from mockChebyshev import mockcheb
# Measure elapsed time

# Boyd
start = time.time()
mockcheb.boyd(15, 85)
end = time.time()

print("Boyd's algorithm, elapsed time: %s" %(end - start))

# İbrahimoğlu
start = time.time()
mockcheb.ibrahimoglu(85)
end = time.time()

print("Ibrahimoglu's algorithm, elapsed time: %s" %(end - start))