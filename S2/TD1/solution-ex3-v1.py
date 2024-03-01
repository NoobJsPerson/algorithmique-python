notes = []
continuer = True
i = 0
somme = 0
min = float('inf')
while continuer:
	notes = notes + [int(input("Donner un note: "))]
	somme = somme + notes[i]
	if notes[i] < min:
		min = notes[i]
	i = i + 1
	choix = input("Continuer a donner des notes? (oui pour continuer, tout le reste pour arrêter): ")
	if choix != "oui":
		continuer = False
print(notes)
taille = i
moyenne = somme / taille
for note in notes:
	if note > moyenne:
		print(note, "est superieur à la moyenne")
print("le min est:", min)
el = int(input("Donner la note que vous voulez savoir sa nombre d'occurences: "))
occurences = 0
for note in notes:
	if note == el:
		occurences = occurences + 1
print("le nombre des occurences de", el, "est:", occurences)
# Tester si le tableau est trié par ordre croissant
triéCroi = True
triéDecroi = True
for i in range(taille-1):
	if notes[i] > notes[i+1]:
		triéCroi = False
		break
for i in range(taille-1):
	if notes[i] < notes[i+1]:
		triéDecroi = False
		break
if triéCroi:
	print("le tableau est trié par ordre croissant")
else:
	if triéDecroi:
		print("le tableau est trié par ordre decroissant")
	else:
		print("le tableau n'est pas trié")
	# Tri par selection
	m = 0
	for i in range(taille-1):
		m = i
		for j in range(i+1,taille):
			if notes[j] < notes[m]:
				m = j
		temp = notes[m]
		notes[m] = notes[i]
		notes[i] = temp
print(notes)
