import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class preprocess:
    def __init__(self,path):
        self.path = path
    def read_file(self):
        if self.path.split(".")[-1] == 'csv':
            df = pd.read_csv(self.path)
            print(df.head())

        return df

    
