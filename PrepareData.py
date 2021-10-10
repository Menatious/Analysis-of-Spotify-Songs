import pandas as pd

def loaddata(filepath):    
    df = pd.read_csv(filepath)
    return df

