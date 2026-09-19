# Décomposition de Cholesky : A = L * L^T
# Condition : A doit être symétrique définie positive.
# On résout ensuite A x = b : L y = b, puis L^T x = y.

from math import sqrt

def cholesky(A):
    n = len(A)
    L = [[0.0] * n for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            somme = 0
            for k in range(j):
                somme = somme + L[i][k] * L[j][k]
            if i == j:
                valeur = A[i][i] - somme
                if valeur <= 0:
                    print("Erreur : la matrice n'est pas définie positive")
                    return None
                L[i][j] = sqrt(valeur)
            else:
                L[i][j] = (A[i][j] - somme) / L[j][j]
    return L

def resoudre(L, b):
    n = len(b)
    # Descente : L y = b
    y = [0.0] * n
    for i in range(n):
        somme = 0
        for k in range(i):
            somme = somme + L[i][k] * y[k]
        y[i] = (b[i] - somme) / L[i][i]
    # Remontée : L^T x = y
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        somme = 0
        for k in range(i + 1, n):
            somme = somme + L[k][i] * x[k]
        x[i] = (y[i] - somme) / L[i][i]
    return x

A = [[4, 12, -16],
     [12, 37, -43],
     [-16, -43, 98]]
b = [1, 2, 3]

L = cholesky(A)
if L is not None:
    print("Matrice L :")
    for ligne in L:
        print(ligne)
    print("Solution x :", resoudre(L, b))
