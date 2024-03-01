# Question: Fusionner deux tableaux t1 et t2 dans un tableau t3.
t1 = []
t2 = []
t3 = []
continuer = True
while continuer:
	t1 = t1 + [int(input("Donner une valeur dans T1: "))]
	choix = input("Continuer a donner des valeurs? (oui pour continuer, tout le reste pour arrêter): ")
	if choix != "oui":
		continuer = False
print(t1)

continuer = True
while continuer:
	t2 = t2 + [int(input("Donner une valeur dans T2: "))]
	choix = input("Continuer a donner des valeurs? (oui pour continuer, tout le reste pour arrêter): ")
	if choix != "oui":
		continuer = False
print(t2)

for el in t1:
	t3 = t3 + [el]
for el in t2:
	t3 = t3 + [el]
print(t3)
