# Définition de la fonction à résoudre :
def f(x):
    return x **12 - 1.10

def dichotomie(f, a, b, epsilon):
    i = 0;
    
    while True:
        m = (a + b) / 2
        if abs(f(m)) < epsilon:
            print("nbre itération : ", i)
            return m
        elif f(a) * f(b) > 0:
            return"Pas de solution sur cet intervalle"
        elif f(a) * f(m) < 0:
            b = m
            i += 1
        elif f(a) * f(m) > 0:
            a = m
            i += 1
            
            
a = 1
b = 1.5
epsilon = 1.0e-10

solution = dichotomie(f, a, b, epsilon)
print("x : ", solution)