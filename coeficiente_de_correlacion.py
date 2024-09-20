import numpy as np

# Función para calcular la covarianza
def covarianza(X1, X2, probabilidades):
    m1 = np.sum(X1 * probabilidades)
    m2 = np.sum(X2 * probabilidades)
    cov = np.sum((X1 - m1) * (X2 - m2) * probabilidades)
    return cov

# Función para calcular la varianza
def varianza(X, probabilidades):
    m = np.sum(X * probabilidades)
    var = np.sum((X - m)**2 * probabilidades)
    return var

# Función para calcular el coeficiente de correlación
def coeficiente_correlacion(X1, X2, probabilidades):
    cov = covarianza(X1, X2, probabilidades)
    sigma_X1 = np.sqrt(varianza(X1, probabilidades))
    sigma_X2 = np.sqrt(varianza(X2, probabilidades))
    rho = cov / (sigma_X1 * sigma_X2)
    return rho

# Ejemplo: valores de dos variables aleatorias con probabilidades conjuntas uniformes
X1 = np.array([1, 2, 3, 4, 5])
X2 = np.array([5, 4, 3, 2, 1])
probabilidades_conjuntas = np.full(len(X1), 1/len(X1))  # Probabilidad uniforme

# Calcular el coeficiente de correlación
rho = coeficiente_correlacion(X1, X2, probabilidades_conjuntas)
print(f'Coeficiente de correlación ρ(X1, X2): {rho}')

# Validar el resultado usando numpy.corrcoef
X = np.array([X1, X2])
correlation_matrix = np.corrcoef(X)
rho_numpy = correlation_matrix[0, 1]  # Extraer el coeficiente de correlación entre X1 y X2

print(f'Coeficiente de correlación ρ(X1, X2) usando numpy.corrcoef: {rho_numpy}')
