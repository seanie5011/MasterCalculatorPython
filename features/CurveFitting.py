import numpy as np
from scipy.optimize import curve_fit

from scipy.optimize import minimize

class CurveFit():
    def __init__(self, xdata, ydata):
        self.x = xdata
        self.y = ydata

        # set the functions
        self.functions = {
            'Linear': lambda x, a, b: a * x + b,
            'Quadratic': lambda x, a, b, c: a * x**2 + b * x + c,
            'Cubic': lambda x, a, b, c, d: a * x**3 + b * x**2 + c * x + d,
        }

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

    def set_function(self, function, p0):
        '''
        Usage:
            Sets the function to be used for fitting, and fits the parameters
        Inputs:
            function: string of the function to use to be passed into self.functions
            p0: initial guess of the parameters to be fitted
        Outputs:
            popt: 
            pcov: 
        '''

        self.func = self.functions[function]
        self.popt, self.pcov = curve_fit(self.func, self.x, self.y, p0=p0)

        return self.popt, self.pcov

    def get_new_data(self, number_points_between=50):
        '''
        Usage:
            Uses the specified function fitted to get the new datapoints between
        Inputs:
            number_points_between: integer of how many points to calculate between original
        Outputs:
            new_x: array of found x-values
            new_y: array of found y-values
        '''

        new_x = np.linspace(self.x[0], self.x[-1], num=number_points_between * len(self.x))
        new_y = self.func(new_x, *self.popt)

        return new_x, new_y

    def get_yvalue(self, x):
        '''
        Usage:
            Uses the specified function fitted to get the y-value at the input x-value
        Inputs:
            x: float of the desired x-value to input
        Outputs:
            float of the corresponding y-value
        '''

        try:
            return float(self.func(x, *self.popt))
        except ValueError:  # if value error, just return 0
            return 0.0


class Fit():
    def __init__(self):
        self.x = np.array([0])
        self.y = np.array([0])

    def set_all(self, xdata, ydata, func, pars):
        self.x = xdata
        self.y = ydata
        self.func = func
        self.pars = pars

        return self.x, self.y, self.func, self.pars

    def set_data_frompath(self, path):
        data = np.loadtxt(path, delimiter = ',', unpack = True)
        self.x = data[0] # all first entries: x-values
        self.y = data[1] # all second entries: y-values

        return self.x, self.y

    def set_data(self, xdata, ydata):
        self.x = xdata
        self.y = ydata

        return self.x, self.y

    def set_function(self, func):
        self.func = func

        return self.func

    def set_pars(self, pars):
        self.pars = pars

        return self.pars

    def driver_func(self, pars): # function used to find difference between experiment and calculated
        ys = self.func(self.x, *pars) # unpack pars
        error = np.sum((ys - self.y)**2)  #error is sum of squares

        return error

    def nelder_mead(self):
        res = minimize(self.driver_func, self.pars, method = 'Nelder-Mead', options = {'maxiter': 30, 'maxfev': 30, "xatol": 0.1, "fatol": 0.1}) # perform Nelder-Mead fit using the driver func
        solved_pars = res.x # x attribute are the new pars

        return solved_pars
