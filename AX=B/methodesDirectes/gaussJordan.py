def gauss_jordan(A, b):
    n = len(A)
    for i in range(n):
        # Pivotisation pour obtenir un élément diagonal non nul
        if A[i][i] == 0:
            for j in range(i+1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    b[i], b[j] = b[j], b[i]
                    break

        # Normalisation de la ligne i
        factor = A[i][i]
        for j in range(i, n):
            A[i][j] /= factor
        b[i] /= factor

        # Élimination de Gauss-Jordan
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(i, n):
                    A[k][j] -= factor * A[i][j]
                b[k] -= factor * b[i]

    return b

# Matrice d'exemple et vecteur résultant
A = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]
b = [8, -11, -3]

# Résolution du système d'équations linéaires avec Gauss-Jordan
solution = gauss_jordan(A, b)

print("Solution du système d'équations linéaires:")
print(solution)