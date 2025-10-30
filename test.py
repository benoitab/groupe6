from module import balayage, dichotomie, lagrange, newton

def main():
    print(" CALCUL DE RACINES D'UNE ÉQUATION ")
    expr = input("Entrez la fonction f(x) (ex: x**2 - 2) : ")
    a = float(input("Début de l'intervalle a : "))
    b = float(input("Fin de l'intervalle b : "))
    e = float(input("Précision (ex: 0.0001) : "))

    while True:
        print("\n--- MENU DES MÉTHODES ---")
        print("1. Méthode du balayage")
        print("2. Méthode de la dichotomie")
        print("3. Méthode de Lagrange (sécante)")
        print("4. Méthode de Newton-Raphson")
        print("5. Exécuter TOUTES les méthodes")
        print("0. Quitter")

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
        elif choix == "0":
            print("\nFin du programme. À bientôt 👋")
            break
        else:
            print("❌ Choix invalide. Réessayez.")

if __name__ == "__main__":
    main()
