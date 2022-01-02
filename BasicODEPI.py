import sympy as sym
import matplotlib
import matplotlib.pyplot as plt

A, B, x = sym.symbols('A B x') #note y is not a symbol
y = sym.Function('y')(x) #y is now a function of x

while True:
    while True: #loop back if exception
        try: #checking they work
            Yddash = sym.sympify(input("Please input the coefficient in front of y'': "))
            Ydash = sym.sympify(input("Please input the coefficient in front of y': "))
            Y = sym.sympify(input("Please input the coefficient in front of y: "))
            rx = sym.sympify(input("Please input the r(x) in standard format: "))
        except:
            print("\nThe format inputted is not correct, please try again.\n")
            continue #next loop iteration
        else: #will run if no exception
            break #break out of loop

    eqIn = Yddash * sym.Derivative(y, x, 2) + Ydash * sym.Derivative(y, x, 1) + Y * y #makes the ODE by multiplying the coefficients
    eqOut = rx #just for readability
    eq = sym.Eq(eqIn, eqOut)
    sym.pprint(eq, use_unicode=False)

    print("\n\n")

    result = sym.dsolve(eq, ics = {y(0): 1, y.diff(x).subs(x, 0): 1}) #solves the ODE, returning the CF and PI solns together
    sym.pprint(result, use_unicode=False)

    if input("\nWould you like to run again? y/n: ") != "y": #can start over, if not "y", will just end program
        break