p = int(input("Donner la valeur de p: "))
n = int(input("Donner la valeur de n: "))
def factorielle(nombre):
		if nombre == 0:
			return 1
		return nombre * factorielle(nombre-1)
if n < 0 or p < 0 or n < p:
	print("p et n doit être des entiers naturel et n doit être superieur ou égale p")
else:
	resultat = factorielle(n) / (factorielle(p) * factorielle(n-p))
	print(resultat)
