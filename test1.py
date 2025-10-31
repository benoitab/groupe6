from module import (
    balayage, dichotomie, lagrange, newton,
    elimination_gauss_numpy, gauss_jordan
)
import numpy as np
import sys
from math import *  


#  FONCTIONS UTILITAIRES POUR LA ROBUSTESSE

def get_float_input(prompt):
    """Demande un nombre réel (float) et boucle tant que la saisie est invalide."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")


def solve_triangular_system(M_triangulaire):
    """Résout un système triangulaire supérieur par substitution arrière."""
    n = M_triangulaire.shape[0]
    solution = np.zeros(n)

    # Remonte la matrice de la dernière ligne à la première
    for i in range(n - 1, -1, -1):
        # Soustrait les termes déjà calculés
        known_sum = np.dot(M_triangulaire[i, i + 1:n], solution[i + 1:n])

        # Calcule l'inconnue courante
        solution[i] = (M_triangulaire[i, n] - known_sum) / M_triangulaire[i, i]

    return solution



#  GESTION DES SYSTÈMES LINÉAIRES (AX = B)

def run_linear_systems():
    print("\n— SYSTÈMES LINÉAIRES (AX = B) —")

    try:
        # 1. SAISIE DE LA TAILLE (Robuste)
        n_float = get_float_input("Nombre d'inconnues (n) : ")
        if n_float != int(n_float) or n_float < 2:
            print("Le nombre d'inconnues doit être un entier supérieur ou égal à 2.")
            return
        n = int(n_float)

        M = np.zeros((n, n + 1))
        print(f"\nSaisie de la Matrice Augmentée [A | B], taille [{n}x{n + 1}].")

        # 2. SAISIE DES COEFFICIENTS (Robuste)
        for i in range(n):
            print(f"\n--- Équation {i + 1} ---")
            for j in range(n + 1):
                is_coefficient = (j < n)
                prompt = (f"Coefficient A[{i + 1},{j + 1}] (devant x{j + 1}) : "
                          if is_coefficient else f"Second membre B[{i + 1}] : ")
                M[i, j] = get_float_input(prompt)

        print("\nMatrice saisie :\n", M.round(4))

        # 3. CHOIX ET EXÉCUTION
        print("\n CHOIX DE LA MÉTHODE :")
        choice = input("1. Pivot de Gauss | 2. Gauss-Jordan | 9. Retour\nVotre choix : ")

        if choice == "1":
            print("\n— RÉSULTAT (Pivot de Gauss) —")
            M_triangulaire = elimination_gauss_numpy(M.copy())
            solution = solve_triangular_system(M_triangulaire)
            print("  Matrice Triangulaire :\n", M_triangulaire.round(4))
            print("  Solution x (Substitution arrière) :\n", solution.round(4))

        elif choice == "2":
            print("\n— RÉSULTAT (Gauss-Jordan) —")
            M_reduite = gauss_jordan(M.copy())
            solution = M_reduite[:, -1]
            print("  Matrice Échelonnée Réduite :\n", M_reduite.round(4))
            print("  Solution x (Lecture directe) :\n", solution.round(4))

        elif choice == "9":
            return

        else:
            print("Choix de méthode invalide.")

    except Exception as e:
        print(f"\nErreur fatale. Le système est peut-être singulier. Détail : {e}", file=sys.stderr)



# RECHERCHE DE RACINES (f(x) = 0)


def run_root_finding():
    print("\n— CALCUL DE RACINES (f(x) = 0) —")

    # 1. SAISIE INITIALE DES PARAMÈTRES (Robuste)
    try:
        print("\nATTENTION: Newton et Lagrange sont sensibles au point de départ/intervalle.")
        expr = input("Fonction f(x) (ex: cos(x) - x) : ")
        if not expr: return
        a = get_float_input("Début de l'intervalle a : ")
        b = get_float_input("Fin de l'intervalle b : ")
        e = get_float_input("Précision e : ")
    except Exception:
        print("Erreur de saisie des paramètres de la fonction.")
        return

    # 2. BOUCLE DU MENU D'EXÉCUTION
    while True:
        print("\n— CHOIX DE LA MÉTHODE —")

        methods = {
            "1": ("Balayage", balayage, (expr, a, b, e)),
            "2": ("Dichotomie", dichotomie, (expr, a, b, e)),
            "3": ("Lagrange (Sécante)", lagrange, (expr, a, b, e)),
            "4": ("Newton-Raphson", newton, (expr, a, e)),
        }

        # Affichage du menu
        for key, (name, *_) in methods.items():
            print(f"{key}. {name}")
        print("5. Exécuter TOUTES | 9. Retour à l'accueil")

        choice = input("Votre choix : ")

        try:
            if choice in methods:
                name, func, args = methods[choice]
                func(*args)

            elif choice == "5":
                print("\n--- EXÉCUTION DE TOUTES LES MÉTHODES ---")
                for _, func, args in methods.values():
                    func(*args)

            elif choice == "9":
                break

            else:
                print("Choix invalide. Veuillez réessayer.")

        except Exception as ex:
            print(f"\nErreur survenue pendant le calcul. Détail: {ex}")
            print("Conseil : Vérifiez l'expression, l'intervalle ou le point de départ.")


#  MENU PRINCIPAL (POINT D'ENTRÉE)

def main():
    while True:
        print("\n===========================================")
        print(" APPLICATION DE CALCUL SCIENTIFIQUE")
        print("===========================================")

        print("Choisissez le type d'opération :")
        print("1. Calcul de Racines (f(x) = 0)")
        print("2. Résolution de Systèmes Linéaires (AX = B)")
        print("0. Quitter")

        choice = input("\nVotre choix : ")

        if choice == "0":
            print("\nFin du programme. Merci de l'avoir utilisé ! Au revoir. ")
            break

        elif choice == "1":
            run_root_finding()

        elif choice == "2":
            run_linear_systems()

        else:
            print("Choix invalide. Veuillez choisir '1', '2' ou '0'.")


if __name__ == "__main__":
    main()
