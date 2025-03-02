# Desarrollado por Juan Diego Cordero.

import sympy as sp
from math import factorial
from matplotlib import pyplot as plt

class Taylor:
    # Método constructor de la clase Taylor.
    def __init__(self, x, fx, n, x0, k = 0, polinomio = 0):
        self.x = x
        self.fx = fx
        self.n = n
        self.x0 = x0
        self.k = k
        self.polinomio = polinomio
    
    # Método que ejecuta la interpolación de Taylor.
    def interpolacion(self):
        while not (self.k > self.n):
            f = self.fx.diff(self.x, self.k)
            f0 = f.subs(self.x, self.x0)
            divisor = factorial(self.k)
            self.polinomio += (f0/divisor)*(self.x - self.x0)**self.k
            self.k += 1
        print(f"f(x) = {self.fx}\nP(x) = {self.polinomio}\n")

    # Método para graficar la interpolación de Taylor.
    def graficarinterpolacion(self, a, b):
        x = [a + i * 0.1 for i in range(int((b - a) / 0.1))]
        y = [self.fx.subs(self.x, valor) for valor in x]
        p = sp.lambdify(self.x, self.polinomio, 'numpy')
        tp = [p(valor) for valor in x]
        plt.plot(x, y, label='f(x)')
        plt.plot(x, tp, label='Polinomio de Taylor')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Interpolación de Taylor')
        plt.grid()
        plt.legend()
        plt.show()
     
# Interpolación 1: f(x) = e^x, n = 4, x0 = 0.}
x = sp.symbols('x')
fx = sp.exp(x)
n = 4
x0 = 0
t1 = Taylor(x, fx, n, x0)
t1.interpolacion()
li = -4
ls = 4
t1.graficarinterpolacion(li, ls)

# Interpolación 2: f(x) = 1/x, n = 4, x0 = 1.
x = sp.symbols('x')
fx = 1/x
n = 4
x0 = 1
t2 = Taylor(x, fx, n, x0)
t2.interpolacion()
a = 0.1
b = 4
t2.graficarinterpolacion(a, b)

# Interpolación 3: f(x) = x^(1/2), n = 2, x0 = 64.
x = sp.symbols('x')
fx = sp.sqrt(x)
n = 2
x0 = 64
t3 = Taylor(x, fx, n, x0)
t3.interpolacion()
a = 0
b = 80
t3.graficarinterpolacion(a, b)