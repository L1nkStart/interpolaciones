import matplotlib.pyplot as plt

def hermite_interpolation(x_values, x_nodes, y_nodes, y_derivatives):
    def product_term(i, x):
        result = 1
        for j in range(i):
            result *= (x - z[j])
        return result

    n = len(x_nodes)
    z = [0] * (2 * n)  # Vector que duplica los nodos
    Q = [[0] * (2 * n) for _ in range(2 * n)]  # Matriz de diferencias divididas

    # Inicialización de las tablas Q y z
    for i in range(n):
        z[2 * i] = z[2 * i + 1] = x_nodes[i]
        Q[2 * i][0] = Q[2 * i + 1][0] = y_nodes[i]
        Q[2 * i + 1][1] = y_derivatives[i]
        if i != 0:
            Q[2 * i][1] = (Q[2 * i][0] - Q[2 * i - 1][0]) / (z[2 * i] - z[2 * i - 1])

    # Cálculo de las diferencias divididas
    for i in range(2, 2 * n):
        for j in range(2, i + 1):
            Q[i][j] = (Q[i][j - 1] - Q[i - 1][j - 1]) / (z[i] - z[i - j])

    # Evaluación del polinomio interpolador
    interpolated_values = []
    for x in x_values:
        result = 0
        for i in range(2 * n):
            term = Q[i][i]
            term *= product_term(i, x)
            result += term
        interpolated_values.append(result)

    return interpolated_values

# Datos proporcionados
x_nodes = [-1, -2]  # Nodos en x
y_nodes = [-9, 12]  # Valores de la función en los nodos
y_derivatives = [10, 13]  # Derivadas de la función en los nodos

# Generar valores de x para la gráfica
x_values_to_plot = [x / 100.0 for x in range(-300, 101)]
y_values_to_plot = hermite_interpolation(x_values_to_plot, x_nodes, y_nodes, y_derivatives)

# Graficar
plt.plot(x_values_to_plot, y_values_to_plot, label='Polinomio de Hermite')
plt.scatter(x_nodes, y_nodes, color='red', zorder=5)
plt.title('Interpolación de Hermite')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
