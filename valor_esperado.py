import numpy as np
import matplotlib.pyplot as plt

def valor_esperado(valores, probabilidades):
    return sum(v * p for v, p in zip(valores, probabilidades))

# Valores de la variable aleatoria X
valores_x = np.array([1, 2, 3, 4, 5])

# Probabilidades asociadas (distribución uniforme)
probabilidades_x = np.array([0.2, 0.2, 0.2, 0.2, 0.2])

# Calcular el valor esperado para la distribución uniforme
E_X = valor_esperado(valores_x, probabilidades_x)

# Probabilidades simétricas
probabilidades_simetrica = np.array([0.1, 0.2, 0.4, 0.2, 0.1])
E_X_simetrica = valor_esperado(valores_x, probabilidades_simetrica)

# Probabilidades asimétricas
probabilidades_asimetrica = np.array([0.05, 0.1, 0.15, 0.3, 0.4])
E_X_asimetrica = valor_esperado(valores_x, probabilidades_asimetrica)

# Mostrar los resultados en consola
print(f"Valor esperado E[X] para distribución uniforme: {E_X}")
print(f"Valor esperado E[X] para distribución simétrica: {E_X_simetrica}")
print(f"Valor esperado E[X] para distribución asimétrica: {E_X_asimetrica}")

# Crear una figura para las gráficas
plt.figure(figsize=(10, 6))

# Gráfico para distribución uniforme
plt.subplot(1, 3, 1)
plt.plot(valores_x, probabilidades_x, color='blue', marker='o', linestyle='-', label='Probabilidades')
plt.axvline(E_X, color='red', linestyle='--', label=f'Valor Esperado = {E_X:.2f}')
plt.title('Distribución Uniforme')
plt.xlabel('Valores de X')
plt.ylabel('Probabilidad')
plt.legend()

# Gráfico para distribución simétrica
plt.subplot(1, 3, 2)
plt.plot(valores_x, probabilidades_simetrica, color='green', marker='o', linestyle='-', label='Probabilidades')
plt.axvline(E_X_simetrica, color='red', linestyle='--', label=f'Valor Esperado = {E_X_simetrica:.2f}')
plt.title('Distribución Simétrica')
plt.xlabel('Valores de X')
plt.legend()

# Gráfico para distribución asimétrica
plt.subplot(1, 3, 3)
plt.plot(valores_x, probabilidades_asimetrica, color='purple', marker='o', linestyle='-', label='Probabilidades')
plt.axvline(E_X_asimetrica, color='red', linestyle='--', label=f'Valor Esperado = {E_X_asimetrica:.2f}')
plt.title('Distribución Asimétrica')
plt.xlabel('Valores de X')
plt.legend()

# Ajustar el espacio entre subplots
plt.tight_layout()

# Mostrar la gráfica
plt.show()
