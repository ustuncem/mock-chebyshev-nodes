from unittest import mock
import numpy as np
from pandas.core.frame import DataFrame
import time
from Parser import data

class MockChebyshev:

    def __init__(self, dataset, point_count_cheb = 15) -> None:
        self.x_cheb_length = point_count_cheb
        self.x_equi_length = len(dataset)
        self.start = dataset[0]
        self.end = dataset[-1]
        self.x_cheb = np.array([0.5 * (self.start + self.end + 2) + 0.5 
                                    * (self.start - self.end) * np.cos(np.pi * j / (point_count_cheb - 1)) 
                                    for j in range(point_count_cheb)])
        self.x_equi = np.array([(-1 + 2* k / (self.x_equi_length - 1)) for k in range(self.x_equi_length)])

    def ibrahimoglu(self):       
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
        x_mockcheb = np.array([])

        for j in self.x_cheb:
            temp = []
            for k in self.x_equi:
                temp.append(abs(j - k))

            x_mockcheb = np.append(x_mockcheb, min(temp))
            
        return np.round(x_mockcheb)

mockcheb = MockChebyshev(list(data.clean_data["Average Closing"].to_dict().keys()), 15)