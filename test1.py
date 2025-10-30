from module import(
    balayage, dichotomie, lagrange, newton,
    elimination_gauss_numpy, substitution_arriere, gauss_jordan
)
import numpy as np
import sys
from math import *
def resoudre_systemes_interactif():

    print("\n— RÉSOLUTION DE SYSTÈMES LINÉAIRES (AX = B) —")

    try:
        #  SAISIE DE LA TAILLE
        n = int(input("Entrez le nombre d'inconnues (n) : "))
        if n < 2:
            print(" le système doit avoir au moins 2 inconnues.")
            return

        M = np.zeros((n, n + 1))
        print(
            f"\nVous allez saisir les coefficients de la matrice [{n}x{n}] et le vecteur B (taille {n + 1} colonnes).")
        print(
            "Pour le système 2x1 + 3x2 = 7, vous entrez '2' pour le coefficient A[1,1], '3' pour A[1,2], et '7' pour B[1].")

        #  SAISIE DES COEFFICIENTS
        print("\n--- Saisie de la Matrice Augmentée [A | B] ---")
        for i in range(n):
            print(f"\n--- Ligne {i + 1} / Équation {i + 1} ---")
            for j in range(n + 1):
                if j < n:
                    val = float(input(f"Coefficient A[{i + 1},{j + 1}] (devant l'inconnue x{j + 1}) : "))
                else:
                    # Saisie du second membre b
                    val = float(input(f"Second membre B[{i + 1}] (valeur à droite du signe '=') : "))
                M[i, j] = val

        print("\nMatrice saisie :\n", M.round(4))

        # 4. CHOIX DE LA MÉTHODE
        print("\n CHOIX DE LA MÉTHODE ")
        print("1. Pivot de Gauss ")
        print("2. Méthode de Gauss-Jordan ")
        choix_syslin = input("Votre choix (1 ou 2) : ")

        print("\n RÉSULTAT ")

        if choix_syslin == "1":
            M_triangulaire = elimination_gauss_numpy(M.copy())
            solution = substitution_arriere(M_triangulaire)
            print("  Méthode choisie : Pivot de Gauss.")
            print("  Matrice Triangulaire (prête pour la remontée):\n", M_triangulaire.round(4))
            print("  Solution x (obtenue par substitution arrière):\n", solution.round(4))

        elif choix_syslin == "2":
            M_reduite = gauss_jordan(M.copy())
            solution = M_reduite[:, -1]
            print("  Méthode choisie : Gauss-Jordan.")
            print("  Matrice Échelonnée Réduite:\n", M_reduite.round(4))
            print("  Solution x (lue directement dans la dernière colonne):\n", solution.round(4))

        else:
            print("Choix de méthode invalide. Veuillez choisir '1' ou '2'.")

    except ValueError as e:
        print(f"Erreur de saisie. Assurez-vous d'entrer des nombres. Détail : {e}", file=sys.stderr)
    except Exception as e:
        print(f" Une erreur interne est survenue. Le système est peut-être singulier. Détail : {e}", file=sys.stderr)


def executer_racines():
    print("\n CALCUL DE valeurs approchées ")
    print("-----------------------------------")
    print("ATTENTION: Newton et Lagrange sont sensibles au point de départ/intervalle.")
    try:
        expr = input("Entrez la fonction f(x) (ex: cos(x) - x, x**2 - 2) : ")
        a = float(input("Début de l'intervalle a (ex: 0) : "))
        b = float(input("Fin de l'intervalle b (ex: 1) : "))
        e = float(input("Précision e (ex: 0.0001) : "))
    except ValueError:
        print("Saisie invalide pour les nombres.")
        return

    while True:
        print("\n MENU DES MÉTHODES ")
        print("1. Balayage | 2. Dichotomie | 3. Lagrange (Sécante) | 4. Newton-Raphson")
        print("5. Exécuter TOUTES | 9. Retour à l'accueil")

        choix = input("Votre choix : ")

        if choix == "1":
            balayage(expr, a, b, e)
        elif choix == "2":
            dichotomie(expr, a, b, e)
        elif choix == "3":
            lagrange(expr, a, b, e)
        elif choix == "4":
            newton(expr, a, e)
        elif choix == "5":
            balayage(expr, a, b, e)
            dichotomie(expr, a, b, e)
            lagrange(expr, a, b, e)
            newton(expr, a, e)
        elif choix == "9":
            break
        else:
            print("Choix invalide. Réessayez.")


def main():
    while True:
        print("\n")
        print("Choisissez le type d'opération à effectuer :")
        print("1. Calcul de valeurs approchées (f(x) = 0)")
        print("2. Résolution de Systèmes Linéaires (AX = B)")
        print("0. Quitter")

        choix_principal = input("Votre choix : ")

        if choix_principal == "1":
            executer_racines()

        elif choix_principal == "2":
            resoudre_systemes_interactif()  # Lancement de la saisie interactive

        elif choix_principal == "0":
            print("\nFin du programme. Merci de l'avoir utilisé ! ")
            break

        else:
            print(" Choix invalide. Veuillez choisir '1', '2' ou '0'.")


if __name__ == "__main__":
    main()