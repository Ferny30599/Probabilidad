import numpy as np
import matplotlib.pyplot as plt

# Generar datos aleatorios para cuatro variables
n_samples = 1000
x1 = np.random.uniform(-5, 5, n_samples)
x2 = np.random.uniform(-5, 5, n_samples)
x3 = np.random.uniform(-5, 5, n_samples)
x4 = np.random.uniform(-5, 5, n_samples)

# Función de densidad conjunta para (x1, x2, x3, x4)
def densidad_conjunta(x1, x2, x3, x4):
    return np.exp(-0.1 * (x1**2 + x2**2 + x3**2 + x4**2))

# Función de densidad conjunta para (x1, x2)
def densidad_conjunta_x1_x2(x1, x2):
    return np.exp(-0.1 * (x1**2 + x2**2))

# Calcula la densidad conjunta y la densidad marginal
f_xyz = densidad_conjunta(x1, x2, x3, x4)
f_x1_x2 = densidad_conjunta_x1_x2(x1, x2)

# Calcular la densidad condicional h(y|x)
h_y_given_x = f_xyz / f_x1_x2

# Crear una malla de puntos para graficar en 3D
x1_grid, x2_grid = np.meshgrid(np.linspace(min(x1), max(x1), 50),
                               np.linspace(min(x2), max(x2), 50))
h_y_given_x_grid = np.exp(-0.1 * (x1_grid**2 + x2_grid**2))

# Crear el gráfico 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Grafica la superficie
ax.plot_surface(x1_grid, x2_grid, h_y_given_x_grid, cmap='viridis', alpha=0.8)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('h(y|x)')
ax.set_title('Densidad Condicional h(y|x)')

plt.show()

# Verificar algunos resultados
print("Ejemplos de densidad condicional h(y|x):")
print(h_y_given_x[:10])  # Muestra de los primeros valores
