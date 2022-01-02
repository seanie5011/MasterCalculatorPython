import sympy as sym
import matplotlib
import matplotlib.pyplot as plt

x, y, z, t = sym.symbols('x y z t')

fInStr = input("Please input your scalar function as in standard format, f(x, y, z):\nf = ")
fInSym = sym.sympify(fInStr)
fInL = sym.latex(fInSym)

f = f"f = {fInL}"
gradf = r"\nabla f = \frac{\partial f}{\partial x}\hat{\imath} + \frac{\partial f}{\partial y}\hat{\jmath} + \frac{\partial f}{\partial z}\hat{k}"

diffxOut = sym.diff(fInSym, x, 1)
diffxL = sym.latex(diffxOut)
diffxS = sym.simplify(diffxOut)
diffxSL = sym.latex(diffxS)
diffyOut = sym.diff(fInSym, y, 1)
diffyL = sym.latex(diffyOut)
diffyS = sym.simplify(diffyOut)
diffySL = sym.latex(diffyS)
diffzOut = sym.diff(fInSym, z, 1)
diffzL = sym.latex(diffzOut)
diffzS = sym.simplify(diffzOut)
diffzSL = sym.latex(diffzS)

gradfsolved = "\\Rightarrow \\nabla f = \\left ( {0} \\right )\\hat{{\\imath}} + \\left ( {1} \\right )\\hat{{\\jmath}} + \\left ( {2} \\right )\\hat{{k}}".format(diffxL, diffyL, diffzL)
gradfsimp = "\\Rightarrow \\nabla f = \\left ( {0} \\right )\\hat{{\\imath}} + \\left ( {1} \\right )\\hat{{\\jmath}} + \\left ( {2} \\right )\\hat{{k}}".format(diffxSL, diffySL, diffzSL)

ax = plt.subplot(111)
ax.text(0.0, 1.0, r"$%s$" %(f), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 0.9, r"$%s$" %(gradf), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 0.8, r"$%s$" %(gradfsolved), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 0.7, r"$%s$" %(gradfsimp), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.axis('off')
plt.show()
