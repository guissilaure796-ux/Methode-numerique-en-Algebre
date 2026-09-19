# Interpolation par la méthode de Vandermonde
# Principe : on cherche le polynôme P(x) = a0 + a1*x + a2*x^2 + ... + an*x^n
# qui passe par les points (x_i, y_i).
# Cela revient à résoudre le système V * a = y, où V est la matrice de Vandermonde :
#   V[i][j] = x_i^j

def matrice_vandermonde(xs):
    n = len(xs)
    V = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(xs[i] ** j)
        V.append(ligne)
    return V

def resoudre(A, b):
    # Résolution de A x = b par élimination de Gauss avec choix du pivot
    n = len(A)
    M = []
    for i in range(n):
        M.append(A[i][:] + [b[i]])
    for i in range(n):
        pivot = i
        for k in range(i + 1, n):
            if abs(M[k][i]) > abs(M[pivot][i]):
                pivot = k
        if abs(M[pivot][i]) < 1e-12:
            print("Erreur : les x_i doivent être deux à deux distincts")
            return None
        M[i], M[pivot] = M[pivot], M[i]
        for k in range(i + 1, n):
            coef = M[k][i] / M[i][i]
            for j in range(i, n + 1):
                M[k][j] = M[k][j] - coef * M[i][j]
    # Remontée
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        somme = 0
        for j in range(i + 1, n):
            somme = somme + M[i][j] * x[j]
        x[i] = (M[i][n] - somme) / M[i][i]
    return x

def evaluer(coef, x):
    # Évaluation de P(x) par la méthode de Horner
    resultat = 0
    for a in reversed(coef):
        resultat = resultat * x + a
    return resultat

# Points donnés (ici ceux de la fonction x^3 - 2x + 1)
xs = [0, 1, 2, 3]
ys = [1, 0, 5, 22]

V = matrice_vandermonde(xs)
print("Matrice de Vandermonde :")
for ligne in V:
    print(ligne)

coef = resoudre(V, ys)
print("Coefficients [a0, a1, a2, a3] :", coef)
print("P(1.5) =", evaluer(coef, 1.5))
print("Valeur exacte :", 1.5**3 - 2*1.5 + 1)
