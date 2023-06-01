import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class preprocess:
    def __init__(self,path):
        self.path = path
    def read_file(self):
        if self.path.split(".")[-1] == 'csv':
            df = pd.read_csv(self.path,delimiter=';')
            print(df.head())

        return df
    

if __name__ == "__main__":
    pre = preprocess('C:\Users\ramka\Downloads\linearregress\datafile.csv')
    df = pre.read_file()


    
