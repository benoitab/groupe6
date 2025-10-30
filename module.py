from math import *
import numpy as np

def f(x, expr):
    """Évalue la fonction f(x) saisie sous forme de texte."""
    return eval(expr)

def fprime(x, expr):
    """Dérivée numérique de f(x)."""
    h = 1e-6
    return (f(x + h, expr) - f(x - h, expr)) / (2 * h)

def balayage(expr, a, b, e):
    x = a
    while f(x, expr) * f(x + e, expr) > 0 and x + e <= b:
        x += e
    if x + e > b:
        print(" Aucune racine trouvée dans l'intervalle [a, b].")
        return None
    s = (x + x + e) / 2
    print("Méthode du balayage → Valeur approchée =", round(s, 6))
    return s

def dichotomie(expr, a, b, e):
    xg, xd = a, b
    if f(xg, expr) * f(xd, expr) > 0:
        print("Pas de changement de signe sur [a, b].")
        return None
    while abs(xd - xg) > e:
        s = (xg + xd) / 2
        if f(xg, expr) * f(s, expr) < 0:
            xd = s
        else:
            xg = s
    print("Méthode de dichotomie → Valeur approchée =", round(s, 6))
    return s

def lagrange(expr, a, b, e):
    x0, x1 = a, b
    if f(x0, expr) * f(x1, expr) > 0:
        print(" Pas de changement de signe sur [a, b].")
        return None
    while abs(x1 - x0) >= e:
        s = (x0 * f(x1, expr) - x1 * f(x0, expr)) / (f(x1, expr) - f(x0, expr))
        if f(s, expr) * f(x1, expr) < 0:
            x0 = s
        else:
            x1 = s
    print(" Méthode de la sécante (Lagrange) → Valeur approchée =", round(s, 6))
    return s

def newton(expr, a, e):
    s = a
    try:
        while abs(f(s, expr)) > e:
            s = s - f(s, expr) / fprime(s, expr)
    except ZeroDivisionError:
        print(" Division par zéro rencontrée (dérivée nulle).")
        return None
    print(" Méthode de Newton → Valeur approchée =", round(s, 6))
    return s

def elimination_gauss_numpy(M):

    n = M.shape[0]

    for i in range(n):
        # Vérification simple du pivot (gestion de l'erreur)
        if M[i, i] == 0:
            raise ValueError("Pivot nul détecté. Le système pourrait être singulier ou nécessiter un pivotement.")

        # Annuler les éléments sous le pivot
        for j in range(i + 1, n):
            facteur = M[j, i] / M[i, i]
            # Opération Ligne j <- Ligne j - facteur * Ligne i
            M[j, i:] = M[j, i:] - facteur * M[i, i:]

    return M

def gauss_jordan(M_augmente):

    M = M_augmente.copy()
    n = M.shape[0]
    for i in range(n):
        # Chercher le pivot (gestion simplifiée : pas de pivotement partiel)
        if M[i, i] == 0:
            raise ValueError("Pivot nul détecté.")

        # Normalisation : Diviser la ligne i par le pivot M[i, i]
        M[i, i:] = M[i, i:] / M[i, i]

        # Élimination SOUS le pivot (comme l'élimination de Gauss)
        for j in range(i + 1, n):
            facteur = M[j, i] / M[i, i]  # M[i,i] est censé être 1 ici, mais on recalcule le facteur de sécurité
            M[j, i:] = M[j, i:] - facteur * M[i, i:]

    # 2. PHASE DE REMONTÉE (Élimination au-dessus)
    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1): # On parcourt les lignes au-dessus de la ligne i
            facteur = M[j, i]
            M[j, i:] = M[j, i:] - facteur * M[i, i:]

    return M