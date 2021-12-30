import pandas as pd

class Parser:
    """[summary]
    """

    def __init__(self):
        pass

    def parse(self):
        raw_data = pd.read_excel("./assets/AVAX.xlsx")
        print(raw_data)
        


x = Parser()
x.parse()
