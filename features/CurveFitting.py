# Installing Dependancies
from matplotlib import pyplot as plt
import numpy as np
import scipy as sp
from scipy.optimize import minimize

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

    def plotting(self, xstart, xend, xsteps = 100, xlabel = "x", ylabel = "y"):
        solved_pars = self.nelder_mead() # plotting using Nelder-Mead
        xs = np.linspace(xstart, xend, xsteps)
        ys = self.func(xs, *solved_pars)

        plt.plot(xs, ys, color = 'k')
        plt.plot(self.x, self.y, color = 'r', marker = '.', ls = 'None')

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
