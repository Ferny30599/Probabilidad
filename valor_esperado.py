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
