from unittest import mock
import numpy as np
from pandas.core.frame import DataFrame
import time
from Parser import data

class MockChebyshev:
    """ MockChebyshev Method Container Class
    """

    def __init__(self, dataset: list, point_count_cheb: int = 15) -> None:
        """Constructor

        Args:
            dataset (list): x-values of the data. Should be equally distanced
            point_count_cheb (int, optional): (n+1) number of points, degree of the mock-Chebyshev polynomial will be n. Defaults to 15.
        """
        self.x_cheb_length = point_count_cheb
        self.x_equi_length = len(dataset)
        self.start = dataset[0]
        self.end = dataset[-1]
        self.x_cheb = np.array([0.5 * (self.start + self.end + 2) + 0.5 
                                    * (self.start - self.end) * np.cos(np.pi * j / (point_count_cheb - 1)) 
                                    for j in range(point_count_cheb)])
        self.x_equi = np.array([(-1 + 2* k / (self.x_equi_length - 1)) for k in range(self.x_equi_length)])

    def ibrahimoglu(self) -> list:
        """ İbrahimoğlu's Mock-Chebyshev node selection algorithm

        TODO: Return type should be a NumPy Array. Also degree could be set on the function itself, rather than the constructor. 

        Returns:
            list: Selected mock-Chebyshev nodes of the self.dataset.
        """
        degree = self.x_cheb_length - 1

        i = j = k = 1 
        h = []

        while i <= degree:
            h.append(self.x_cheb[i] - self.x_cheb[i-1])
            i = i + 1
        
        h_min = min(h)
        S = [0]

        while j <= degree:
            S.append(np.round(h[j - 1] / h_min) + S[j - 1])
            j = j + 1

        h_delta = (self.end - self.start) / S[degree]
        mockcheb = [self.x_cheb[0]]

        while k <= degree:
            mockcheb.append(self.x_cheb[0] + S[k] * h_delta)
            k = k + 1

        return np.round(mockcheb)
        
    def boyd(self):
        """ Boyd's Mock-Chebyshev node selection algorithm

        Returns:
            NumPy List: Selected mock-Chebyshev nodes of the self.dataset.
        """
        x_mockcheb = np.array([])

        for j in self.x_cheb:
            temp = []
            for k in self.x_equi:
                temp.append(abs(j - k))

            x_mockcheb = np.append(x_mockcheb, min(temp))
            
        return np.round(x_mockcheb)

mockcheb = MockChebyshev(list(data.clean_data["Average Closing"].to_dict().keys()), 15)