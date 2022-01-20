import numpy as np
from pandas.core.frame import DataFrame

class Lagrange:
    """Lagrange Polynomial Calculator 1.0.0

    TODO: Merge polynomial functions, polynomial() is unnecessary
    """
    
    def __init__(self, data: DataFrame) -> None:
        """Initialization of Lagrange Class

        Args:
            data (DataFrame): Key-Value pair for the construction of the Lagrange interpolants.
        """
        self.keys = np.array(list(data.keys()), float)
        self.values = np.array(list(data.values()), float)

    def polynomial(self, x: int or float) -> int or float:
        """ Method to construct Lagrange Interpolation Polynomial for a specific subset.
        
        DEPRECATION NOTICE. FUNCTION USAGE WILL CHANGE, USE IN CAUTION

        Args:
            x (int or float): Value of the x-axis.

        Returns:
            int or float: y-value of x.
        """

        xplt = np.arange(self.keys[0], self.keys[-1] + 1, step=6)
        yplt = np.array([self.values[i] for i in range(len(self.values)) if i % 6 == 0], float)

        sum = 0
        for xi, yi in zip(xplt, yplt):
            sum += yi * np.prod((x - xplt[xplt != xi]) / (xi - xplt[xplt != xi]))
        
        return sum

    def polynomial_mockcheb(self, x: int or float, x_axis, y_axis)-> int or float:
        """Main Method to construct Lagrange Interpolation Polynomial

        Args:
            x (intorfloat): Desired value to observe
            x_axis (NumPy Array): values for x 
            y_axis (NumPy Array): values for y

        Returns:
            int or float: Value of x in the interpolation polynomial
        """
        sum = 0
        for xi, yi in zip(x_axis, y_axis):
            sum += yi * np.prod((x - x_axis[x_axis != xi]) / (xi - x_axis[x_axis != xi]))
        
        return sum
    