def crout(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        U[i][i] = 1.0

        for k in range(i, n):
            sum = 0.0
            for j in range(i):
                sum += L[k][j] * U[j][i]
            L[k][i] = A[k][i] - sum

        for k in range(i + 1, n):
            sum = 0.0
            for j in range(i):
                sum += L[i][j] * U[j][k]
            U[i][k] = (A[i][k] - sum) / L[i][i]

    return L, U

# Matrice d'exemple
A = [
    [2, -1, 3],
    [4, 1, 3],
    [4, -1, 1]
]

# Obtenir la décomposition LU avec la méthode de Crout
L, U = crout(A)

print("Matrice L:")
for row in L:
    print(row)

print("\nMatrice U:")
for row in U:
    print(row)