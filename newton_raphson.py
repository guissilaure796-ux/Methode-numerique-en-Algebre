# Méthode de Newton-Raphson pour un système de deux équations non linéaires
# Formule : X_{n+1} = X_n - J(X_n)^(-1) * F(X_n)
# où J est la matrice jacobienne (les dérivées partielles).
# Exemple : x^2 + y^2 = 4  et  x*y = 1

def F(x, y):
    return [x**2 + y**2 - 4, x*y - 1]

def J(x, y):
    return [[2*x, 2*y],
            [y,   x]]

def newton_raphson(x0, y0, eps=1e-10, nmax=50):
    x = x0
    y = y0
    for n in range(nmax):
        f1, f2 = F(x, y)
        a, b = J(x, y)[0]
        c, d = J(x, y)[1]
        det = a*d - b*c
        if det == 0:
            print("Erreur : jacobienne non inversible")
            return None
        # On résout J * delta = -F par la formule de Cramer
        dx = (-f1*d + f2*b) / det
        dy = (-f2*a + f1*c) / det
        x = x + dx
        y = y + dy
        if abs(dx) < eps and abs(dy) < eps:
            print("Nombre d'itérations :", n + 1)
            return x, y
    print("Pas de convergence")
    return None

solution = newton_raphson(2, 0.5)
print("Solution approchée (x, y) :", solution)
print("Vérification F(x, y) :", F(solution[0], solution[1]))
