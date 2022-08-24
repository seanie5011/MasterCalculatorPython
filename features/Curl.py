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
curlF = r"\nabla \times \bar{F} = \left ( \frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z}\right )\hat{\imath} - \left ( \frac{\partial F_z}{\partial x} - \frac{\partial F_x}{\partial z} \right )\hat{\jmath} + \left ( \frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y} \right )\hat{k}"

diffzyOut = sym.diff(f3InSym, y, 1)
diffzyL = sym.latex(diffzyOut)
diffyzOut = sym.diff(f2InSym, z, 1)
diffyzL = sym.latex(diffyzOut)
curliS = sym.simplify(diffzyOut - diffyzOut)
curliSL = sym.latex(curliS)

diffzxOut = sym.diff(f3InSym, x, 1)
diffzxL = sym.latex(diffzxOut)
diffxzOut = sym.diff(f1InSym, z, 1)
diffxzL = sym.latex(diffxzOut)
curljS = sym.simplify(diffxzOut - diffzxOut)
curljSL = sym.latex(curljS)

diffyxOut = sym.diff(f2InSym, x, 1)
diffyxL = sym.latex(diffyxOut)
diffxyOut = sym.diff(f1InSym, y, 1)
diffxyL = sym.latex(diffxyOut)
curlkS = sym.simplify(diffyxOut - diffxyOut)
curlkSL = sym.latex(curlkS)

curlFsolved = "\\Rightarrow \\nabla \\times \\bar{{F}} = \\left ( {0} - {1} \\right )\\hat{{\\imath}} + \\left ( {2} - {3} \\right )\\hat{{\\jmath}} + \\left ( {4} - {5} \\right )\\hat{{k}}".format(diffzyL, diffyzL, diffzxL, diffxzL, diffyxL, diffxyL)
curlFsimp = "\\Rightarrow \\nabla \\times \\bar{{F}} = \\left ( {0} \\right )\\hat{{\\imath}} + \\left ( {1} \\right )\\hat{{\\jmath}} + \\left ( {2} \\right )\\hat{{k}}".format(curliSL, curljSL, curlkSL)


ax = plt.subplot(111)
ax.text(0.0, 1.0, r"$%s$" %(F), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 0.9, r"$%s$" %(curlF), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 0.7, r"$%s$" %(curlFsolved), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.text(0.0, 0.6, r"$%s$" %(curlFsimp), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.axis('off')
plt.show()