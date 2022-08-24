# Dependancies
import numpy as np
import matplotlib.pyplot as plt

class Interpolate():
    def __init__(self):
        self.x = np.array([0])
        self.y = np.array([0])

    def set_data_frompath(self, path):
        data = np.loadtxt(path, delimiter = ',', unpack = True)
        self.x = data[0] # all first entries: x-values
        self.y = data[1] # all second entries: y-values

        return self.x, self.y

    def set_data(self, xdata, ydata):
        self.x = xdata
        self.y = ydata

        return self.x, self.y

    def cubic_spline(self):
        '''
        Usage:
            Takes a set of known datapoints and uses Cubic Spline Interpolation between them
        Inputs:
            X: array of known x-values
            Y: array of known y-values
        Outputs:
            a: array of coefficients
            b: array of coefficients
            c: array of coefficients
            d: array of coefficients
        '''
        # Copy Inputs for usage
        x = np.copy(self.x)
        y = np.copy(self.y)
        # Get size n
        n = len(x)
    
        # Helper h
        h = np.zeros([n])
        # Coefficients: a, b, c, d
        a = y
        b = np.zeros([n])
        c = np.zeros([n])
        d = np.zeros([n])
    
        # Matrix l
        l = np.zeros([n])
        # Matrix mu
        mu = np.zeros([n])
        # Helper z
        z = np.zeros([n])
        # b in Ax=b, now called alpha
        alpha = np.zeros([n])
    
        # Step 1
        for i in range(0, n - 1): # must be careful of the n - 1
            h[i] = x[i + 1] - x[i]
        
        # Step 2
        for i in range(1, n - 1):
            alpha[i] = 3 * (a[i + 1] - a[i]) / h[i] - 3 * (a[i] - a[i-1]) / h[i-1] #subbing in
        
        # Step 3
        l[0] = 1
        mu[0] = 0
        z[0] = 0
    
        # Step 4
        for i in range(1, n - 1):
            l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1] # remember we have said l is the diagonal in L
            mu[i] = h[i] / l[i] # remember we have said mu is the second diagonal in U
            z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]
        
        # Step 5
        l[n - 1] = 1
        z[n - 1] = 0
        c[n - 1] = 0
    
        # Step 6
        for j in range(n - 2, -1, -1): # from n - 2 to 0, check notation for n
            c[j] = z[j] - mu[j] * c[j + 1] # subbing in formulae
            b[j] = (a[j + 1] - a[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
            d[j] = (c[j + 1] - c[j]) / (3 * h[j])
        
        ## Extra - Print results
        #for i in range(n - 1):
        #    print("S" + str(i) + "(x) = " + str(a[i]) + " + " + \
        #          str(b[i]) + "(x-" + str(x[i]) + ") + " + \
        #          str(c[i]) + "(x-" + str(x[i]) + ")^2 + " + \
        #          str(d[i]) + "(x-" + str(x[i]) + ")^3")

        # Extra - set variables
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        # Step 7
        return (a, b, c, d)

    def get_yvalue(self, x_new):
        '''
        Usage:
            Takes the calculated formulae from the Cubic Spline Interpolation to find a y-value at a desired x-value
        Inputs:
            x_new: float of desired x-value
            x: array of known x-values
            a: array of coefficients
            b: array of coefficients
            c: array of coefficients
            d: array of coefficients
        Outputs:
            y_new: float of found y-value at xs
        '''
        i = -1 # start at -1 since we want counter to start at 0
        for value in self.x:
            if x_new > value: # if desired is greater than each known point, look in next range
                i += 1
            else:
                break

        y_new = self.a[i] + self.b[i] * (x_new - self.x[i]) + self.c[i] * (x_new - self.x[i])**2 + self.d[i] * (x_new - self.x[i])**3 # apply formula in correct S

        return y_new

    def get_data(self):
        x_list = []
        y_list = []

        for i in range(len(self.x) - 1):
            xs = np.linspace(self.x[i], self.x[i + 1], 50)
            ys = self.a[i] + self.b[i] * (xs - self.x[i]) + self.c[i] * (xs - self.x[i])**2 + self.d[i] * (xs - self.x[i])**3

            x_list.append(xs)
            y_list.append(ys)

        return x_list, y_list

    def plotting(self, xlabel = "x", ylabel = "y"):
        x_list, y_list = self.get_data()
        for index in range(len(x_list)):
            xs = x_list[index]
            ys = y_list[index]

            plt.plot(xs, ys, color = 'k')
            plt.plot(self.x, self.y, color = 'r', marker = '.', ls = 'None')

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
