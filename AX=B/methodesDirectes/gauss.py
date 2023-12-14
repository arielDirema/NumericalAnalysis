def gauss_elimination(A, b):
    n = len(A)

    for i in range(n):
        pivot = A[i][i]
        if pivot == 0:
            raise ValueError("La matrice n'est pas inversible (pivot = 0)")

        for j in range(i + 1, n):
            factor = A[j][i] / pivot
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    # Rétro-substitution pour trouver les valeurs de x
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A[i][i]
        for j in range(i - 1, -1, -1):
            b[j] -= A[j][i] * x[i]

    return x

# Matrice d'exemple et vecteur résultant
A = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]
b = [8, -11, -3]

# Résolution du système d'équations linéaires avec la méthode de Gauss
solution = gauss_elimination(A, b)

print("Solution du système d'équations linéaires:")
print(solution)