# Interpolation par le schéma d'Aitken (Aitken-Neville)
# Principe : on calcule la valeur du polynôme d'interpolation en un point x
# sans jamais construire le polynôme, en remplissant un tableau.
#   P[i][0] = y_i
#   P[i][k] = ( (x - x_{i-k}) * P[i][k-1] - (x - x_i) * P[i-1][k-1] ) / (x_i - x_{i-k})
# La valeur cherchée est le dernier élément de la dernière ligne.

def aitken(xs, ys, x):
    n = len(xs)
    P = [[0.0] * n for i in range(n)]
    for i in range(n):
        P[i][0] = ys[i]
    for k in range(1, n):
        for i in range(k, n):
            P[i][k] = ((x - xs[i - k]) * P[i][k - 1] - (x - xs[i]) * P[i - 1][k - 1]) / (xs[i] - xs[i - k])
    return P

# Points donnés (ici ceux de la fonction x^3 - 2x + 1)
xs = [0, 1, 2, 3]
ys = [1, 0, 5, 22]
x = 1.5

P = aitken(xs, ys, x)
print("Tableau d'Aitken pour x =", x)
for ligne in P:
    print(ligne)
print("P(1.5) =", P[-1][-1])
print("Valeur exacte :", 1.5**3 - 2*1.5 + 1)
