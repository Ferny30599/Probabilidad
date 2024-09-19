import numpy as np

# Función para calcular la probabilidad conjunta P_{XY}(x, y)
def joint_probability(x, y, data_x, data_y):
    total_samples = len(data_x)
    count_joint = np.sum((data_x == x) & (data_y == y))
    return count_joint / total_samples

# Función para calcular la probabilidad marginal P_X(x)
def marginal_probability_x(x, data_x, data_y, omega_y):
    return sum(joint_probability(x, y, data_x, data_y) for y in omega_y)

# Función para calcular la probabilidad marginal P_Y(y)
def marginal_probability_y(y, data_x, data_y, omega_x):
    return sum(joint_probability(x, y, data_x, data_y) for x in omega_x)

# Generar datos aleatorios para X e Y
data_x = np.random.randint(0, 2, 100)  # 100 muestras de {0, 1}
data_y = np.random.randint(0, 2, 100)  # 100 muestras de {0, 1}

# Definir el espacio muestral para X e Y
omega_x = np.unique(data_x)
omega_y = np.unique(data_y)

# Calcular las probabilidades marginales para X y Y
prob_marginal_x = {x: marginal_probability_x(x, data_x, data_y, omega_y) for x in omega_x}
prob_marginal_y = {y: marginal_probability_y(y, data_x, data_y, omega_x) for y in omega_y}

# Mostrar los resultados
print("Probabilidades marginales para X:")
for x in omega_x:
    print(f"P_X({x}) = {prob_marginal_x[x]}")

print("\nProbabilidades marginales para Y:")
for y in omega_y:
    print(f"P_Y({y}) = {prob_marginal_y[y]}")

# Verificar que las sumas de las probabilidades marginales sean 1
suma_prob_marginal_x = sum(prob_marginal_x.values())
suma_prob_marginal_y = sum(prob_marginal_y.values())

print(f"\nSuma de las probabilidades marginales para X: {suma_prob_marginal_x}")
print(f"Suma de las probabilidades marginales para Y: {suma_prob_marginal_y}")
