import sympy as sym
import matplotlib
import matplotlib.pyplot as plt

def SinglePendulum():
    # variables
    g, m, l, t = sym.symbols('g, m, l, t')

    #functions and free variables
    theta = sym.symbols(r'\theta', cls = sym.Function) # define these as functions

    theta = theta(t) # makes theta a function of time

    theta_d = sym.diff(theta, t, 1) # theta dot (first time derivative)
    theta_dd = sym.diff(theta, t, 2) # theta double dot (second time derivative)

    #positions as functions of the above
    x, y  = sym.symbols('x, y', cls = sym.Function) # define these as functions

    x = x(theta) # makes x a function of theta
    x = l * sym.sin(theta) #user input

    y = y(theta)
    y = -l * sym.cos(theta) #user input

    x_d = sym.diff(x, t) # x dot (first time derivative)
    x_dd = sym.diff(x, t, 2) # x double dot (second time derivative)
    y_d = sym.diff(y, t)
    y_dd = sym.diff(y, t, 2)

    #KE
    T = (1/2) * m * (x_d**2 + y_d**2)
    #PE
    U = m * g * y
    #Lagrangian
    L = T - U

    #Euler-Lagrange Equations for each
    EL_theta = sym.diff(sym.diff(L, theta_d), t) - sym.diff(L, theta)
    #simplify to get eoms
    EL_theta = EL_theta.simplify()

    EL_EOMs = [EL_theta]

    ax = plt.subplot(111)
    for i in range(len(EL_EOMs)):
        ax.text(0.0, 1.0 - i*0.1, r"$%s$" %(EL_EOMs[i]), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
    ax.axis('off')
    plt.show()

def SingleSpring():
    # variables
    g, m, l, k, l_ambda, t = sym.symbols(r'g, m, l, k, \lambda, t')

    #functions and free variables
    x  = sym.symbols('x', cls = sym.Function) # define these as functions

    x = x(t) # makes theta1 a function of time

    x_d = sym.diff(x, t, 1) # theta1 dot (first time derivative)
    x_dd = sym.diff(x, t, 2) # theta1 double dot (second time derivative)

    #KE
    T = (1/2) * m * x_d**2
    #PE
    U = (1/2) * k * x**2
    #External Damping
    W = -l_ambda * x_d * x
    #Lagrangian
    L = T - U

    #Euler-Lagrange Equations for each
    EL_x = sym.diff(sym.diff(L, x_d), t) - sym.diff(L, x) - sym.diff(W, x) # extra work from damping
    #simplify to get eoms
    EL_x = EL_x.simplify()

    EL_EOMs = [EL_x]

    ax = plt.subplot(111)
    for i in range(len(EL_EOMs)):
        ax.text(0.0, 1.0 - i*0.1, r"$%s$" %(EL_EOMs[i]), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
    ax.axis('off')
    plt.show()

def ElasticPendulum():
    # variables
    g, m, l, k, t = sym.symbols('g, m, l, k, t')

    #functions and free variables
    r, theta  = sym.symbols(r'r, \theta', cls = sym.Function) # define these as functions

    r = r(t)
    theta = theta(t) # makes theta a function of time

    r_d = sym.diff(r, t, 1)
    r_dd = sym.diff(r, t, 2)
    theta_d = sym.diff(theta, t, 1) # theta dot (first time derivative)
    theta_dd = sym.diff(theta, t, 2) # theta double dot (second time derivative)

    #positions as functions of the above
    x, y  = sym.symbols('x, y', cls = sym.Function) # define these as functions

    x = x(r, theta) # makes x a function of theta and r
    x = (l + r) * sym.sin(theta) #user input

    y = y(r, theta)
    y = -(l + r) * sym.cos(theta) #user input

    x_d = sym.diff(x, t) # x dot (first time derivative)
    x_dd = sym.diff(x, t, 2) # x double dot (second time derivative)
    y_d = sym.diff(y, t)
    y_dd = sym.diff(y, t, 2)

    #KE
    T = (1/2) * m * (x_d**2 + y_d**2)
    #PE
    U = m * g * y + (1/2) * k * (r)**2
    #Lagrangian
    L = T - U

    #Euler-Lagrange Equations for each
    EL_r = sym.diff(sym.diff(L, r_d), t) - sym.diff(L, r)
    EL_theta = sym.diff(sym.diff(L, theta_d), t) - sym.diff(L, theta)
    #simplify to get eoms
    EL_r = EL_r.simplify()
    EL_theta = EL_theta.simplify()

    EL_EOMs = [EL_r, EL_theta]

    ax = plt.subplot(111)
    for i in range(len(EL_EOMs)):
        ax.text(0.0, 1.0 - i*0.1, r"$%s$" %(EL_EOMs[i]), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
    ax.axis('off')
    plt.show()

def DoublePendulum():
    # variables
    g, m1, m2, l1, l2, t = sym.symbols('g, m_1, m_2, l_1, l_2, t')

    #functions and free variables
    theta1, theta2  = sym.symbols(r'\theta_1, \theta_2', cls = sym.Function) # define these as functions

    theta1 = theta1(t) # makes theta1 a function of time
    theta2 = theta2(t)

    theta1_d = sym.diff(theta1, t, 1) # theta1 dot (first time derivative)
    theta1_dd = sym.diff(theta1, t, 2) # theta1 double dot (second time derivative)
    theta2_d = sym.diff(theta2, t, 1)
    theta2_dd = sym.diff(theta2, t, 2)

    #positions as functions of the above
    x1, y1, x2, y2  = sym.symbols('x_1, y_1, x_2, y_2', cls = sym.Function) # define these as functions

    x1 = x1(theta1) # makes x1 a function of theta1
    x1 = l1 * sym.sin(theta1) #user input

    y1 = y1(theta1)
    y1 = -l1 * sym.cos(theta1) #user input

    x2 = x2(theta1, theta2)
    x2 = l1 * sym.sin(theta1) + l2 * sym.sin(theta2) #user input
    
    y2 = y2(theta1, theta2)
    y2 = -l1 * sym.cos(theta1) - l2 * sym.cos(theta2) #user input

    x1_d = sym.diff(x1, t) # x1 dot (first time derivative)
    x1_dd = sym.diff(x1, t, 2) # x1 double dot (second time derivative)
    y1_d = sym.diff(y1, t)
    y1_dd = sym.diff(y1, t, 2)
    x2_d = sym.diff(x2, t)
    x2_dd = sym.diff(x2, t, 2)
    y2_d = sym.diff(y2, t)
    y2_dd = sym.diff(y2, t, 2)

    #KE
    T = (1/2) * m1 * (x1_d**2 + y1_d**2) + (1/2) * m2 * (x2_d**2 + y2_d**2)
    #PE
    U = m1 * g * y1 + m2 * g * y2
    #Lagrangian
    L = T - U

    #Euler-Lagrange Equations for each
    EL_theta1 = sym.diff(sym.diff(L, theta1_d), t) - sym.diff(L, theta1)
    EL_theta2 = sym.diff(sym.diff(L, theta2_d), t) - sym.diff(L, theta2)
    #simplify to get eoms
    EL_theta1 = EL_theta1.simplify()
    EL_theta2 = EL_theta2.simplify()

    EL_EOMs = [EL_theta1, EL_theta2]

    ax = plt.subplot(111)
    for i in range(len(EL_EOMs)):
        ax.text(0.0, 1.0 - i*0.1, r"$%s$" %(EL_EOMs[i]), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
    ax.axis('off')
    plt.show()

def DoublePendulum1Spring():
    # variables
    g, m1, m2, l1, l2, k, t = sym.symbols('g, m_1, m_2, l_1, l_2, k, t')

    #functions and free variables
    theta1, r2, theta2  = sym.symbols(r'\theta_1, r_2, \theta_2', cls = sym.Function) # define these as functions

    theta1 = theta1(t) # makes theta1 a function of time
    r2 = r2(t)
    theta2 = theta2(t)

    theta1_d = sym.diff(theta1, t, 1) # theta1 dot (first time derivative)
    theta1_dd = sym.diff(theta1, t, 2) # theta1 double dot (second time derivative)
    r2_d = sym.diff(r2, t, 1)
    r2_dd = sym.diff(r2, t, 2)
    theta2_d = sym.diff(theta2, t, 1)
    theta2_dd = sym.diff(theta2, t, 2)

    #positions as functions of the above
    x1, y1, x2, y2  = sym.symbols('x_1, y_1, x_2, y_2', cls = sym.Function) # define these as functions

    x1 = x1(theta1) # makes x1 a function of theta1 and r1
    x1 = l1 * sym.sin(theta1) #user input

    y1 = y1(theta1)
    y1 = -l1 * sym.cos(theta1) #user input

    x2 = x2(theta1, r2, theta2)
    x2 = l1* sym.sin(theta1) + (l2 + r2) * sym.sin(theta2) #user input

    y2 = y2(theta1, r2, theta2)
    y2 = -l1 * sym.cos(theta1) - (l2 + r2) * sym.cos(theta2) #user input

    x1_d = sym.diff(x1, t) # x1 dot (first time derivative)
    x1_dd = sym.diff(x1, t, 2) # x1 double dot (second time derivative)
    y1_d = sym.diff(y1, t)
    y1_dd = sym.diff(y1, t, 2)
    x2_d = sym.diff(x2, t)
    x2_dd = sym.diff(x2, t, 2)
    y2_d = sym.diff(y2, t)
    y2_dd = sym.diff(y2, t, 2)

    #KE
    T = (1/2) * m1 * (x1_d**2 + y1_d**2) + (1/2) * m2 * (x2_d**2 + y2_d**2)
    #PE
    U = m1 * g * y1 + m2 * g * y2 + (1/2) * k * (r2)**2
    #Lagrangian
    L = T - U

    #Euler-Lagrange Equations for each
    EL_theta1 = sym.diff(sym.diff(L, theta1_d), t) - sym.diff(L, theta1)
    EL_r2 = sym.diff(sym.diff(L, r2_d), t) - sym.diff(L, r2)
    EL_theta2 = sym.diff(sym.diff(L, theta2_d), t) - sym.diff(L, theta2)
    #simplify to get eoms
    EL_theta1 = EL_theta1.simplify()
    EL_r2 = EL_r2.simplify()
    EL_theta2 = EL_theta2.simplify()

    EL_EOMs = [EL_theta1, EL_r2, EL_theta2]

    ax = plt.subplot(111)
    for i in range(len(EL_EOMs)):
        ax.text(0.0, 1.0 - i*0.1, r"$%s$" %(EL_EOMs[i]), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
    ax.axis('off')
    plt.show()

def DoublePendulum2Spring():
    # variables
    g, m1, m2, l1, l2, k1, k2, t = sym.symbols('g, m_1, m_2, l_1, l_2, k_1, k_2, t')

    #functions and free variables
    r1, theta1, r2, theta2  = sym.symbols(r'r_1, \theta_1, r_2, \theta_2', cls = sym.Function) # define these as functions

    r1 = r1(t)
    theta1 = theta1(t) # makes theta1 a function of time
    r2 = r2(t)
    theta2 = theta2(t)

    r1_d = sym.diff(r1, t, 1)
    r1_dd = sym.diff(r1, t, 2)
    theta1_d = sym.diff(theta1, t, 1) # theta1 dot (first time derivative)
    theta1_dd = sym.diff(theta1, t, 2) # theta1 double dot (second time derivative)
    r2_d = sym.diff(r2, t, 1)
    r2_dd = sym.diff(r2, t, 2)
    theta2_d = sym.diff(theta2, t, 1)
    theta2_dd = sym.diff(theta2, t, 2)

    #positions as functions of the above
    x1, y1, x2, y2  = sym.symbols('x_1, y_1, x_2, y_2', cls = sym.Function) # define these as functions

    x1 = x1(theta1, r1) # makes x1 a function of theta1 and r1
    x1 = (l1 + r1) * sym.sin(theta1) #user input

    y1 = y1(theta1, r1)
    y1 = -(l1 + r1) * sym.cos(theta1) #user input

    x2 = x2(theta1, r1, theta2, r2)
    x2 = (l1 + r1) * sym.sin(theta1) + (l2 + r2) * sym.sin(theta2) #user input

    y2 = y2(theta1, r1, theta2, r2)
    y2 = -(l1 + r1) * sym.cos(theta1) - (l2 + r2) * sym.cos(theta2) #user input

    x1_d = sym.diff(x1, t) # x1 dot (first time derivative)
    x1_dd = sym.diff(x1, t, 2) # x1 double dot (second time derivative)
    y1_d = sym.diff(y1, t)
    y1_dd = sym.diff(y1, t, 2)
    x2_d = sym.diff(x2, t)
    x2_dd = sym.diff(x2, t, 2)
    y2_d = sym.diff(y2, t)
    y2_dd = sym.diff(y2, t, 2)

    #KE
    T = (1/2) * m1 * (x1_d**2 + y1_d**2) + (1/2) * m2 * (x2_d**2 + y2_d**2)
    #PE
    U = m1 * g * y1 + m2 * g * y2 + (1/2) * k1 * (r1)**2 + (1/2) * k2 * (r2)**2
    #Lagrangian
    L = T - U

    #Euler-Lagrange Equations for each
    EL_r1 = sym.diff(sym.diff(L, r1_d), t) - sym.diff(L, r1)
    EL_theta1 = sym.diff(sym.diff(L, theta1_d), t) - sym.diff(L, theta1)
    EL_r2 = sym.diff(sym.diff(L, r2_d), t) - sym.diff(L, r2)
    EL_theta2 = sym.diff(sym.diff(L, theta2_d), t) - sym.diff(L, theta2)
    #simplify to get eoms
    EL_r1 = EL_r1.simplify()
    EL_theta1 = EL_theta1.simplify()
    EL_r2 = EL_r2.simplify()
    EL_theta2 = EL_theta2.simplify()

    EL_EOMs = [EL_r1, EL_theta1, EL_r2, EL_theta2]

    ax = plt.subplot(111)
    for i in range(len(EL_EOMs)):
        ax.text(0.0, 1.0 - i*0.1, r"$%s$" %(EL_EOMs[i]), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
    ax.axis('off')
    plt.show()

#SinglePendulum()
#SingleSpring()
#ElasticPendulum()
#DoublePendulum()
#DoublePendulum1Spring()
DoublePendulum2Spring()