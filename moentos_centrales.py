import numpy as np
import matplotlib.pyplot as plt

def valor_esperado(valores, probabilidades):
    return sum(v * p for v, p in zip(valores, probabilidades))

# Valores de la variable aleatoria X
valores_x = np.array([1, 2, 3, 4, 5])

# Probabilidades asociadas (en este caso, distribución uniforme)
probabilidades_x = np.array([0.2, 0.2, 0.2, 0.2, 0.2])

# Calcular el valor esperado
E_X = valor_esperado(valores_x, probabilidades_x)

# Mostrar el resultado
print(f"Valor esperado E[X]: {E_X}")


# Calcular la media aritmética
media_aritmetica = np.mean(valores_x)

# Mostrar el resultado
print(f"Media aritmética de X: {media_aritmetica}")


# Probabilidades simétricas
probabilidades_simetrica = np.array([0.1, 0.2, 0.4, 0.2, 0.1])

# Calcular el valor esperado y la media aritmética
E_X_simetrica = valor_esperado(valores_x, probabilidades_simetrica)
media_aritmetica_simetrica = np.mean(valores_x)

# Mostrar los resultados
print(f"\nDistribución Simétrica:")
print(f"Valor esperado E[X]: {E_X_simetrica}")
print(f"Media aritmética: {media_aritmetica_simetrica}")


# Probabilidades asimétricas
probabilidades_asimetrica = np.array([0.05, 0.1, 0.15, 0.3, 0.4])

# Calcular el valor esperado y la media aritmética
E_X_asimetrica = valor_esperado(valores_x, probabilidades_asimetrica)
media_aritmetica_asimetrica = np.mean(valores_x)

# Mostrar los resultados
print(f"\nDistribución Asimétrica:")
print(f"Valor esperado E[X]: {E_X_asimetrica}")
print(f"Media aritmética: {media_aritmetica_asimetrica}")


import numpy as np
from math import comb  # Para el coeficiente binomial (n choose k)

# Función para calcular alpha_k
def alpha_k(valores, probabilidades, k):
    return np.sum((valores ** k) * probabilidades)

# Función para calcular los momentos centrales usando el teorema binomial
def momento_central_binomial(valores, probabilidades, n):
    # Primero, calcular la media (m)
    media = np.sum(valores * probabilidades)

    # Calcular los momentos crudos (alpha_k) para k = 0, 1, ..., n
    momentos = [alpha_k(valores, probabilidades, k) for k in range(n+1)]

    # Aplicar el teorema binomial para el momento central beta_n
    beta_n = 0
    for k in range(n+1):
        binom_coef = comb(n, k)  # Coeficiente binomial (n choose k)
        beta_n += binom_coef * (-media)**(n-k) * momentos[k]

    return beta_n

# Calcular la varianza utilizando la función de NumPy
def varianza(valores, probabilidades):
    varianza = np.var(valores, ddof=0)  # ddof=0 para la varianza de población
    return varianza

# Ejemplo: valores de un dado de seis caras con probabilidades uniformes
valores_X = np.array([1, 2, 3, 4, 5, 6])
probabilidades_X = np.array([1/6] * 6)  # Probabilidad uniforme


# Calcular el segundo momento central (beta_2 = varianza)
n=2
beta_n = momento_central_binomial(valores_X, probabilidades_X, n)
print(f'El momento central de orden {n} (beta_{n}) es: {beta_n}')

# Calcular la varianza
varianza_calculada = varianza(valores_X, probabilidades_X)
print(f'La varianza calculada con NumPy es: {varianza_calculada}')

Como el momento central y la varianza coincide, el teorema se cumple.
