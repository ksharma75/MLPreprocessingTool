import numpy as np
import pandas as pd
import regex as re
import shutil
import sys
from os import path
from data_description import DataDescription
from imputation import Imputation
from categorical import EncodeCategorical
from feature_scaling import FeatureScaling
from download import Download

#Exception Class
class IncorrectFileFormatError(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)

class ExitError(Exception):
    def __init__(self,message="Exiting......"):
        self.message=message
        super().__init__(self.message)

def readCSV(file_path):
    data=pd.read_csv(file_path)
    data.columns=data.columns.str.lower()
    columns=data.columns
    print('The columns of input dataset are as follows:-\n')
    print(columns.values)
    target_var=input('\nWhich is the target variable?(Press -1 to exit):')
    if target_var=='-1':
        raise ExitError
    elif target_var not in columns.values:
        raise Exception
    return dropColumn(data,target_var)
    
        
def dropColumn(data,target_var):
    dependent_df=data[target_var]
    independent_df=data.drop([target_var],axis=1)
    return independent_df

#if __name__=="__main__":


def main():
    print('-'*10+'Welcome to ML Preprocessor CLI'+'-'*10+'\n\n')
    try:
        file_path=sys.argv[1]
        if file_path.endswith('.csv')==False:
            raise IncorrectFileFormatError("file is not in CSV format")

        revised_df=readCSV(file_path)
        print('\nScreenshot of independent dataframe:\n')
        print(revised_df.head())
        print('\n'+'-'*30+'\n')
        while True:
            print('\nTasks(Preprocessing)')
            print('1.Data Description')
            print('2.Handling NULL values')
            print('3.Encoding Categorical Data')
            print('4.Feature Scaling of the Dataset')
            print('5.Download the modified Dataset\n')
            option=int(input('What do you want to do?(Press -1 to exit):'))
            if option==-1:
                raise ExitError
            elif option==1:
                data_desc=DataDescription(revised_df)
                while True:
                    option=data_desc.getOption()
                    if option==-1:
                        break
                    elif option==1:
                        data_desc.showProperty()
                    elif option==2:
                        data_desc.showStats()
                    elif option==3:
                        data_desc.showDF()
                    else:
                        print('Incorrect option!Try again.')
                
            elif option==2:
                impute=Imputation(revised_df)
                while True:
                    option=impute.getOption()
                    if option==-1:
                        break
                    elif option==1:
                        impute.countNULL()
                    elif option==2:
                        revised_df=impute.dropColumn()
                    elif option==3:
                        revised_df=impute.fillUtil()
                    elif option==4:
                        impute.showDF()
                    else:
                        print('Incorrect option!Try again.')
            elif option==3:
                encode=EncodeCategorical(revised_df)
                while True:
                    option=encode.getOption()
                    if option==-1:
                        break
                    elif option==1:
                        encode.showCategorical()
                    elif option==2:
                        revised_df=encode.performOneHotEncodingUtil()
                    elif option==3:
                        encode.showDF()
                    else:
                        print('Incorrect option!Try again.')
            elif option==4:
                while True:
                    scale=FeatureScaling(revised_df)
                    option=scale.getOption()
                    if option==-1:
                        break
                    elif option==1:
                        scale.normalizeUtil()
                    elif option==2:
                        scale.standardizeUtil()
                    elif option==3:
                        scale.showDF()
                    else:
                        print('Incorrect option!Try again.')
            elif option==5:
                download=Download(revised_df)
                download.downloadDataframe()
            else:
                print('Incorrect option!Try again.')
    except IndexError as e:
        print('File path missing.',e)
    except IncorrectFileFormatError as e:
        print('Incorrect file format.',e)
    except FileNotFoundError as e:
        print('File Not Found!',e)
    except ExitError as e:
        print(e)
    except Exception as e:
        print('Incorrect option chosen.',e)       
        

main()   