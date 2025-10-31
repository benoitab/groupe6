# Création des données simulées
# x2: Nombre d'heures d'utilisation (prédicteur)
x2 <- runif(100, min = 1, max = 10)
# Taux (lambda) de la distribution de Poisson, dépendant de x2
lambda <- exp(1 + 0.5 * x2)
# Variable de réponse (nombre de pannes)
y_comptage <- rpois(100, lambda = lambda)

# Application du GLM Poisson (Régression de Poisson)
modele_poisson <- glm(y_comptage ~ x2, family = poisson(link = "log"))

# Affichage des résultats
print("Résultats de la Régression de Poisson (GLM Poisson):")
print(summary(modele_poisson))
