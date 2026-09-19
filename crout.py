# Décomposition de Crout : A = L * U
# L est triangulaire inférieure, U est triangulaire supérieure avec 1 sur la diagonale.
# On résout ensuite A x = b en deux étapes : L y = b, puis U x = y.

def crout(A):
    n = len(A)
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]
    for i in range(n):
        U[i][i] = 1.0
    for j in range(n):
        for i in range(j, n):
            somme = 0
            for k in range(j):
                somme = somme + L[i][k] * U[k][j]
            L[i][j] = A[i][j] - somme
        if L[j][j] == 0:
            print("Erreur : pivot nul")
            return None, None
        for i in range(j + 1, n):
            somme = 0
            for k in range(j):
                somme = somme + L[j][k] * U[k][i]
            U[j][i] = (A[j][i] - somme) / L[j][j]
    return L, U

def resoudre(L, U, b):
    n = len(b)
    # Descente : L y = b
    y = [0.0] * n
    for i in range(n):
        somme = 0
        for k in range(i):
            somme = somme + L[i][k] * y[k]
        y[i] = (b[i] - somme) / L[i][i]
    # Remontée : U x = y
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        somme = 0
        for k in range(i + 1, n):
            somme = somme + U[i][k] * x[k]
        x[i] = y[i] - somme
    return x

A = [[2, 1, 1],
     [4, 3, 3],
     [8, 7, 9]]
b = [4, 10, 24]

L, U = crout(A)
print("Matrice L :")
for ligne in L:
    print(ligne)
print("Matrice U :")
for ligne in U:
    print(ligne)
print("Solution x :", resoudre(L, U, b))
