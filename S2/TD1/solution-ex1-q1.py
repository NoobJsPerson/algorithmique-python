# Lire les variables a, b et c
a = int(input("Donner la valeur de a: "))
b = int(input("Donner la valeur de b: "))
c = int(input("Donner la valeur de c: "))

# `input` est pour lire valeur donné par le clavier en tapant sur le clavier et en appuyant sur Entrer.
# Entre paenthèses de `input` se trouve le texte qui va être affiché pour demander à l'utilisateur à donner une valuer.
# `input` donne un valeur à type `str` (chaine de charactères) mais nous voulons un valeur de type réel
# Alors nous devons convertir les valeurs à type réel en utilisant `int`

# Effectuer la permutation circulaire:
temp = a
a = c
c = b
b = temp

# La permutation circulaire est effectuée par donner la valeur de la dernière variable à le premier et par donner la valeur de chaque variable à l'une à sa droite.
# Un exemple de ceci pourrait être comme ça:
# Avant la permutation circulaire: a = 1, b = 2 et c = 3
# Aprés le permutation circulaire: a = 3, b = 1 et c = 2
# Si nous faisons cela directement, comme:
# 	a = c
# 	b = a
# 	c = b
# Nous allons perdre la valeur originale de `a` car il va être remplacée par la valeur de `c`.
# Par conséquence, Tous les variable vont avoir la valeur de `c`, et ce n'est pas que nous voulons.
# Alors nous devons avoir une variable temporaire pour stocker la valeur de `a` afin de ne pas la perdre.
# Et on va d'aboard donner `c` la valeur de `b` avant donner `b` la valeur originale de `a` stockée dans la variable temporaire pour ne donner pas `c` la valeur originale de `a` par accident.

# Écrire la resultat:
print("a = ", a, " , b = ", b, " et c = ", c)

# On utilise `print` pour écrire du texte sur la console.
# Dans les parenthèses de `print` on donne les chaines des charactères entouré par double apostrophe (")
# Ils pouvent être entouré par des apostrophes (')
