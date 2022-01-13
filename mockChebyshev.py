import numpy as np
from pandas.core.frame import DataFrame
import time
from Parser import data

class MockChebyshev:

    def __init__(self) -> None:
        pass

    def boyd(self, point_count_cheb, point_count_equi):

        x_cheb = np.array([-np.cos(np.pi * j / point_count_cheb) for j in range(point_count_cheb)])
        x_equi = np.array([(-1 + 2* k / point_count_equi) for k in range(point_count_equi)])
        x_mockcheb = np.array([])

        for xj in x_cheb:
            k = 1
            min = abs(xj - x_equi[0])
            value_to_add = x_equi[0]
            index = 0
            while k < len(x_equi):
                if abs(xj - x_equi[k]) < min:
                    min = abs(xj - x_equi[k])
                    value_to_add = x_equi[k]
                    index = k
                k += 1
            value_to_add = (1 + value_to_add) * point_count_equi / 2
            x_mockcheb = np.append(x_mockcheb, value_to_add)
            x_equi = np.delete(x_equi, index)

        return x_mockcheb

    def ibrahimoglu(self, n, start = 1, end = 85):

        x_cheb = np.array([0.5 *(start + end) + 0.5 * (start - end) * np.cos(np.pi * j / (n-1)) for j in range(n)])
        
        h = []
        for j in range(n - 1):
            h.append(x_cheb[j + 1] - x_cheb[j]) 
        
        hmin = min(h)
        S = [0]

        for j in range(n - 1):
            S.append(np.ceil(h[j] / hmin) + S[j])
        
        h_alpha = (end - start) / S[n-1]
        mockcheb_first = x_cheb[0]
        mockcheb_nodes = np.array([mockcheb_first], float)

        for j in range(n - 1):
            item_to_add = mockcheb_first + S[j + 1] * h_alpha
            mockcheb_nodes = np.append(mockcheb_nodes, item_to_add)
        
        return np.round(mockcheb_nodes)


mockcheb = MockChebyshev()