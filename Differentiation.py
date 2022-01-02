import sympy as sym
import matplotlib
import matplotlib.pyplot as plt

x, y, z, t = sym.symbols('x y z t')

exprInStr = input("Please Input your equation as in standard format:\ny = ")
exprInSym = sym.sympify(exprInStr)

diffFinal = int(input("Please input the value of the derivative you wish to compute (any previous will also be computed): "))

exprIn = []
exprOut = []
exprEq = []

val = 0
while val <= diffFinal:
    if val != 0:
        In = sym.Derivative(exprInSym, x, val)
        Out = sym.diff(exprInSym, x, val)
        Eq = sym.Eq(In, Out)
    elif val == 0:
        Eq = sym.Eq(y, exprInSym)
    exprEq.append(sym.latex(Eq))
    print(f"Expr{val} = {sym.latex(Eq)}")
    val += 1

ax = plt.subplot(111)
for val1 in range(len(exprEq)):
    ax.text(0.0, 1.0 - val1*0.1, r"$%s$" %(exprEq[val1]), horizontalalignment = 'left', verticalalignment = 'center', fontsize = 14, color = "black")
ax.axis('off')
plt.show()