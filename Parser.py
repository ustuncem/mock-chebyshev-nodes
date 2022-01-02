import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

class Parser:
    """ Initializing and Cleaning Data
    """

    def __init__(self, filename: str) -> None:
        self.raw_data = pd.read_excel(filename)
        self.filename = filename
        self.clean_data = self.__parse(columns_to_drop=["Difference"])

    def debug(self) -> None:
        """Debugger 
        """
        print("Raw Data: \n", self.raw_data)
        print("Raw Data Info:\n")
        self.raw_data.info()
        print("Raw Data / Types: \n", self.raw_data.dtypes)

        print("Clean Data: \n", self.clean_data)
        print("Clean Data Info:\n")
        self.clean_data.info()
        print("Clean Data / Types: \n", self.clean_data.dtypes)

    def __parse(self, columns_to_drop = []) -> DataFrame:
        """Main method to parse incoming Excel.

        Args:
            columns_to_drop (list, optional): [Columns to drop]. Defaults to [].

        Returns:
            DataFrame: [Pandas DataFrame object]
        """


        if len(columns_to_drop) > 0:
            self.raw_data.drop(columns = columns_to_drop, inplace=True)

        self.raw_data = self.raw_data.dropna(axis="columns", how="all")
        self.raw_data = self.raw_data.fillna(0)

        #Sort Data (ASC)
        self.raw_data = self.raw_data.sort_values(by=["Day"], ascending=False)
        
        # Cleaned Data
        return self.raw_data


data = Parser("./assets/AVAX.xlsx")
