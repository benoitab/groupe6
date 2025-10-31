# Test des rangs signés de Wilcoxon (Apparié) 

# Création de données appariées simulées (ex: Mesures 'Avant' et 'Après' une cure)
set.seed(42)
# Mesures Avant : Loin de la normale pour justifier un test non-paramétrique
avant = rchisq(50, df = 3)
# Mesures Après : Simplement "avant" + une petite diminution moyenne
apres = avant - runif(50, min = 0.5, max = 1.5)

?wilcox.test()
print("Test de Wilcoxon (Apparié) : Avant vs Après")
# 'paired = TRUE' indique que ce sont des observations liées
print(wilcox.test(avant, apres, paired = TRUE, alternative = "two.sided"))

# Teste l'hypothèse nulle que la médiane des différences est égale à zéro.
