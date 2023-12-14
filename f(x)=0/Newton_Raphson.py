# Définition de la fonction à résoudre :
def f(x):
    return x **12 - 1.10

# Dérivée de la fonction f(x)
def f_prime(x):
    return 12*x**11
# Méthode de Newton-Raphson pour résoudre f(x) = 0
def newton_raphson(f, f_prime, x0, epsilon, max_iterations):
    iteration = 0
    while iteration < max_iterations:
        x1 = x0 - f(x0) / f_prime(x0)
        
        if abs(x1 - x0) < epsilon:
            print("Convergence après", iteration, "itérations.")
            return x1
        
        x0 = x1
        iteration += 1
    
    return "Pas de convergence après le nombre d'itérations donné."

# Paramètres initiaux
x0 = 0.5  # Estimation initiale
epsilon = 1.0e-10  # Tolérance pour la convergence
max_iterations = 100  # Nombre maximal d'itérations

# Résolution de l'équation f(x) = 0 avec la méthode de Newton-Raphson
solution = newton_raphson(f, f_prime, x0, epsilon, max_iterations)
print("La solution est :", solution)