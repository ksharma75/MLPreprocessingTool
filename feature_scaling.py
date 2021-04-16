import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

class FeatureScaling:
    def __init__(self,dataframe):
        self.dataframe=dataframe

    def get_dataframe(self):
        return self.dataframe

    def set_dataframe(self,x):
        self.dataframe=x  
        
    def getOption(self):
        print('Tasks(Feature Scaling)\n')
        print('1.Perform Normalization(MinMax Scaler)')
        print('2.Perform Standardization(Standard Scaler)')
        print('3.Show dataset')
        option=int(input('What do you want to do?(Press -1 to go back):'))
        return option

    def normalizeUtil(self):
        while True:    
            print('\nTasks(Normalization)')
            print('1.Normalize the entire dataset')
            print('2.Normalize specific columns')
            print('3.Show dataset')
            option=int(input('What do you want to do?(Press -1 to go back):'))
            if option==-1:
                return self.dataframe
            elif option==1:
                num_cols=self.dataframe.select_dtypes(include=np.number).columns
                self.normalize(num_cols)
                print('Normalization has been done on all columns.')
            elif option==2:
                num_cols=self.dataframe.select_dtypes(include=np.number).columns
                print('The numerical columns are:-')
                print(num_cols.tolist())
                na_cols=input('Which columns do you to want to normalize?(Type space seperated values):').strip().split(' ')
                self.normalize(na_cols)
                print('Normalization has been done on the chosen columns.')
            elif option==3:
                self.showDF()
        return self.dataframe


    def standardizeUtil(self):
        while True:
            print('Tasks(Standardization)\n')
            print('1.Standardize the entire dataset')
            print('2.Standardize specific columns')
            print('3.Show dataset')
            option=int(input('What do you want to do?(Press -1 to go back):'))
            if option==-1:
                    return self.dataframe
            elif option==1:
                num_cols=self.dataframe.select_dtypes(include=np.number).columns
                self.standardize(num_cols)
                print('Standardization has been done on all columns.')
            elif option==2:
                num_cols=self.dataframe.select_dtypes(include=np.number).columns
                print('The numerical columns are:-')
                print(num_cols.tolist())
                na_cols=input('Which columns do you to want to standardize?(Type space seperated values):').strip().split(' ')
                self.standardize(na_cols)
                print('Standardization has been done on the chosen columns.')
            elif option==3:
                self.showDF()
            return self.dataframe


    def normalize(self,num_cols):
        scaler=MinMaxScaler()
        self.dataframe[num_cols]=scaler.fit_transform(self.dataframe[num_cols])
        

    def standardize(self,num_cols):
        scaler=StandardScaler()
        self.dataframe[num_cols]=scaler.fit_transform(self.dataframe[num_cols])
        

    def showDF(self):
        rows=int(input('Number of rows to show?:'))
        print(self.dataframe.head(rows))

        

    


    
