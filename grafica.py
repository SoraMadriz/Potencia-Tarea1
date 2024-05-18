import sympy as sp
import matplotlib.pyplot as plt

# Declarar la variable simbólica x
x = sp.symbols('x')

# Declarar la función f(x) utilizando sympy
def f(x):
    return x**2  # Ejemplo de función cuadrática

# Crear una lista de 50 valores para x
x_values = list(range(50))

# Calcular los valores de f(x) para cada x
y_values = [f(x_val) for x_val in x_values]

# Graficar la función
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico de f(x)')
plt.show()
