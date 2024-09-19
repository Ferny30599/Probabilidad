#Demostrar la regla de bayes como sigue:
#$P(y|x) = \frac{P(x,y)}{\sum_{i=1}^n P(x|y_i)P(y_i)}$ con valores de interés para y de {0,1} y valores de interés para x es $\mathbb{R}$.
import numpy as np

# Genera datos para y en {0, 1}
np.random.seed(42)
N = 100
y = np.random.randint(0, 2, N)  # y toma valores en {0, 1}

# Genera datos aleatorios para x en un rango de números reales
x = np.random.randint(-10, 10, N)

# Calcula P(x, y) utilizando la frecuencia de la intersección de x e y
def Pxinty(x_val, y_val, x, y):
  Nxy = np.sum((x == x_val) & (y == y_val))
  # print("Valores de X:")
  # print(x)
  # print("Valores de Y:")
  # print(y)
  #print( np.sum((x == x_val) & (y == y_val)))
  return Nxy / N

# Ejemplo para x_val = 2.5 y y_val = 1
x_val = 1
y_val = 1
P_x_y = Pxinty(x_val, y_val, x, y)
print(f"P(x={x_val}, y={y_val}) = {P_x_y}")

# Calcula P(x|y) como la frecuencia condicional
def P_xdadoy(x_val, y_val, x, y):
    Ny = np.sum(y == y_val)
    Nxdadoy = np.sum((x == x_val) & (y == y_val))
    return Nxdadoy / Ny

# Calcula P(y)
def P_y(y_val, y):
    return np.sum(y == y_val) / N

# Calcula los resultados para x_val = 2.5 y y_val = 1
Pxdadoy = P_xdadoy(x_val, y_val, x, y)
Py_val = P_y(y_val, y)

print(f"P(x={x_val} | y={y_val}) = {Pxdadoy}")
print(f"P(y={y_val}) = {Py_val}")

# Verificar la ecuación P(y|x) = P(x,y) / sum(P(x|y_i) * P(y_i))
def P_ydadox(x_val, y_val, x, y):
    numerador = Pxinty(x_val, y_val, x, y)
    denominador = sum(P_xdadoy(x_val, yi, x, y) * P_y(yi, y) for yi in [0, 1])
    print(f"P(y|x)={numerador}/{denominador}")
    return numerador / denominador

# Calcular P(y=0|x=2.5)
Pydadox0 = P_ydadox(x_val, 0, x, y)
print(f"P(y=0 | x={x_val}) = {Pydadox0}")

# Calcular P(y=1|x=2.5)
Pydadox1 = P_ydadox(x_val, 1, x, y)
print(f"P(y=1 | x={x_val}) = {Pydadox1}")
