def decomposition_LU(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        L[i][i] = 1.0

        for k in range(i, n):
            sum = 0.0
            for j in range(i):
                sum += (L[i][j] * U[j][k])
            U[i][k] = A[i][k] - sum

        for k in range(i, n):
            sum = 0.0
            for j in range(i):
                sum += (L[k][j] * U[j][i])
            L[k][i] = (A[k][i] - sum) / U[i][i]

    return L, U

# Exemple de matrice
A = [
    [2, -1, 3],
    [4, 1, 3],
    [4, -1, 1]
]

# Calcul de la décomposition LU
L, U = decomposition_LU(A)

# Affichage des matrices L et U
print("Matrice L:")
for row in L:
    print(row)

print("\nMatrice U:")
for row in U:
    print(row)