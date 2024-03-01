# Question 1:
x = int(input("Donner la valeur de x: "))
y = int(input("Donner la valeur de y: "))
temp = x
x = y
y = temp
print(f"x: {x}, y: {y}")
# Question 2:
x = int(input("Entrer un premier entier x : "))
y = int(input("Entrer un second entier y : "))
z = int(input("Entrer un 3ème entier z : "))
print(f"Avant la permutation x= {x}, y= {y} et z= {z}")
temp = x
x = y
y = z
z = temp
print(f"Après la permutation x= {x}, y= {y} et z= {z}")
