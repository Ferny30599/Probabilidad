import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definimos la función de densidad conjunta
def joint_pdf(x, y):
    return np.exp(-x - y)  # Ejemplo de densidad conjunta: e^(-x - y)

# Valores de x y y
x = np.linspace(0, 2, 100)
y = np.linspace(0, 2, 100)
X, Y = np.meshgrid(x, y)
Z = joint_pdf(X, Y)

# Crear la figura
fig = plt.figure(figsize=(12, 6))

# Gráfica en 3D de la función de densidad conjunta
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f_{X,Y}(x, y)')
ax.set_title('Función de Densidad Conjunta $f_{X,Y}(x, y)$')

plt.show()
