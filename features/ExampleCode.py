import sympy as sym
import matplotlib as mpl
import matplotlib.pyplot as plt
from io import BytesIO

x, y, z, t = sym.symbols('x y z t')

expr1 = sym.Derivative(x**4, x, 3)
sym.pprint(expr1, use_unicode=False)
print(sym.latex(expr1))

expr2 = sym.diff(x**4, x, 3)
expr3 = sym.Eq(expr1, expr2)
sym.pprint(expr3, use_unicode=False)
print(sym.latex(expr3))

M = sym.Matrix([[1, 2, 3], [3, 2, 1]])
sym.pprint(M, use_unicode=False)
print(sym.latex(M))

ax = plt.subplot(111)
ax.text(0.0, 1.0, r"$%s$" %(sym.latex(expr3)), fontsize=20, color="black")
ax.axis('off')
plt.show()