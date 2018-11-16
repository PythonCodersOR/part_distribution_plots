# do one things and do it well
# This is a wrapper function for the pandas function 'ExcelFile'
# and reads and excel file after checking to see if the file exsits

import os, pandas as pd

def readXL(str_file):
    if os.path.isfile(str_file) == False:
        raise ValueError('Cannot find file ' + str_file)
    elif os.path.isfile(str_file) == True:
        df = pd.ExcelFile(str_file)
    return df
       

# try it out
str_path = 'C:\\Users\\kbranna\\Source\\Repos\\part_distribution_plots'
str_file_XL = 'ParticleDistributions_EC.xlsx'
str_file = os.path.join(str_path, str_file_XL)

df = readXL(str_file)