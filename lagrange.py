# Interpolation de Lagrange
# Principe : trouver le polynôme qui passe par tous les points donnés.
# P(x) = somme de y_i * L_i(x)
# avec L_i(x) = produit de (x - x_j) / (x_i - x_j) pour j différent de i

def lagrange(xs, ys, x):
    n = len(xs)
    somme = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if j != i:
                L = L * (x - xs[j]) / (xs[i] - xs[j])
        somme = somme + ys[i] * L
    return somme

# Points donnés (ici ceux de la fonction x^2)
xs = [0, 1, 2, 3]
ys = [0, 1, 4, 9]

print("P(1.5) =", lagrange(xs, ys, 1.5))
print("Valeur exacte :", 1.5**2)
