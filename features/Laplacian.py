import sympy as sym
import matplotlib
import matplotlib.pyplot as plt

x, y, z, t = sym.symbols('x y z t')

fInStr = input("Please input your scalar function as in standard format, f(x, y, z):\nf = ")
fInSym = sym.sympify(fInStr)
fInL = sym.latex(fInSym)

f = f"f = {fInL}"
lapf = r"\nabla^{2} f = \nabla \cdot \nabla f = \Delta f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}"

diffx2Out = sym.diff(fInSym, x, 2)
diffx2L = sym.latex(diffx2Out)
diffx2S = sym.simplify(diffx2Out)
diffx2SL = sym.latex(diffx2S)
diffy2Out = sym.diff(fInSym, y, 2)
diffy2L = sym.latex(diffy2Out)
diffy2S = sym.simplify(diffy2Out)
diffy2SL = sym.latex(diffy2S)
diffz2Out = sym.diff(fInSym, z, 2)
diffz2L = sym.latex(diffz2Out)
diffz2S = sym.simplify(diffz2Out)
diffz2SL = sym.latex(diffz2S)

finalanswer = diffx2Out + diffy2Out + diffz2Out
finalanswerL = sym.latex(finalanswer)
finalanswerS = sym.simplify(finalanswer)
finalanswerSL = sym.latex(finalanswerS)

lapfsplit = "\\Rightarrow \\nabla^{{2}} f = \\left ( {0} \\right ) + \\left ( {1} \\right ) + \\left ( {2} \\right )".format(diffx2L, diffy2L, diffz2L)
lapfsolved = "\\Rightarrow \\nabla^{{2}} f = {0}".format(finalanswerL)
lapfsimp = "\\Rightarrow \\nabla^{{2}} f = {0}".format(finalanswerSL)

ax = plt.subplot(111)
ax.text(0.0, 1.0, r"$%s$" %(f), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 0.9, r"$%s$" %(lapf), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 0.8, r"$%s$" %(lapfsplit), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 0.7, r"$%s$" %(lapfsolved), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 0.6, r"$%s$" %(lapfsimp), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.axis('off')
plt.show()
