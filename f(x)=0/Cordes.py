def f(x):
    return x **12 - 1.10

# Méthode des cordes pour résoudre f(x) = 0
def methode_des_cordes(f, x0, x1, epsilon, max_iterations):
    iteration = 0
    
    while iteration < max_iterations:
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        
        if abs(f(x2)) < epsilon:
            print("Le nombre d'itérations est : ", iteration)
            return x2
        
        x0 = x1
        x1 = x2
        iteration += 1
    
    return "Pas de convergence après le nombre d'itérations donné."

# Paramètres initiaux
x0 = 1  # Premier point initial
x1 = 1.5  # Deuxième point initial
epsilon = 1.0e-10  # Tolérance pour la convergence
max_iterations = 100  # Nombre maximal d'itérations

# Résolution de l'équation f(x) = 0 avec la méthode des cordes
solution = methode_des_cordes(f, x0, x1, epsilon, max_iterations)
print("La solution est :", solution)