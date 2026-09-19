# Méthode de la dichotomie
# Principe : si f(a) et f(b) sont de signes opposés, il y a une racine dans [a, b].
# On coupe l'intervalle en deux jusqu'à obtenir la précision voulue.

def f(x):
    return x**3 - 2*x - 5

def dichotomie(a, b, eps=1e-6, nmax=100):
    if f(a) * f(b) > 0:
        print("Erreur : f(a) et f(b) doivent être de signes opposés")
        return None
    n = 0
    while (b - a) / 2 > eps and n < nmax:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        n = n + 1
    print("Nombre d'itérations :", n)
    return (a + b) / 2

racine = dichotomie(2, 3)
print("Racine approchée :", racine)
print("f(racine) =", f(racine))
