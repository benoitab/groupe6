# Création des données simulées
# x3: Taille (prédicteur)
x3 <- rnorm(100, mean = 170, sd = 10)
# Variable de réponse (Poids)
y_gaussien <- 50 + 0.5 * x3 + rnorm(100, sd = 5)

# Application du GLM Gaussien (Régression Linéaire Classique)
modele_gaussien <- glm(y_gaussien ~ x3, family = gaussian(link = "identity"))

# Affichage des résultats
print("Résultats de la Régression Linéaire Classique (GLM Gaussien):")
print(summary(modele_gaussien))
# Note : C'est équivalent à lm(y_gaussien ~ x3)
