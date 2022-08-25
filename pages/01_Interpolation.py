import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from features.Interpolation import CubicSpline

# Helper functions
def convert_df_to_xy(df, xlabel='x', ylabel='y', dtype=np.float64):
    '''
    Usage:
        Converts 2 of a pandas DataFrame columns (labeled accordingly) to numpy arrays of dtype
    Inputs:
        df: a pandas DataFrame
        xlabel: a string of the column name to be taken as the x
        ylabel: a string of the column name to be taken as the y
        dtype: the numpy datatype for the array
    Outputs:
        x: the numpy array corresponding to the x-column
        y: the numpy array corresponding to the y-column
    '''

    x = df[xlabel].to_numpy(dtype=dtype)
    y = df[ylabel].to_numpy(dtype=dtype)

    return x, y

def convert_xy_to_df(x, y, xlabel='x', ylabel='y'):
    '''
    Usage:
        Converts 2 numpy arrays into a pandas DataFrame with labels specified
    Inputs:
        x: a numpy array
        y: a numpy array
        xlabel: a string of the column name to be taken as the x
        ylabel: a string of the column name to be taken as the y
    Outputs:
        df: a pandas DataFrame containing x and y
    '''

    x_df = pd.DataFrame(x, columns=[xlabel])
    y_df = pd.DataFrame(y, columns=[ylabel])

    df = pd.concat([x_df, y_df], axis=1)

    return df

def main():
    # --- Main
    st.markdown("# Interpolation :chart_with_upwards_trend:")

    df = pd.read_csv('test_data.csv')
    new_interpolation = CubicSpline()
    new_interpolation.set_data(*convert_df_to_xy(df))
    new_interpolation.get_factors()
    new_df = convert_xy_to_df(*new_interpolation.get_new_data())

    points = px.scatter(
        df,
        x='x',
        y='y',
        color_discrete_sequence=["#000000"]
    )

    line = px.line(
        new_df,
        x='x',
        y='y',
        color_discrete_sequence=["#FF0000"]
    )

    full_chart = go.Figure(
        data=line.data + points.data,
    ).update_layout(
        {
            'title': 'Title'
        }
    )
    st.plotly_chart(full_chart, use_container_width=True)

    # --- Sidebar
    st.sidebar.markdown("# Interpolation")

if __name__ == '__main__':
    st.set_page_config(
        page_title='Interpolation',
        page_icon=':chart_with_upwards_trend:',
        layout='centered',
        initial_sidebar_state='expanded'
    )
    main()
