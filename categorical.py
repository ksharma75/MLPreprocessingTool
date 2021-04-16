import numpy as np
import pandas as pd

class EncodeCategorical:
    def __init__(self,dataframe):
        self.dataframe=dataframe

    def get_dataframe(self):
        return self.dataframe

    def set_dataframe(self,x):
        self.dataframe=x  

    def getOption(self):
        print('\nTasks(Encode Categorical)')
        print('1.Show Categorical Columns')
        print('2.Performing One Hot Encoding')
        print('3.Show dataset')
        option=int(input('What do you want to do?(Press -1 to exit):'))
        return option
    
    def showCategorical(self):
        print('The categorical columns are as follows:-')
        print(self.dataframe.select_dtypes(include='object').columns.tolist())

    def performOneHotEncodingUtil(self):
        while True:
            print('\nTasks(OneHotEncoding)\n')
            print('1.OneHotEncode the entire dataset')
            print('2.OneHotEncode specific columns')
            print('3.Show dataset')
            option=int(input('What do you want to do?(Press -1 to go back):'))
            if option==-1:
                return self.dataframe
            elif option==1:
                cat_cols=self.dataframe.select_dtypes(include='object').columns
                self.performOneHotEncoding(cat_cols)
                print('One Hot Encoding has been done on all columns.')
            elif option==2:
                cat_cols=self.dataframe.select_dtypes(include='object').columns
                print('The categorical columns are:-')
                print(cat_cols.tolist())
                ohe_cat_cols=input('Which columns do you to want to one hot encode?(Type space seperated values):').strip().split(' ')
                self.performOneHotEncoding(ohe_cat_cols)
                print('OneHotEncoding has been done on the chosen columns.')
            elif option==3:
                self.showDF()
            
            

    def performOneHotEncoding(self,cat_cols):
        #cat_cols=self.dataframe.select_dtypes(include='object').tolist()
        dict_cols=dict(zip(cat_cols,cat_cols))
        self.dataframe=pd.get_dummies(data=self.dataframe,prefix=dict_cols,prefix_sep='_',dummy_na=False,columns=cat_cols)
        

    def showDF(self):
        rows=int(input('Number of rows to show?:'))
        print(self.dataframe.head(rows))


        
