# Méthode de Newton
# Formule : x_{n+1} = x_n - f(x_n) / f'(x_n)

def f(x):
    return x**2 - 2

def df(x):
    return 2*x

def newton(x0, eps=1e-8, nmax=50):
    x = x0
    for n in range(nmax):
        if df(x) == 0:
            print("Erreur : dérivée nulle")
            return None
        x_suivant = x - f(x) / df(x)
        if abs(x_suivant - x) < eps:
            print("Nombre d'itérations :", n + 1)
            return x_suivant
        x = x_suivant
    print("Pas de convergence")
    return None

racine = newton(1)
print("Racine approchée de sqrt(2) :", racine)
