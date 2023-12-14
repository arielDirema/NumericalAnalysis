def jacobi(A, b, n_iterations=25, epsilon=1e-10):
    n = len(A)
    x = [0.0] * n  # Initialisation de la solution x

    for iteration in range(n_iterations):
        x_new = [0.0] * n  # Initialisation du nouveau vecteur x

        for i in range(n):
            sum = 0.0
            for j in range(n):
                if j != i:
                    sum += A[i][j] * x[j]
            x_new[i] = (b[i] - sum) / A[i][i]

        # Critère de convergence
        error = max([abs(x_new[i] - x[i]) for i in range(n)])
        if error < epsilon:
            return x_new

        x = x_new  # Mise à jour de x pour l'itération suivante

    return x

# Matrice d'exemple et vecteur résultant
A = [
    [4, -1, 0],
    [-1, 4, -1],
    [0, -1, 3]
]
b = [12, -1, 0]

# Résolution du système d'équations linéaires avec la méthode de Jacobi
solution = jacobi(A, b)

print("Solution du système d'équations linéaires:")
print(solution)