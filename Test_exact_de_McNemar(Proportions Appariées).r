# Test_exact_de_McNemar(Proportions Appariées)

# Création de données binaires appariées simulées :
# Intention d'achat : 0 = Non, 1 = Oui
# 100 personnes
achat_avant = c(rep(0, 30), rep(1, 70)) # 70 Oui avant
achat_apres = c(rep(0, 25), rep(1, 5), rep(0, 10), rep(1, 60))
# Les données sont ordonnées pour simuler les paires :
# 25 (Non -> Non)
# 5 (Non -> Oui)  <-- Discordant
# 10 (Oui -> Non) <-- Discordant
# 60 (Oui -> Oui)

# Construction de la table de contingence (doit être carrée)
Tableau_McNemar = table(Apres = achat_apres, Avant = achat_avant)
print("Table de Contingence (McNemar):")
print(Tableau_McNemar)

?mcnemar.test()
print("Test exact de McNemar : Après vs Avant")
# Teste l'hypothèse nulle qu'il n'y a pas de changement marginal (la proportion de Non->Oui est égale à la proportion de Oui->Non)
print(mcnemar.test(Tableau_McNemar, correct = FALSE))
