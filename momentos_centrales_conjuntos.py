import numpy as np

# Función para calcular el momento central conjunto
def beta_jk(X1, X2, j, k, probabilidades):
    # Calcular las medias de X1 y X2
    m1 = np.sum(X1 * probabilidades)
    m2 = np.sum(X2 * probabilidades)

    # Calcular el momento central conjunto \beta_{jk}
    beta = np.sum(((X1 - m1)**j) * ((X2 - m2)**k) * probabilidades)

    return beta

# Ejemplo: valores de dos variables aleatorias con probabilidades conjuntas uniformes
X1 = np.array([1, 2, 3, 4, 5])
X2 = np.array([1, 2, 3, 4, 5])
probabilidades_conjuntas = np.full(len(X1), 1/len(X1))  # Probabilidad uniforme

# Calcular el momento central conjunto de orden (1,1)
momento_conjunto_11 = beta_jk(X1, X2, 1, 1, probabilidades_conjuntas)
print(f'Momento central conjunto (1,1): {momento_conjunto_11}')

# Calcular la covarianza usando la función de numpy
# Necesitamos ajustar la forma de los datos para numpy.cov
X = np.array([X1, X2])
cov_matrix = np.cov(X, bias=True)
cov_X1_X2 = cov_matrix[0, 1]  # Extraer la covarianza entre X1 y X2

print(f'Covarianza calculada usando numpy.cov: {cov_X1_X2}')

#Como el momento central conjunto $\beta_{1,1}$ y la covarianza coincide, el teorema se cumple.
