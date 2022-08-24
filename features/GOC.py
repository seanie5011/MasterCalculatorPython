import sympy as sym
import matplotlib
import matplotlib.pyplot as plt

x, y, z, t, u, v, w = sym.symbols('x y z t u v w')

# - Defining Coords - #
CoordSym = []
CoordL = []

#Inputs
yn = input("Do you wish to take an input? y/n: ") #type in new coords or use the ones set here
if yn == "y":
    while True: #loop back if exception
        xInStr = input("Please input your transformations (x, y, z) --> (u, v, w):\nx = ")
        yInStr = input("y = ")
        zInStr = input("z = ")
        try: #checking they work
            xInSym = sym.sympify(xInStr) #not efficient but sure whatevs
            yInSym = sym.sympify(yInStr)
            zInSym = sym.sympify(zInStr)
        except:
            print("\nThe format inputted is not correct, please try again.\n")
            continue #next loop iteration
        else: #will run if no exception
            break #break out of loop
else: #preset ones
    xInStr = "u*sin(v)*cos(w)"
    yInStr = "u*sin(v)*sin(w)"
    zInStr = "u*cos(v)"

xInSym = sym.sympify(xInStr) #doing again so both conditions have it
CoordSym.append(xInSym)
xInL = sym.latex(xInSym)
CoordL.append(xInL) #append sympy expressions to sympy list, latex expressions to latex list

yInSym = sym.sympify(yInStr)
CoordSym.append(yInSym)
yInL = sym.latex(yInSym)
CoordL.append(yInL)

zInSym = sym.sympify(zInStr)
CoordSym.append(zInSym)
zInL = sym.latex(zInSym)
CoordL.append(zInL)

xL = f"x = {xInL}" #to be displayed
yL = f"y = {yInL}"
zL = f"z = {zInL}"

# - Derivatives - #
diffIn = [[] for i in range(3)] #same as [[], [], []]
diffOut = [[] for i in range(3)]
diffEqL = [[] for i in range(3)]
xyz = [x, y, z]
uvw = [u, v, w]

for index, expr in enumerate(CoordSym):
    for val in uvw:#gets all x derivatives (x with u, x with v, x with w), then all y and then all z
        In = sym.Derivative(xyz[index], val, 1)
        diffIn[index].append(In)
        Out = sym.diff(expr, val, 1)
        diffOut[index].append(Out)
        Eq = sym.Eq(In, Out) #creates sympy expression of In = Out
        diffEqL[index].append(sym.latex(Eq)) #diffEqL[0][0] = dx/du, diffEqL[0][1] = dx/dv, diffEqL[1][1] = dy/dv

# - Metric and Scale Factors- #
g = [[0, 0, 0] for i in range(3)]
h = []

for j in range(len(uvw)):
    for k in range(len(uvw)): #iterates over j and k to change position in matrix
        for i in range(len(xyz)): #iterates over i to add 
            g[j][k] += diffOut[i][j] * diffOut[i][k] #note: not TeX of expression, is the actual expression
            g[j][k] = sym.simplify(g[j][k])
        if j == k:
            h.append(sym.simplify(sym.sqrt(g[j][k]))) #scale factors, note square root does not always work

gL = [sym.latex(a) for a in g] #turns the lists into latex, not individual elements
hL = sym.latex(h) #list into latex

# - Arc and Volume Element - #
#Arc
dsi = []
dsiL = []

for i in range(len(uvw)):
    dsi.append(g[i][i]) #equals to the scale factors squared
    dsiL.append(sym.latex(dsi[i]))

#Volume
jacobi = sym.Matrix([diffOut[0], diffOut[1], diffOut[2]])
dV = sym.simplify(jacobi.det()) #determinent of the jacobi
dVL = sym.latex(dV)

# - Grad - #
gradi = []
gradiL = []

gradisimp = []
gradisimpL = []

for index, sfactor in enumerate(h):
    gradi.append(1/sfactor) #1/scale factor for each i
    gradiL.append(sym.latex(gradi[index]))

    gradisimp.append(sym.simplify(gradi[index])) #simplify this
    gradisimpL.append(sym.latex(gradisimp[index]))
#have regular and simplified exression
gradf = r"\nabla f = \left ( %s \right ) \frac{\partial f}{\partial u}\bar{e}_u + \left ( %s \right ) \frac{\partial f}{\partial v}\bar{e}_v + \left ( %s \right ) \frac{\partial f}{\partial w}\bar{e}_w" %(gradiL[0], gradiL[1], gradiL[2])
gradfsimp = r"\Rightarrow \nabla f = \left ( %s \right ) \frac{\partial f}{\partial u}\bar{e}_u + \left ( %s \right ) \frac{\partial f}{\partial v}\bar{e}_v + \left ( %s \right ) \frac{\partial f}{\partial w}\bar{e}_w" %(gradisimpL[0], gradisimpL[1], gradisimpL[2])

# - Divergence - #
sf123mult = h[0] * h[1] * h[2] #h1*h2*h3
sf23mult = h[1] * h[2] #h2*h3
sf13mult = h[0] * h[2]
sf12mult = h[0] * h[1]

sf123multL = sym.latex(sf123mult)
sf23multL = sym.latex(sf23mult)
sf13multL = sym.latex(sf13mult)
sf12multL = sym.latex(sf12mult)

sf123multsimpL = sym.latex(sym.simplify(sf123mult)) #simplified h1*h2*h3
sf123multrecipL = sym.latex(sym.simplify(1/sf123mult)) #reciprocal of simplified
sf23multsimpL = sym.latex(sym.simplify(sf23mult))
sf13multsimpL = sym.latex(sym.simplify(sf13mult))
sf12multsimpL = sym.latex(sym.simplify(sf12mult))

divF = r"\nabla \cdot \bar{F} = \left ( \frac{1}{%s} \right ) \left [ \frac{\partial \left ( %s F_u \right )}{\partial u} + \frac{\partial \left ( %s F_v \right )}{\partial v} + \frac{\partial \left ( %s F_w \right )}{\partial w} \right ]" %(sf123multL, sf23multL, sf13multL, sf12multL)
divFsimp = r"\Rightarrow \nabla \cdot \bar{F} = \left ( %s \right ) \left [ \frac{\partial \left ( %s F_u \right )}{\partial u} + \frac{\partial \left ( %s F_v \right )}{\partial v} + \frac{\partial \left ( %s F_w \right )}{\partial w} \right ]" %(sf123multrecipL, sf23multsimpL, sf13multsimpL, sf12multsimpL)

# - Curl - #
sf1L = sym.latex(h[0]) #turn the individual scale factors into latex form
sf2L = sym.latex(h[1])
sf3L = sym.latex(h[2])

sf23multrecipL = sym.latex(sym.simplify(1/sf23mult)) #simplfiy the reciprocals of the multiples
sf13multrecipL = sym.latex(sym.simplify(1/sf13mult))
sf12multrecipL = sym.latex(sym.simplify(1/sf12mult))

curlF = r"\nabla \times \bar{F} = \left ( \frac{1}{%s} \right ) \left [ \frac{\partial \left ( %s F_w \right )}{\partial v} - \frac{\partial \left ( %s F_v \right )}{\partial w}\right ]\bar{e}_u + \left ( \frac{1}{%s} \right ) \left [ \frac{\partial \left ( %s F_u \right )}{\partial w} - \frac{\partial \left ( %s F_w \right )}{\partial u} \right ]\bar{e}_v + \left ( \frac{1}{%s} \right ) \left [ \frac{\partial \left ( %s F_v \right )}{\partial u} - \frac{\partial \left ( %s F_u \right )}{\partial v} \right ]\bar{e}_w" %(sf23multsimpL, sf3L, sf2L, sf13multsimpL, sf1L, sf3L, sf12multsimpL, sf2L, sf1L)
curlFsimp = r"\Rightarrow \nabla \times \bar{F} = \left ( %s \right ) \left [ \frac{\partial \left ( %s F_w \right )}{\partial v} - \frac{\partial \left ( %s F_v \right )}{\partial w}\right ]\bar{e}_u + \left ( %s \right ) \left [ \frac{\partial \left ( %s F_u \right )}{\partial w} - \frac{\partial \left ( %s F_w \right )}{\partial u} \right ]\bar{e}_v + \left ( %s \right ) \left [ \frac{\partial \left ( %s F_v \right )}{\partial u} - \frac{\partial \left ( %s F_u \right )}{\partial v} \right ]\bar{e}_w" %(sf23multrecipL, sf3L, sf2L, sf13multrecipL, sf1L, sf3L, sf12multrecipL, sf2L, sf1L)

# - Laplacian - #
sf23o1mult = sf23mult / h[0] #h2*h3/h1
sf13o2mult = sf13mult / h[1] #h1*h3/h2
sf12o3mult = sf12mult / h[2]

sf23o1multL = sym.latex(sf23o1mult)
sf13o2multL = sym.latex(sf13o2mult)
sf12o3multL = sym.latex(sf12o3mult)

sf23o1multsimpL = sym.latex(sym.simplify(sf23o1mult)) #latex of simplified
sf13o2multsimpL = sym.latex(sym.simplify(sf13o2mult))
sf12o3multsimpL = sym.latex(sym.simplify(sf12o3mult))

lapf = r"\nabla^{2} f = \left ( \frac{1}{%s} \right ) \left [ \frac{\partial }{\partial u}\left ( %s \frac{\partial f}{\partial u} \right ) + \frac{\partial }{\partial v}\left ( %s \frac{\partial f}{\partial v} \right ) +\frac{\partial }{\partial w}\left ( %s \frac{\partial f}{\partial w} \right ) \right ]" %(sf123multL, sf23o1multL, sf13o2multL, sf12o3multL)
lapfsimp = r"\Rightarrow \nabla^{2} f = \left ( %s \right ) \left [ \frac{\partial }{\partial u}\left ( %s \frac{\partial f}{\partial u} \right ) + \frac{\partial }{\partial v}\left ( %s \frac{\partial f}{\partial v} \right ) +\frac{\partial }{\partial w}\left ( %s \frac{\partial f}{\partial w} \right ) \right ]" %(sf123multrecipL, sf23o1multsimpL, sf13o2multsimpL, sf12o3multsimpL)

# - Plotting - #
ax = plt.subplot(111)
ax.text(0.0, 1.0, r"$\left ( x, y, z \right ) \rightarrow \left ( u, v, w \right )$", horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")

#Coords
for val0 in range(len(CoordL)):
    ax.text(0.0, 1.0 - 0.1*(val0 + 1), r"$%s = %s$" %(xyz[val0], CoordL[val0]), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black") #the +1 and beyond for other expressions is just to create extra space

#Derivatives
for val1 in range(len(diffEqL)):
    for val2 in range(len(diffEqL[0])): #double loop to print all elements of 2D array
        ax.text(0.0, 1.0 - 0.1*(val0 + val1*len(diffEqL) + val2 + 2), r"$%s$" %(diffEqL[val1][val2]), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black") #the %s just subs into the string in order given

#Metric and Scale Factors
for val3 in range(len(gL)):
    if val3 == int((len(gL) - 1)/2):
        ax.text(0.0, 1.0 - 0.1*(val0 + val1*len(diffEqL) + val2 + val3 + 3), r"$g_{jk} = %s$" %(gL[val3]), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
    else:
        ax.text(0.0, 1.0 - 0.1*(val0 + val1*len(diffEqL) + val2 + val3 + 3), r"        $%s$" %(gL[val3]), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 1.0 - 0.1*(val0 + val1*len(diffEqL) + val2 + val3 + 4), r"$h_i = %s$" %(hL), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")

#Arc and Volume element
ax.text(0.0, 1.0 - 0.1*(val0 + val1*len(diffEqL) + val2 + val3 + 5), r"$ds^{2} = (%s)du^{2} + (%s)dv^{2} + (%s)dw^{2}$" %(dsiL[0], dsiL[1], dsiL[2]), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 1.0 - 0.1*(val0 + val1*len(diffEqL) + val2 + val3 + 6), r"$dV = (%s)dudvdw$" %(dVL), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")

#Grad
ax.text(0.0, 1.0 - 0.1*(val0 + val1*len(diffEqL) + val2 + val3 + 7.5), r"$%s$" %(gradf), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 1.0 - 0.1*(val0 + val1*len(diffEqL) + val2 + val3 + 8.5), r"$%s$" %(gradfsimp), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")

#Divergence
ax.text(0.0, 1.0 - 0.1*(val0 + val1*len(diffEqL) + val2 + val3 + 10), r"$%s$" %(divF), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 1.0 - 0.1*(val0 + val1*len(diffEqL) + val2 + val3 + 11.5), r"$%s$" %(divFsimp), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")

#Curl
ax.text(0.0, 1.0 - 0.1*(val0 + val1*len(diffEqL) + val2 + val3 + 13), r"$%s$" %(curlF), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black") #need more space
ax.text(0.0, 1.0 - 0.1*(val0 + val1*len(diffEqL) + val2 + val3 + 14.5), r"$%s$" %(curlFsimp), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")

#Laplacian
ax.text(0.0, 1.0 - 0.1*(val0 + val1*len(diffEqL) + val2 + val3 + 16), r"$%s$" %(lapf), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 1.0 - 0.1*(val0 + val1*len(diffEqL) + val2 + val3 + 17.5), r"$%s$" %(lapfsimp), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")

ax.axis('off') #removes all axes and ticks
plt.show() #finally show! use the button in bottom left corner to navigate