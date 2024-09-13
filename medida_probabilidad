import numpy as np

# Generar 100 datos aleatorios (0 o 1)
n = 100
omega = np.random.randint(0, 2, n)

# Contar las ocurrencias de w1 (0) y w2 (1)
w1_count = np.sum(omega == 0)
w2_count = np.sum(omega == 1)

# Calcular las probabilidades de w1 y w2
P_w1 = w1_count / n
P_w2 = w2_count / n

# Verificar axioma de la probabilidad total
P_omega = P_w1 + P_w2

# Mostrar resultados
print(f'P(w1) = {P_w1}')
print(f'P(w2) = {P_w2}')
print(f'P(Omega) = {P_omega}')

# Verificación del axioma de la probabilidad total
assert np.isclose(P_omega, 1), "El axioma P(Omega) = 1 no se cumple."
