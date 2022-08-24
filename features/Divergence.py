import sympy as sym
import matplotlib
import matplotlib.pyplot as plt

x, y, z, t = sym.symbols('x y z t')

f1InStr = input("Please input your vector as in standard format, F = (F1, F2, F3):\nF1 = ")
f1InSym = sym.sympify(f1InStr)
f1InL = sym.latex(f1InSym)
f2InStr = input("F2 = ")
f2InSym = sym.sympify(f2InStr)
f2InL = sym.latex(f2InSym)
f3InStr = input("F3 = ")
f3InSym = sym.sympify(f3InStr)
f3InL = sym.latex(f3InSym)

F = f"\\bar{{F}} = \\left ( {f1InL}, {f2InL}, {f3InL} \\right )"
divF = r"\nabla \cdot \bar{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}"

diffxOut = sym.diff(f1InSym, x, 1)
diffxL = sym.latex(diffxOut)
diffyOut = sym.diff(f2InSym, y, 1)
diffyL = sym.latex(diffyOut)
diffzOut = sym.diff(f3InSym, z, 1)
diffzL = sym.latex(diffzOut)

finalanswer = diffxOut + diffyOut + diffzOut
finalanswerL = sym.latex(finalanswer)
finalanswerS = sym.simplify(finalanswer)
finalanswerSL = sym.latex(finalanswerS)

divFsplit = "\\Rightarrow \\nabla \\cdot \\bar{{F}} = \\left ( {0} \\right ) + \\left ( {1} \\right ) + \\left ( {2} \\right )".format(diffxL, diffyL, diffzL)
divFsolved = "\\Rightarrow \\nabla \\cdot \\bar{{F}} = {0}".format(finalanswerL)
divFsimp = "\\Rightarrow \\nabla \\cdot \\bar{{F}} = {0}".format(finalanswerSL)

ax = plt.subplot(111)
ax.text(0.0, 1.0, r"$%s$" %(F), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 0.9, r"$%s$" %(divF), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 0.8, r"$%s$" %(divFsplit), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 0.7, r"$%s$" %(divFsolved), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 0.6, r"$%s$" %(divFsimp), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.axis('off')
plt.show()
