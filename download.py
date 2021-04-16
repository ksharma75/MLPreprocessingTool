import os

class Download:
    def __init__(self,dataframe):
        self.dataframe=dataframe

    def downloadDataframe(self):
        fileName=input('Enter the filename you want?(Press -1 to go back):')
        if fileName!=-1:
            self.dataframe.to_csv(fileName)
            print(fileName+' created successfully!')
        