import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# Función para calcular el coeficiente binomial
def coeficiente_binomial(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

# Función para calcular la distribución binomial
def distribucion_binomial(n, p, k):
    return coeficiente_binomial(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Parámetros dados
n = 5  # Número de lanzamientos
p = 1/6  # Probabilidad de obtener un 6 en un lanzamiento
k = 2  # Número de éxitos deseados (sacar un 6)

# Calcular la probabilidad de obtener exactamente 2 veces un 6 en 5 lanzamientos
probabilidad_k_2 = distribucion_binomial(n, p, k)
print(f'La probabilidad de obtener exactamente {k} veces un 6 en {n} lanzamientos es: {probabilidad_k_2}')

# Calcular y graficar toda la distribución para k = 0, 1, ..., n
k_values = np.arange(0, n + 1)
probabilidades = [distribucion_binomial(n, p, k_val) for k_val in k_values]

plt.plot(k_values, probabilidades, marker='o', linestyle='-', color='blue')
plt.xlabel('Número de éxitos (k)')
plt.ylabel('Probabilidad')
plt.title(f'Distribución Binomial (n={n}, p={p:.2f})')
plt.grid(True)
plt.show()

# Sumar todas las probabilidades
suma_probabilidades = np.sum(probabilidades)

# Verificar que la suma sea 1
print(f'Suma de todas las probabilidades: {suma_probabilidades}')
