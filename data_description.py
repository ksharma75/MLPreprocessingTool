import numpy as np
import pandas as pd

class DataDescription:
    def __init__(self,dataframe):
        self.dataframe=dataframe

    def get_dataframe(self):
        return self.dataframe

    def set_dataframe(self,x):
        self.dataframe=x   

    def getOption(self):
        print('\nTasks(Data Description)\n')
        print('1.Describe a specific column')
        print('2.Show Properties of each column')
        print('3.Show dataset')
        option=int(input('What do you want to do?(Press -1 to go back):'))
        return option

    def showStats(self):
        desc = self.dataframe.describe(include=np.number)
        print('='*5+'Statistics of dataframe'+'='*5+'\n')
        print(desc)
        print('\n'+'='*10+'Summary of dataframe'+'='*10+'\n')
        self.dataframe.info()

    def showProperty(self):
        col=input('Property of which variable do you want to view?:')
        if col in self.dataframe.columns.values:
            desc=self.dataframe[col].describe()
            print(desc)
        
    def showDF(self):
        rows=int(input('Number of rows to show?:'))
        print(self.dataframe.head(rows))

