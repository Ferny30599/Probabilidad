import numpy as np
import matplotlib.pyplot as plt

# Definición de parámetros
P_Y_1 = 0.2  # P(Y = 1)
P_X_1_given_Y_1 = 0.8  # P(X = 1 | Y = 1)
P_X_1_given_Y_0 = 0.1  # P(X = 1 | Y = 0)
P_Y_0 = 1 - P_Y_1  # P(Y = 0)

# Cálculo de P(X = 1) usando la regla de la suma
P_X_1 = P_X_1_given_Y_1 * P_Y_1 + P_X_1_given_Y_0 * P_Y_0

# Cálculo de P(Y = 1 | X = 1)
P_Y_1_given_X_1 = (P_X_1_given_Y_1 * P_Y_1) / P_X_1

# Datos para graficar
x_labels = ['P(Y = 1)', 'P(X = 1 | Y = 1)', 'P(X = 1 | Y = 0)', 'P(X = 1)', 'P(Y = 1 | X = 1)']
values = [P_Y_1, P_X_1_given_Y_1, P_X_1_given_Y_0, P_X_1, P_Y_1_given_X_1]

# Crear gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(x_labels, values, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.ylabel('Probabilidad')
plt.title('Probabilidades relacionadas con la Regla de Bayes')
plt.ylim(0, 1)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
