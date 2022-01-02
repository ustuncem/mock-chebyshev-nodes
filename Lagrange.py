import numpy as np
from pandas.core.frame import DataFrame

class Lagrange:
    
    def __init__(self, data: DataFrame) -> None:
        self.keys = np.array(list(data.keys()), float)
        self.values = np.array(list(data.values()), float)

    def polynomial(self, x):

        sum = 0
        for xi, yi in zip(self.keys, self.values):
            sum += yi * np.prod((x - self.keys[self.keys != xi]) / (xi - self.keys[self.keys != xi]))
        
        return sum