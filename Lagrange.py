import matplotlib.pyplot as plt

class Lagrange:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.polinomio = None  # Funcion de interpolacion(Definiremos despues)
    
    # Metodo para calcular la interpolacion de Lagrange
    def interpolacion(self):
        def lagrange_basis(i, xi):
            term = 1
            for j in range(len(self.x)):
                if i != j:
                    term *= (xi - self.x[j]) / (self.x[i] - self.x[j])
            return term
        
        def lagrange_interpolate(xi):
            yi = 0
            for i in range(len(self.x)):
                yi += self.y[i] * lagrange_basis(i, xi)
            return yi

        self.polinomio = lagrange_interpolate  
        print("Interpolacion de Lagrange realizada.")
    
    # Metodo para graficar la interpolacion de Lagrange
    def graficarinterpolacion(self, a, b):
        x_interp = [a + i * (b - a) / 99 for i in range(100)]
        y_interp = [self.polinomio(xi) for xi in x_interp]
        
        plt.figure(figsize=(8, 5))
        plt.plot(x_interp, y_interp, label='Interpolacion de Lagrange', linestyle='--')
        plt.scatter(self.x, self.y, color='red', label='Datos originales')
        plt.xlabel('Dias')
        plt.ylabel('Temperatura (°C)')
        plt.title('Interpolacion de Lagrange de Temperaturas')
        plt.legend()
        plt.grid()
        plt.show()

# Datos de temperatura para una semana
dias = [1, 2, 3, 4, 5, 6, 7]  
temperaturas = [15, 17, 20, 22, 21, 19, 16]  

# Ejecutar la interpolacion
lagrange_interp = Lagrange(dias, temperaturas)
lagrange_interp.interpolacion()

# Graficar la interpolacion en el rango dado
lagrange_interp.graficarinterpolacion(1, 7)
