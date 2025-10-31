# Création des données simulées
set.seed(42)
n <- 100
# Variable de prédiction (quantité/dose)
x1 <- rnorm(n, mean = 10, sd = 2)
# Variable de réponse binaire (probabilité de succès dépendant de x1)
proba <- 1 / (1 + exp(3 - 0.3 * x1))
y_binaire <- rbinom(n, size = 1, prob = proba)

# Application du GLM Binomial (Régression Logistique)
modele_logistique <- glm(y_binaire ~ x1, family = binomial(link = "logit"))

# Affichage des résultats
print("Résultats de la Régression Logistique (GLM Binomial):")
print(summary(modele_logistique))
