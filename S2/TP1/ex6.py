# Question 1:
a=float(input("Donner la valeur de a: "))
b=float(input("Donner la valeur de b: "))
x=-b/a
print(f"La solution est {x}")
# Question 2:
from math import sqrt
a=float(input("Donner la valeur de a: "))
b=float(input("Donner la valeur de b: "))
c=float(input("Donner la valeur de c: "))
if a!=0:
	det=b*b-4*a*c
	if det > 0:
		x1 = (-b-sqrt(det))/(2*a)
		x2 = (-b+sqrt(det))/(2*a)
		print("la première solution est", x1)
		print("la deuxième solution est", x2)
	elif det == 0:
		x = -b/(2*a)
		print("la solution est", x)
	else:
		xreel=-b/(2*a)
		ximaginaire1=-sqrt(-det)/(2*a)
		ximaginaire2=-ximaginaire1
		print(f"la première solution est ({xreel})+i({ximaginaire1})")
		print(f"la deuxième solution est ({xreel})+i({ximaginaire2})")
elif b!=0:
	print("la solution est", -c/b)
elif c!=0:
	print("l'équation n'admet pas des solutions")
else:
	print("tout nombres sont des solutions de cette équation")
