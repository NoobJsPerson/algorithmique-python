# Question: Ecrire un algorithm qui remplit dex tableaux T1 et T2 dynamiques et les fusionne dans un tableau T3.
t1 = []
t2 = []
t3 = []
continuer = True
while continuer:
	t1 = t1 + [int(input("Donner une valeur dans T1: "))]
	choix = input("Continuer a donner des valeurs? (oui pour continuer, tout le reste pour arrêter): ")
	if choix != "oui":
		continuer = False

m = 0
taille1 = len(t1)
for i in range(taille1-1):
	m=i
	for j in range(i+1,taille1):
		if t1[j] < t1[m]:
			m=j
	temp = t1[i]
	t1[i] = t1[m]
	t1[m] = temp

print(t1)

continuer = True
while continuer:
	t2 = t2 + [int(input("Donner une valeur dans T2: "))]
	choix = input("Continuer a donner des valeurs? (oui pour continuer, tout le reste pour arrêter): ")
	if choix != "oui":
		continuer = False

m = 0
taille2 = len(t2)
for i in range(taille2-1):
	m=i
	for j in range(i+1,taille2):
		if t2[j] < t2[m]:
			m=j
	temp = t2[i]
	t2[i] = t2[m]
	t2[m] = temp


print(t2)

for el in t1:
	t3 = t3 + [el]
for el in t2:
	t3 = t3 + [el]

m = 0
taille3 = taille1 + taille2
for i in range(taille3-1):
	m=i
	for j in range(i+1,taille3):
		if t3[j] < t3[m]:
			m=j
	temp = t3[i]
	t3[i] = t3[m]
	t3[m] = temp


print(t3)
