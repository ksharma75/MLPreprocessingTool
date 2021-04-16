import numpy as np
import pandas as pd

class Imputation:
    def __init__(self,dataframe):
        self.dataframe=dataframe

    def get_dataframe(self):
        return self.dataframe

    def set_dataframe(self,x):
        self.dataframe=x  

    def getOption(self):
        print('\nTasks(Data Imputation)\n')
        print('1.Show number of NULL values')
        print('2.Remove Columns')
        print('3.Fill Null Values')
        print('4.Show Dataset')
        option=int(input('What do you want to do?(Press -1 to go back):'))
        return option
    
    def fillUtil(self):
        while True:
            print('\nHow to deal with numerical values?:')
            print('1.Fill Null values with mean')
            print('2.Fill Null values with median')
            print('3.Fill Null values with mode')
            num_opt=int(input('\nWhat do you want to do?(Press -1 to go back):'))
            if num_opt==-1:
                return self.dataframe
            elif num_opt==1:
                self.fillWithMean()
                break
            elif num_opt==2:
                self.fillWithMedian()
                break
            elif num_opt==3:
                self.fillWithMode()
                break
            else:
                print('Incorrect option!Try again.')

        while True:
            print('\nHow to deal with categorical values?:')
            print('1.Fill Null values with most frequent value')
            print('2.Fill Null values with Unknown')
            cat_opt=int(input('\nWhat do you want to do?(Press -1 to move back):'))
            if cat_opt==-1:
                return self.dataframe
            elif cat_opt==1:
                self.fillWithFreqVal()
                break
            elif cat_opt==2:
                self.fillWithUnknown()
                break
            else:
                print('Incorrect option!Try again.')
            
        return self.dataframe

    def countNULL(self):
        print('The count of NULL values are as follows:\n')
        print(self.dataframe.isnull().sum(axis=0))

    def dropColumn(self):
        while True:
            print('\n1.Delete all NULL columns')
            print('2.Delete some NULL columns')
            del_opt=int(input('What do you want to do?(Press -1 to go back:'))
            if del_opt==-1:
                break
            elif del_opt==1:
                self.dataframe=self.dataframe.dropna(axis=1)
                print('\nNULL columns dropped!')
                break
            elif del_opt==2:
                print('\n The NULL columns are:-')
                print(self.dataframe.columns[self.dataframe.isnull().any(axis=0)].tolist())
                na_cols=input('Which columns do you to want to drop?(Type space seperated values):').strip().split(' ')
                print(list(set(self.dataframe.columns.tolist())-set(na_cols)))
                self.dataframe=self.dataframe[list(set(self.dataframe.columns.tolist())-set(na_cols))]
                print('\n Chosen NULL columns deleted!')
                break
            else:
                print('Incorrect option!Try again.')    
        return self.dataframe

    def fillWithMean(self):
        for col in self.dataframe.columns.values:
            if self.dataframe[col].dtypes in ['int64','float64']:
                 #self.dataframe[col].replace(np.nan,self.dataframe[col].mean(),inplace=True) 
                 self.dataframe[col]=self.dataframe[col].fillna(self.dataframe[col].mean())
        print('NaN values have been replaced with Mean.')
        
    def fillWithMedian(self):
        for col in self.dataframe.columns.values:
            if self.dataframe[col].dtypes in ['int64','float64']:
                 #self.dataframe[col].replace(np.nan,self.dataframe[col].median(),inplace=True)
                 self.dataframe[col]=self.dataframe[col].fillna(self.dataframe[col].median()) 
        print('NaN values have been replaced with Median.')

    def fillWithMode(self):
        for col in self.dataframe.columns.values:
            if self.dataframe[col].dtypes in ['int64','float64']:
                 #self.dataframe[col].replace(np.nan,self.dataframe[col].mode(),inplace=True) 
                 self.dataframe[col]=self.dataframe[col].fillna(self.dataframe[col].mode())
        print('NaN values have been replaced with Mean.')

    def fillWithFreqVal(self):
        for col in self.dataframe.columns.values:
            if self.dataframe[col].dtypes=='object':
                self.dataframe[col]=self.dataframe[col].fillna(self.dataframe[col].value_counts().idxmax()[0])
        print('NaN values have been replaced with Most Frequent Value.')
        
    def fillWithUnknown(self):
        for col in self.dataframe.columns.values:
            if self.dataframe[col].dtypes=='object':
                self.dataframe[col]=self.dataframe[col].fillna('Unknown')
        print('NaN values have been replaced with Unknown.')
        
    def showDF(self):
        rows=int(input('Number of rows to show?:'))
        print(self.dataframe.head(rows))