import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)
pd.set_option("display.expand_frame_repr", False)
pd.set_option('display.max_rows', 100)


def removeWhiteSpace(df, columnList):
    for i in columnList:
        if df[i].dtype == 'object':
            df[i] = df[i].str.strip().str.replace(' ', '')      
        else:
            pass

def numericDowncast(df):
    for i in df.columns:
        pd.to_numeric(df[i], errors='ignore', downcast='integer')

    
def renameColumns(df, prefix):
    columnMapping = {}
    for i in df.columns:
        columnMapping[i] = prefix + i
    df.rename(columns=columnMapping, inplace=True)
