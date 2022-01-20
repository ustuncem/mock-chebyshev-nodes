import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import os

class Parser:
    """ Initializing and Cleaning Data
    """

    def __init__(self, filename: str) -> None:
        file_extension = os.path.splitext(filename)
        if file_extension[1] == ".xlsx":
            self.raw_data = pd.read_excel(filename)
            self.clean_data = self.__parse(columns_to_drop=["Difference"])
        else:
            self.raw_data = pd.read_csv(filename)
            self.clean_data = self.__parsecsv(columns_to_drop=["unix","open", "high", "low", "tradecount", "Volume USDT", "Volume BTC", "symbol"])

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
        self.raw_data = self.raw_data.sort_values(by=["Day"], ascending=True)
        
        # Cleaned Data
        return self.raw_data

    def __parsecsv(self, columns_to_drop = []) -> DataFrame:
        """Main method to parse incoming CSV.

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
        self.raw_data = self.raw_data.sort_values(by=["date"], ascending=True)
        self.raw_data.reset_index(drop=True, inplace=True)
        
        # Cleaned Data
        return self.raw_data.head(4099)


data = Parser("./assets/AVAX.xlsx")

csv_data = Parser("./assets/Binance_BTCUSDT_1h.csv")