# Méthode de Gauss-Jordan
# Principe : on transforme la matrice augmentée [A | b] pour que A devienne
# la matrice identité. La dernière colonne donne alors directement la solution.

def gauss_jordan(A, b):
    n = len(A)
    # Matrice augmentée
    M = []
    for i in range(n):
        M.append(A[i][:] + [b[i]])

    for i in range(n):
        # Choix du pivot (plus grand élément en valeur absolue)
        pivot = i
        for k in range(i + 1, n):
            if abs(M[k][i]) > abs(M[pivot][i]):
                pivot = k
        if abs(M[pivot][i]) < 1e-12:
            print("Erreur : matrice singulière")
            return None
        M[i], M[pivot] = M[pivot], M[i]

        # On divise la ligne i par le pivot
        p = M[i][i]
        for j in range(n + 1):
            M[i][j] = M[i][j] / p

        # On annule la colonne i dans toutes les autres lignes
        for k in range(n):
            if k != i:
                coef = M[k][i]
                for j in range(n + 1):
                    M[k][j] = M[k][j] - coef * M[i][j]

    return [M[i][n] for i in range(n)]

A = [[2, 1, -1],
     [-3, -1, 2],
     [-2, 1, 2]]
b = [8, -11, -3]

print("Solution x :", gauss_jordan(A, b))
