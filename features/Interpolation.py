import numpy as np
from scipy.interpolate import interp1d

class Interpolate():
    def __init__(self, xdata, ydata):
        self.x = xdata
        self.y = ydata

    def set_data(self, xdata, ydata):
        '''
        Usage:
            Takes a numpy array containing type np.float64 and assigns to the class variables
        Inputs:
            xdata: array of known x-values
            ydata: array of known y-values
        Outputs:
            x: array of known x-values
            y: array of known y-values
        '''

        self.x = xdata
        self.y = ydata

        return self.x, self.y

    def get_new_data(self, number_points_between=50, kind='cubic'):
        '''
        Usage:
            Uses the specified kind of interpolation to get the new datapoints between
        Inputs:
            number_points_between: integer of how many points to calculate between original
            kind: string of which kind of interpolation to use
        Outputs:
            new_x: array of found x-values
            interpolated_data(new_x): array of found y-values
        '''

        self.interpolated_function = interp1d(self.x, self.y, kind=kind)  # creates function from scipy

        new_x = np.linspace(self.x[0], self.x[-1], num=number_points_between * len(self.x))
        interpolated_data = self.interpolated_function(new_x)

        return new_x, interpolated_data

    def get_yvalue(self, x):
        '''
        Usage:
            Uses the specified kind of interpolation to get the y-value at the input x-value
        Inputs:
            x: float of the desired x-value to input
        Outputs:
            float of the corresponding y-value
        '''

        try:
            return float(self.interpolated_function(x))
        except ValueError:  # if enters a number out of range
            return 0.0
