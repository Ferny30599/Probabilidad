import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Función de densidad condicional h(y|x)
def h_y_given_x(y, x):
    return np.exp(-y)  # Exponencial para y >= 0

# Valor esperado condicional E[Y|X=x]
def valor_esperado_condicional(x):
    integral, error = quad(lambda y: y * h_y_given_x(y, x), 0, np.inf)
    return integral

# Generar valores de X y calcular E[Y|X=x]
x_values = np.linspace(0, 5, 100)
expected_values = [valor_esperado_condicional(x) for x in x_values]

# Graficar el valor esperado condicional
plt.figure(figsize=(8, 6))
plt.plot(x_values, expected_values, label=r'$E[Y|X=x]$', color='blue', lw=2)
plt.title(r'Valor Esperado Condicional $E[Y|X=x]$ para $h(y|x) = e^{-y}$')
plt.xlabel(r'$x$')
plt.ylabel(r'$E[Y|X=x]$')
plt.grid(True)
plt.legend()
plt.show()
