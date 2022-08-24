# MasterCalculator

## This project contains numerous functions primarily for usage in an Undergraduate Physics context

This project contains numerous functions that can solve complicated tasks / problems, focused on use in an Undergraduate Physics students work. These are showcased using a web-app created with [Streamlit](https://streamlit.io/).

The functionality supported (and planned to implement) are as follows:

1. [Interpolation](#interpolation)
2. [Curve Fitting](#curve-fitting)
3. [Differentiation / Integration](#differentiation--integration)
4. [Scientific Calculator](#scientific-calculator)
5. [Unit Converter](#unit-converter)
6. [Vector Operations](#vector-operations)
7. [Other](#other)

**[User Instructions](#user-instructions)**

### Interpolation

Interpolate between datapoints using algorithms like Cubic-Spline Interpolation.

### Curve Fitting

Using [SciPy](https://scipy.org/), fit various types of curve to data.

### Differentiation / Integration

Perform both analytical and numerical Differentiation and Integration using [SymPy](https://www.sympy.org/en/index.html) or SciPy.

### Scientific Calculator

Similar to the likes of the [Desmos Scientific Calculator](https://www.desmos.com/scientific) - the main addition being hyperbolic functions, and constants (using [NumPy](https://numpy.org/)).

### Unit Converter

Convert for example: *m* to *km*, or *ly* to *kpc* and so on. May use a library like [AstroPy](https://www.astropy.org/).

### Vector Operations

Various Vector Operations like: Grad, Div, Cirl, Laplacian, Cross Product, Dot Product, etc.

### Other

More features may include: Latex Code generator, Notes functionality, an app like [WebPlotDigitizer](https://automeris.io/WebPlotDigitizer/)

## User Instructions

1. Clone this project
3. Create a virtual enviroment to be used, ideally in the same folder as this project
2. Install the necessary libraries as detailed, using *pip*  
``pip install *library*``  
*Note: ensure protobuf is of version 3.20.x or lower; using ``pip install --upgrade protobuf==3.19.0``*
3. Open the terminal in the directory of the desired script (CTRL + L, type ``cmd``), or cd into it
4. Activate the Virtual Enviroment
``*venv*\Scripts\activate``
5. Run the script using Streamlit
``streamlit run Home.py``  
*Note: To close the app, CTRL + C on the terminal then close the browser*
