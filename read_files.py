import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

class read:
    def __init__(self,path,delimiter):
        self.path = path
        self.delimiter = delimiter
    def read_file(self):
        if self.path.split(".")[-1] == 'csv':
            try:
                df = pd.read_csv(self.path,delimiter=self.delimiter)
            except:
                return "error in reading the file"
            
            print(df.head())
            st.header('Dataset Preview')
            st.write(df)

        return df
    

if __name__ == "__main__":
    pre = read(r'C:\Users\ramka\Downloads\linearregress\datafile.csv',';')
    df = pre.read_file()


    
