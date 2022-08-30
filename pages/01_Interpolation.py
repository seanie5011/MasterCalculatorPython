import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from io import StringIO

from features.Interpolation import Interpolate
from features.helpers import convert_df_to_xy, convert_xy_to_df

def main():
    # --- Main
    # explanation
    st.markdown('''
    # :page_with_curl: Interpolation

    In this App the user enters the $x$ and
    $y$ data they wish to use for the interpolation.

    ## :floppy_disk: Input Data

    You can select the `Browse files` button below to search for your Data File. It is **necessary** to only use numeric digits in this file,
    with no headers, just the raw-data. It is *recommended* that this file be in the `.csv` format, with no spaces between columns or data-points, 
    and with a comma `,` as the delimeter.

    *Types supported: `.csv`, `.txt`*
    ''')

    # - Initialise
    df = None
    kinds = {
            'Linear': 'linear',
            'Quadratic-Spline': 'quadratic',
            'Cubic-Spline': 'cubic'
    }  # dict used to decide which kind to use with radio

    # - Set Data
    # uploaded file
    @st.experimental_memo(max_entries=1)  # only 1 allowed file at a time
    def read_file(file):
        '''
        Usage:
            Reads the first 2 columns of an input file, labels them as 'x' and 'y', and sets type to float
            Extra functionality to reset interpolate button session state
        Inputs:
            file: a string path to the corresponding file
        Outputs:
            A pandas dataframe
        '''

        # if we upload new file (not same as one already in), we run this next block
        # we want to reset the interpolate button so as not to run it again
        if st.session_state.interpolate_button:
            del st.session_state.interpolate_button

        df = pd.read_csv(
            file, 
            sep=None, 
            names=['x', 'y'], 
            usecols=[0, 1], 
            dtype=np.float64
        )
        return df

    uploaded_file = st.file_uploader('Select your Data File here:', type=['csv', 'txt'])
    if uploaded_file is not None:
        try:
            df = read_file(uploaded_file)
        except ValueError:
            st.error('The Input Data must contain numbers only.')
        except:
            st.error('Unknown Error, please try again or report a bug.')
        else:
            with st.expander('See your Input Data:'):
                st.dataframe(df)

    # - Interpolate
    # Use session states to keep track of whether or not interpolate button was pressed
    if 'interpolate_button' not in st.session_state:  # for when app is reloaded
        st.session_state.interpolate_button = False

    def click_callback():  # keeps the interpolate button pressed in session state
        st.session_state.interpolate_button = True

    if df is not None:  # will only display if there is a file uploaded
        # explanation
        st.markdown('''
        ## :clipboard: Interpolation Settings

        Here you can select a couple settings for the computation. Firstly, you can select how many points to add *inbetween* your
        Input data-points - this is the resolution. Secondly, you can select the Interpolation Algorithm to use. Don't be afraid to play
        with the settings, and find what works!
        ''')

        # Interpolation Settings
        with st.form('Interpolation Settings'):
            number_points_between = st.slider(
                'Number of points to add in Interpolation:', 
                min_value=1, 
                max_value=100, 
                value=50, 
                step=1
            )
            interpolate_kind = st.radio('Interpolation Algorithm:', ('Linear', 'Quadratic-Spline', 'Cubic-Spline'))

            st.form_submit_button('Interpolate Data', on_click=click_callback)  # on click calls above function
        
        # Computation
        if st.session_state.interpolate_button:
            # get interpolated data
            new_interpolation = Interpolate(*convert_df_to_xy(df))
            new_df = convert_xy_to_df(
                *new_interpolation.get_new_data(
                    number_points_between=number_points_between, 
                    kind=kinds[interpolate_kind]
                )
            )
        
            # plotting
            # explanation
            st.markdown('''
            ## :chart_with_upwards_trend: Plotting the Interpolated Data

            This is a basic plot of the Input and Interpolated Data. This plot is interactive, make sure to check out the settings in the upper-right corner!  
            *Hint: You can even download this plot as a `.png` by using the Camera symbol!*
            ''')

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

            full_chart = go.Figure(data=line.data + points.data)
            full_chart.update_layout(title='Plot of Input and Interpolated Data')
            full_chart.update_xaxes(title_text="x-data")
            full_chart.update_yaxes(title_text="y-data")

            st.plotly_chart(full_chart, use_container_width=True)

            # get yvalue for given x
            # explanation
            st.markdown('''
            ## :pencil2: Solving for a Specific Input

            Using the Algorithm selected above, we can find the exact y-value that would correspond to any given x-value.
            However, this can only be done within the range of the Input Data. This is because the Algorithm can be 
            *wildly* inaccurate outside of the x-values we gave it.
            ''')

            desired_x = st.number_input(
                'Enter any x-value to get the corresponding y-value:', 
                min_value=df['x'].min(),  # cannot use values outside of given data
                max_value=df['x'].max(),
                format="%f"
            )
            new_y = new_interpolation.get_yvalue(float(desired_x))
            st.latex(f'''
             \\left( x, y \\right) = \\left( {float(desired_x)}, {new_y} \\right)
             ''')

            # new dataframe and download it
            # explanation
            st.markdown('''
            ## :open_file_folder: Raw Ouput Data
            ''')

            with st.expander('See your Output Data:'):
                st.dataframe(new_df)

            st.download_button(
                'Download Output Data as CSV',
                data=new_df.to_csv(index=False, header=False),
                file_name='interpolation.csv'
            )

    # --- Sidebar
    with st.sidebar:
        st.markdown('''
        # :chart_with_upwards_trend: Interpolation

        ## How it works:
        In this App we use *pandas* to take in user-data and manipulate
        it. Then, using *scipy*, we can Interpolate between the user-data
        and plot using *plotly*. Using the Interpolation Algorithm we can
        find a y-value for any given x-value in range. Finally, we can save
        the plotted data in a `.csv` file for the user to use elsewhere!

        ## Uses:
        Interpolation is used commonly in Undergraduate Physics or Mathematics,
        for example:  
        - Computing Integrals  
        - Differential Equations  
        - Experiment Prediction  
        - More...  

        ## Further Reading:
        - [Interpolation Wikipedia](https://en.wikipedia.org/wiki/Interpolation)  
        - [Scipy `.interpolate` Docs](https://docs.scipy.org/doc/scipy/reference/interpolate.html)  

        ## Packages Used:
        - [`streamlit`](https://docs.streamlit.io/)  
        - [`plotly`](https://plotly.com/python-api-reference/index.html)  
        - [`pandas`](https://pandas.pydata.org/docs/)  
        - [`numpy`](https://numpy.org/doc/)  
        - [`scipy`](https://docs.scipy.org/doc/scipy/)  
        ''')

if __name__ == '__main__':
    st.set_page_config(
        page_title='Interpolation',
        page_icon=':chart_with_upwards_trend:',
        layout='wide',
        initial_sidebar_state='expanded'
    )
    main()
