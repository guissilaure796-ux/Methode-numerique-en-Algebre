# Méthode de Richardson
# Formule : x^(k+1) = x^(k) + alpha * ( b - A * x^(k) )
# alpha est un paramètre. Pour A symétrique définie positive, la méthode converge
# si 0 < alpha < 2 / lambda_max, où lambda_max est la plus grande valeur propre de A.

def produit(A, x):
    n = len(A)
    resultat = []
    for i in range(n):
        somme = 0
        for j in range(n):
            somme = somme + A[i][j] * x[j]
        resultat.append(somme)
    return resultat

def richardson(A, b, x0, alpha, eps=1e-8, nmax=2000):
    n = len(A)
    x = x0[:]
    for k in range(nmax):
        Ax = produit(A, x)
        r = [b[i] - Ax[i] for i in range(n)]   # résidu
        x = [x[i] + alpha * r[i] for i in range(n)]
        if max(abs(v) for v in r) < eps:
            print("Nombre d'itérations :", k + 1)
            return x
    print("Pas de convergence")
    return x

A = [[4, 1, 0],
     [1, 4, 1],
     [0, 1, 4]]
b = [5, 6, 5]

# Les valeurs propres de A sont comprises entre 2 et 6, on prend alpha = 0.25
print("Solution x :", richardson(A, b, [0, 0, 0], 0.25))
