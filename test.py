from module import balayage, dichotomie, lagrange, newton


def main():
    print(" CALCUL DE RACINES D'UNE ÉQUATION ")

    # Initialize variables
    expr, a, b, e = "", 0.0, 0.0, 0.0

    while True:
        print("\n--- MENU DES MÉTHODES ---")
        print("1. Saisir les paramètres (Fonction, Intervalle, Précision)")
        print("2. Méthode du balayage")
        print("3. Méthode de la dichotomie")
        print("4. Méthode de Lagrange (sécante)")
        print("5. Méthode de Newton-Raphson")
        print("6. Exécuter TOUTES les méthodes")
        print("0. Quitter")

        choix = input("Votre choix : ")

        # CAS 0 : QUITTER (Check first for clean exit) 
        if choix == "0":
            print("\nFin du programme. À bientôt")
            break

        # CAS 1 : SAISIE DES PARAMÈTRES
        elif choix == "1":
            print("\n--- SAISIE DES PARAMÈTRES ---")
            try:
                expr = input("Entrez la fonction f(x) (ex: x**2 - 2) : ")
                a = float(input("Début de l'intervalle a : "))
                b = float(input("Fin de l'intervalle b : "))
                e = float(input("Précision (ex: 0.0001) : "))
                print("Paramètres enregistrés.") # Retrait de l'icône
            except ValueError:
                # Catches error if user enters non-numeric text for a, b, or e
                print("Erreur de saisie : Assurez-vous d'entrer des nombres valides pour a, b, et e.") # Retrait de l'icône
                # Reset parameters to avoid accidental use
                expr, a, b, e = "", 0.0, 0.0, 0.0

        # CAS 2 à 6 : EXÉCUTION DES MÉTHODES
        elif choix in ("2", "3", "4", "5", "6"):
            if not expr:
                print("Veuillez d'abord saisir les paramètres (Option 1).") # Retrait de l'icône
                continue  # Go back to menu

            # Execute methods within a try-except block to handle calculation errors
            try:
                if choix == "2":
                    balayage(expr, a, b, e)
                elif choix == "3":
                    dichotomie(expr, a, b, e)
                elif choix == "4":
                    lagrange(expr, a, b, e)
                elif choix == "5":  # Newton-Raphson (Note: Uses 'a' as initial guess, not 'b')
                    newton(expr, a, e)
                elif choix == "6":  # ALL methods
                    print("\n--- EXÉCUTION DE TOUTES LES MÉTHODES ---")
                    balayage(expr, a, b, e)
                    dichotomie(expr, a, b, e)
                    lagrange(expr, a, b, e)
                    newton(expr, a, e)

            except Exception as ex:
                # Catches ZeroDivisionError, NameError (if 'expr' is invalid math), etc., coming from module.py
                print(f"Une erreur est survenue pendant le calcul. Détails: {ex}") # Retrait de l'icône
                print("Vérifiez l'expression de la fonction, l'intervalle ou si la dérivée est nulle.")

        #  CAS INVALIDE 
        else:
            print("Choix invalide. Réessayez.") # Retrait de l'icône


if __name__ == "__main__":
    main()
