import pandas as pd
import numpy as np

def convert_df_to_xy(df, dtype=np.float64):
    '''
    Usage:
        Converts 2 of a pandas DataFrame columns to numpy arrays of dtype
    Inputs:
        df: a pandas DataFrame
        dtype: the numpy datatype for the array
    Outputs:
        x: the numpy array corresponding to the x-column
        y: the numpy array corresponding to the y-column
    '''

    x = df['x'].to_numpy(dtype=dtype)
    y = df['y'].to_numpy(dtype=dtype)

    return x, y

def convert_xy_to_df(x, y, xlabel='x', ylabel='y'):
    '''
    Usage:
        Converts 2 numpy arrays into a pandas DataFrame
    Inputs:
        x: a numpy array
        y: a numpy array
    Outputs:
        df: a pandas DataFrame containing x and y
    '''

    x_df = pd.DataFrame(x, columns=['x'])
    y_df = pd.DataFrame(y, columns=['y'])

    df = pd.concat([x_df, y_df], axis=1)

    return df
