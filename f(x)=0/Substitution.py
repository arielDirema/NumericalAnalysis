from math import *;
from decimal import *;

# Fonction représentant l'équation
def equation(x):
    return Decimal(x) **12 - Decimal('1.10')

def substitution(f, x0, n_iterations=100, epsilon=1e-10):
    x = x0
    
    x = Decimal(x)

    for i in range(n_iterations):
        x_new = f(x)

        # Critère de convergence
        if abs(x_new - x) < epsilon:
            return x_new
        
        x = x_new

    return x

# Fonction représentant l'équation
#def equation(x):
    #return x **12 - 1.10

# Valeur initiale pour x
x0 = 1.5

# Résolution de l'équation f(x) = 0 avec la méthode de substitution
solution = substitution(equation, x0)

print("Solution de l'équation  :")
print(solution)