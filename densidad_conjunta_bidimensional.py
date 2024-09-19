import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definimos la función de densidad conjunta
def joint_density(x, y):
    # Ejemplo de función de densidad conjunta: distribución normal bivariada
    mu_x, mu_y = 0, 0
    sigma_x, sigma_y = 1, 1
    rho = 0.5
    return (1 / (2 * np.pi * sigma_x * sigma_y * np.sqrt(1 - rho**2))) * \
           np.exp(- (1 / (2 * (1 - rho**2))) * ((x - mu_x)**2 / sigma_x**2 + (y - mu_y)**2 / sigma_y**2 - 2 * rho * (x - mu_x) * (y - mu_y) / (sigma_x * sigma_y)))

# Crear una malla de valores
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = joint_density(X, Y)

# Crear la figura
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Density')
ax.set_title('Función de Densidad Conjunta $f_{X,Y}(x, y)$')

plt.show()
