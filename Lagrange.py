import numpy as np
from pandas.core.frame import DataFrame

class Lagrange:
    
    def __init__(self, data: DataFrame) -> None:
        self.keys = np.array(list(data.keys()), float)
        self.values = np.array(list(data.values()), float)

    def polynomial(self, x):
        xplt = np.arange(self.keys[0], self.keys[-1] + 1, step=6)
        yplt = np.array([self.values[i] for i in range(len(self.values)) if i % 6 == 0], float)

        sum = 0
        for xi, yi in zip(xplt, yplt):
            sum += yi * np.prod((x - xplt[xplt != xi]) / (xi - xplt[xplt != xi]))
        
        return sum

    def polynomial_mockcheb(self, x, x_axis, y_axis):

        sum = 0
        for xi, yi in zip(x_axis, y_axis):
            sum += yi * np.prod((x - x_axis[x_axis != xi]) / (xi - x_axis[x_axis != xi]))
        
        return sum
    