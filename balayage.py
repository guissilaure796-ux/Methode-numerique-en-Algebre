# Méthode du balayage
# Principe : on parcourt [a, b] avec un pas h et on repère les intervalles
# où f change de signe. Chacun contient au moins une racine.

def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def balayage(a, b, h):
    intervalles = []
    n = int(round((b - a) / h))
    for i in range(n):
        x = a + i * h
        y = x + h
        if f(x) * f(y) < 0:
            intervalles.append((x, y))
    return intervalles

resultat = balayage(0.05, 4, 0.1)
print("Intervalles contenant une racine :")
for (g, d) in resultat:
    print("[", round(g, 2), ";", round(d, 2), "]")
