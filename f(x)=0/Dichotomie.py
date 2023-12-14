import math


def dichotomie(f, a, b, epsilon):
    i = 0;
    while (b - a) > epsilon:
        
        m = (a + b) / 2
        if abs(f(m)) < epsilon: #or f(m) == 0:
            print(i)
            return m
        
        #    return b
        elif f(a) * f(b) > 0:
            return"Pas de solution sur cet intervalle"
        elif f(a) * f(m) < 0:
            b = m
            i += 1
        else:
            a = m
            i += 1
def main():
    a = 1
    b = 1.5
    epsilon = 1.0e-10
    if a > b:
        print("*****Intervalle incorrect : a doit être inférieur à b*****")
    else:
        #Resolution de l'eqn
        solution = dichotomie(lambda x: x **12 - 1.10, a, b, epsilon)
        print("x : ", solution)
    
if __name__ == "__main__":
    main()
