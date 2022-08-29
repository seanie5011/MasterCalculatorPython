import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from features.Interpolation import Interpolate

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
    st.markdown('''
    # :chart_with_upwards_trend: Interpolation

    In this App the user enters the $x$ and
    $y$ data they wish to use for the interpolation.

    ## Input Data:
    *Types supported: `.csv`, `.txt`*
    ''')

    # - Initialise
    df = None

    # - Set Data
    # uploaded file
    uploaded_file = st.file_uploader('', type=['csv', 'txt'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

    # - Interpolate
    interpolate_button = st.button('Interpolate Data')
    if interpolate_button and df is not None:
        # get new data
        new_interpolation = Interpolate(*convert_df_to_xy(df))
        new_df = convert_xy_to_df(*new_interpolation.get_new_data())
        
        # plotting
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

        # new dataframe and download
        st.dataframe(new_df)
        st.download_button(
            'Download as CSV',
            data=new_df.to_csv(index=False),
            file_name='interpolation.csv'
        )

    # --- Sidebar
    with st.sidebar:
        st.markdown('''
        # :chart_with_upwards_trend: Interpolation

        ## How it works:
        There are many algorithms used which can be selected, such as:
        - Linear  
        - Cubic-Spline  

        ## Uses:
        Interpolation is used commonly in the following:  
        - Computing Integrals  
        - Differential Equations  
        - More...  

        ## Further Reading:
        - [Interpolation Wikipedia](https://en.wikipedia.org/wiki/Interpolation)  
        - [Scipy `.interpolate` Docs](https://docs.scipy.org/doc/scipy/reference/interpolate.html)  
        ''')

if __name__ == '__main__':
    st.set_page_config(
        page_title='Interpolation',
        page_icon=':chart_with_upwards_trend:',
        layout='centered',
        initial_sidebar_state='expanded'
    )
    main()
