# Méthode de Jacobi
# Formule : x_i^(k+1) = ( b_i - somme_{j != i} a_ij * x_j^(k) ) / a_ii
# Toutes les composantes sont calculées avec les valeurs de l'itération précédente.
# Convergence assurée si A est à diagonale strictement dominante.

def jacobi(A, b, x0, eps=1e-8, nmax=500):
    n = len(A)
    x = x0[:]
    for k in range(nmax):
        x_nouveau = [0.0] * n
        for i in range(n):
            somme = 0
            for j in range(n):
                if j != i:
                    somme = somme + A[i][j] * x[j]
            x_nouveau[i] = (b[i] - somme) / A[i][i]
        erreur = max(abs(x_nouveau[i] - x[i]) for i in range(n))
        x = x_nouveau
        if erreur < eps:
            print("Nombre d'itérations :", k + 1)
            return x
    print("Pas de convergence")
    return x

A = [[10, -1, 2],
     [-1, 11, -1],
     [2, -1, 10]]
b = [6, 25, -11]

print("Solution x :", jacobi(A, b, [0, 0, 0]))
