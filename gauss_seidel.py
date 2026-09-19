# Méthode de Gauss-Seidel
# Formule : x_i^(k+1) = ( b_i - somme_{j<i} a_ij * x_j^(k+1) - somme_{j>i} a_ij * x_j^(k) ) / a_ii
# Différence avec Jacobi : on utilise tout de suite les nouvelles valeurs calculées.
# Elle converge en général plus vite que Jacobi.

def gauss_seidel(A, b, x0, eps=1e-8, nmax=500):
    n = len(A)
    x = x0[:]
    for k in range(nmax):
        erreur = 0
        for i in range(n):
            somme = 0
            for j in range(n):
                if j != i:
                    somme = somme + A[i][j] * x[j]
            nouveau = (b[i] - somme) / A[i][i]
            erreur = max(erreur, abs(nouveau - x[i]))
            x[i] = nouveau
        if erreur < eps:
            print("Nombre d'itérations :", k + 1)
            return x
    print("Pas de convergence")
    return x

A = [[10, -1, 2],
     [-1, 11, -1],
     [2, -1, 10]]
b = [6, 25, -11]

print("Solution x :", gauss_seidel(A, b, [0, 0, 0]))
