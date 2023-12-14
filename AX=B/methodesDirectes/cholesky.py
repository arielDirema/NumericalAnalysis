import numpy as np

def cholesky(A):
    n = len(A)
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i+1):
            sum = 0
            if j == i:
                for k in range(j):
                    sum += L[j][k] ** 2
                L[j][j] = np.sqrt(A[j][j] - sum)
            else:
                for k in range(j):
                    sum += L[i][k] * L[j][k]
                L[i][j] = (A[i][j] - sum) / L[j][j]

    return L

# Matrice d'exemple (symétrique définie positive)
A = np.array([
    [4, 12, -16],
    [12, 37, -43],
    [-16, -43, 98]
])

# Décomposition de Cholesky
L = cholesky(A)

print("Matrice L (Résultat de la décomposition de Cholesky) :")
print(L)